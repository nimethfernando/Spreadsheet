Flask File Upload and Processing App
Overview
<p>This app allows users to upload two Excel files (<code>Our.xlsx</code> and <code>Invoice.xlsx</code>), compare their content, and download the processed result. The app matches rows based on specific conditions and saves the output to a new Excel file.</p>
Features
<ul> <li>Upload two Excel files (<code>Our.xlsx</code> and <code>Invoice.xlsx</code>).</li> <li>Compares rows based on column matches (e.g., <code>Site</code>, <code>Perfects Project</code>).</li> <li>Generates a downloadable Excel file with two sheets: <ul> <li><strong>Similar</strong>: Matching rows.</li> <li><strong>Non-Similar</strong>: Non-matching rows.</li> </ul> </li> </ul>

Installation

1. Install the dependencies

    ```bash
    pip install flask pandas openpyxl
    ```
    
2. Run the Flask app

    ```bash
    python app.py
    ```

5. Open the app in your browser:

    - Go to http://127.0.0.1:5000/

