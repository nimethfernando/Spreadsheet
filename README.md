Flask File Upload and Processing Application
Overview
<p>This Flask application allows users to upload two Excel files (<code>Our.xlsx</code> and <code>Invoice.xlsx</code>), process the data in these files, and download the results. It compares the content between the two files based on specific conditions and outputs two sets of data: similar rows and non-similar rows. The processed result is saved in an Excel file (<code>harro.xlsx</code>) that can be downloaded by the user.</p>
Features
<ul> <li><strong>Upload two Excel files</strong>: Users can upload two files (<code>Our.xlsx</code> and <code>Invoice.xlsx</code>).</li> <li><strong>File validation</strong>: Ensures that both files are uploaded and have valid content.</li> <li><strong>Data comparison</strong>: Compares rows between the two files based on specific criteria, such as matching <code>Site</code>, <code>Perfects Project</code>, and <code>Total Net Time</code>.</li> <li><strong>Result generation</strong>: Outputs two sets of data: similar rows and non-similar rows.</li> <li><strong>Download processed result</strong>: The processed results are saved in an Excel file with two sheets (<code>Similar</code> and <code>Non-Similar</code>), which can be downloaded.</li> </ul>
Installation
Prerequisites
<p>Before running the application, make sure you have the following installed:</p> <ul> <li>Python 3.x</li> <li>Flask</li> <li>Pandas</li> <li>OpenPyXL (for working with Excel files)</li> </ul> <p>You can install these dependencies using the following command:</p>
bash
Copy code
pip install flask pandas openpyxl
Directory Setup
<p>This application requires an <code>uploads</code> directory where uploaded files will be stored and processed. If this directory doesn't exist, the application will automatically create it on startup.</p>
How to Run
<ol> <li><strong>Download or clone the code</strong> to your local machine.</li> <li><strong>Navigate to the directory</strong> where the code is saved.</li> <li>Run the following command to start the Flask application:</li> </ol>
bash
Copy code
python app.py
<p>4. Open your web browser and go to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</p>
Usage
<ol> <li><strong>Upload Files</strong>: <ul> <li>The home page (<code>/</code>) will present a form to upload two Excel files: <code>Our.xlsx</code> and <code>Invoice.xlsx</code>.</li> <li>The files should have the following structure: <ul> <li><code>Our.xlsx</code> should contain columns: <code>Site</code>, <code>Perfects Project</code>, <code>Net Time AIP [h]</code>.</li> <li><code>Invoice.xlsx</code> should contain columns: <code> Site </code>, <code> Project </code>, <code> Total Net Time TM with Empty clips (HRS) </code>, <code>Empty Perfects</code>, and <code>Perfect with External Returns</code>.</li> </ul> </li> </ul> </li>
less
Copy code
<li><strong>File Processing</strong>: 
    <ul>
        <li>Once files are uploaded, the application will process the files by comparing the rows based on:
            <ul>
                <li>Matching values in the <code>Site</code> and <code>Perfects Project</code> columns.</li>
                <li>The difference between the <code>Total Net Time</code> from <code>Invoice.xlsx</code> and <code>Net Time</code> from <code>Our.xlsx</code> should be less than 1 hour.</li>
            </ul>
        </li>
        <li>It will also filter rows in <code>Invoice.xlsx</code> where <code>Empty Perfects</code> or <code>Perfect with External Returns</code> is not <code>1</code> (if these columns exist).</li>
    </ul>
</li>

<li><strong>Download Results</strong>: 
    <ul>
        <li>After processing, a link to download the processed results will be displayed.</li>
        <li>The output file (<code>harro.xlsx</code>) will contain two sheets:
            <ul>
                <li><code>Similar</code>: Rows from <code>Invoice.xlsx</code> that matched the rows in <code>Our.xlsx</code>.</li>
                <li><code>Non-Similar</code>: Rows from <code>Invoice.xlsx</code> that did not match any row in <code>Our.xlsx</code>.</li>
            </ul>
        </li>
    </ul>
</li>

<li><strong>Download the file</strong>: Click on the download link to download the processed Excel file.</li>
</ol>
