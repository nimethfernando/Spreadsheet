Flask File Upload and Processing App
Overview
<p>This app allows users to upload two Excel files (<code>Our.xlsx</code> and <code>Invoice.xlsx</code>), compare their content, and download the processed result. The app matches rows based on specific conditions and saves the output to a new Excel file.</p>
Features
<ul> <li>Upload two Excel files (<code>Our.xlsx</code> and <code>Invoice.xlsx</code>).</li> <li>Compares rows based on column matches (e.g., <code>Site</code>, <code>Perfects Project</code>).</li> <li>Generates a downloadable Excel file with two sheets: <ul> <li><strong>Similar</strong>: Matching rows.</li> <li><strong>Non-Similar</strong>: Non-matching rows.</li> </ul> </li> </ul>
Installation
<p>To run the app, you'll need the following:</p> <ul> <li>Python 3.x</li> <li>Flask</li> <li>Pandas</li> <li>OpenPyXL</li> </ul> <p>Install the required libraries:</p>
pip install flask pandas openpyxl
Running the App
<ol> <li>Clone the repository or download the files.</li> <li>Run the app using:</li> </ol>

python app.py

<p>3. Visit <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a> in your browser.</p>
