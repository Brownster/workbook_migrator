from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = {'csv'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # for example 16MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file1' not in request.files or 'file2' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file1 = request.files['file1']
        file2 = request.files['file2']

        # if user does not select file, browser submits an empty part without filename
        if file1.filename == '' or file2.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            try:
                filename1 = secure_filename(file1.filename)
                filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
                file1.save(filepath1)

                filename2 = secure_filename(file2.filename)
                filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
                file2.save(filepath2)

                # CSV comparison logic here (omitted for brevity)
                # ...

                return send_from_directory(directory=app.config['UPLOAD_FOLDER'], filename=filename1, as_attachment=True)

            except Exception as e:
                flash('Error processing files. Please ensure they are valid CSVs.')
                return redirect(request.url)

        else:
            flash('Allowed file types are .csv')
            return redirect(request.url)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
