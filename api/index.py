from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/uploads'  # Use /tmp for serverless compatibility

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file1' not in request.files or 'file2' not in request.files:
        return "No file part"
    
    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '' or file2.filename == '':
        return "No selected file"
    
    # Ensure /tmp/uploads exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Our.xlsx')
    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Invoice.xlsx')
    file1.save(file1_path)
    file2.save(file2_path)

    try:
        file1_df = pd.read_excel(file1_path, dtype=str, keep_default_na=False)
        file2_df = pd.read_excel(file2_path, dtype=str, keep_default_na=False)

        # Filter logic
        if 'Empty Perfects' in file2_df.columns and 'Perfect with External Returns' in file2_df.columns:
            file2Unique = file2_df[(file2_df['Empty Perfects'] != '1') & (file2_df['Perfect with External Returns'] != '1')]
        else:
            file2Unique = file2_df

        similar_rows = []
        non_similar_rows = []

        for i, row_df2 in file2Unique.iterrows():
            is_similar_found = False
            for j, row_df1 in file1_df.iterrows():
                is_similar = False
                if ((row_df1['Site'] == row_df2[' Site ']) and
                    (row_df1['Perfects Project'] == row_df2[' Project ']) and
                    (abs(float(row_df2[' Total Net Time TM with Empty clips (HRS) ']) - 
                         float(row_df1['Net Time AIP [h]'])) < 1)):
                    is_similar = True
                if is_similar:
                    similar_rows.append(row_df2)
                    is_similar_found = True
                    break
            if not is_similar_found:
                non_similar_rows.append(row_df2)

        similar_df = pd.DataFrame(similar_rows)
        non_similar_df = pd.DataFrame(non_similar_rows)

        output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'harro.xlsx')
        with pd.ExcelWriter(output_file) as writer:
            similar_df.to_excel(writer, sheet_name="Similar", index=False)
            non_similar_df.to_excel(writer, sheet_name="Non-Similar", index=False)

        # Optional: Clean up input files (not output, as it's needed for download)
        try:
            os.remove(file1_path)
            os.remove(file2_path)
        except Exception:
            pass

        return "Files processed successfully. Download the result: <a href='/download/harro.xlsx'>Download</a>"
    
    except Exception as e:
        return f"Unexpected error occurred during file process: {e}"

    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_from_directory(
            os.path.abspath(app.config['UPLOAD_FOLDER']),
            filename,
            as_attachment=True
        )
    except FileNotFoundError:
        return "File expired or not found", 404
