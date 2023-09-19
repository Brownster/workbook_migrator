@app.route('/', methods=['GET', 'POST'])
def index():
    download_link = None

    if request.method == 'POST':
        # ... rest of your code ...

        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            filename1 = None  # Add this line here
            try:
                # ... rest of your code ...

                result_filename = "result.csv"
                result_filepath = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)
                combined_csv.to_csv(result_filepath, index=False)

                download_link = url_for('download_file', filename=result_filename)
                return render_template('index.html', download_link=download_link)

            except Exception as e:
                flash('Error processing files. Please ensure they are valid CSVs.')

    return render_template('index.html', download_link=download_link)
