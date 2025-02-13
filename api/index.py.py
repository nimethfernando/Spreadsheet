from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import os
from flask import send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'


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
    
    if file1 and file2:
        # Save the uploaded files
        file1_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Our.xlsx')
        file2_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Invoice.xlsx')
        file1.save(file1_path)
        file2.save(file2_path)

        # Now proceed with your processing logic
        try:
            # Load files
            file1_df = pd.read_excel(file1_path, dtype=str, keep_default_na=False)
            file2_df = pd.read_excel(file2_path, dtype=str, keep_default_na=False)
            
            # Print column names to check if they match
            print("File1 Columns (Our.xlsx):", file1_df.columns)
            print("File2 Columns (Invoice.xlsx):", file2_df.columns)

            # Check if the columns 'Empty Perfects' and 'Perfect with External Returns' exist in file2_df
            if 'Empty Perfects' in file2_df.columns and 'Perfect with External Returns' in file2_df.columns:
                # Filter file2 (Invoice file) if the columns exist
                file2Unique = file2_df[(file2_df['Empty Perfects'] != '1') & (file2_df['Perfect with External Returns'] != '1')]
            else:
                # If the columns don't exist, skip filtering
                file2Unique = file2_df

            similar_rows = []
            non_similar_rows = []

            # Iterate over the file2 (Invoice) DataFrame row by row
            for i, row_df2 in file2Unique.iterrows():
                is_similar_found = False  # Track if any similar row is found for the current row_df2
                
                for j, row_df1 in file1_df.iterrows():
                    # Flag to check if rows are similar
                    is_similar = False

                    if ((row_df1['Site'] == row_df2[' Site ']) and
                        (row_df1['Perfects Project'] == row_df2[' Project ']) and
                        (abs(float(row_df2[' Total Net Time TM with Empty clips (HRS) ']) - 
                             float(row_df1['Net Time AIP [h]'])) < 1)):
                        is_similar = True

                    if is_similar:
                        similar_rows.append(row_df2)  # Append from file2 (Invoice)
                        is_similar_found = True
                        break  # No need to continue once a similar row is found

                if not is_similar_found:
                    non_similar_rows.append(row_df2)  # Append from file2 (Invoice)

            # Convert the results into DataFrames
            similar_df = pd.DataFrame(similar_rows)
            non_similar_df = pd.DataFrame(non_similar_rows)

            output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'harro.xlsx')

            # Save the DataFrames to Excel with two sheets: one for similar and one for non-similar
            with pd.ExcelWriter(output_file) as writer:
                similar_df.to_excel(writer, sheet_name="Similar", index=False)
                non_similar_df.to_excel(writer, sheet_name="Non-Similar", index=False)

            return "Files processed successfully. Download the result: <a href='/download/harro.xlsx'>Download</a>"
        
        except Exception as e:
            return f"Unexpected error occurred during file process: {e}"

    return redirect(url_for('index'))


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')
    app.run(debug=True)
