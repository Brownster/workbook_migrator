CSV Comparer Web App
Description:

This application is a Flask-based web tool designed to compare two CSV files based on specific criteria. When a user uploads two CSV files, the application checks if an ip_address from the second CSV exists in the first one. If it does, the values in the columns "Secret Server URL" and "Configuration Item" from the second CSV are copied over to the first CSV.
Features:

    User-Friendly Interface: Users can easily upload their CSV files through a simple web-based interface.
    Input Validation:
        The application ensures only valid .csv files are uploaded.
        There's a file size limit to prevent oversized files from being processed.
    Security:
        Uses secure_filename() to ensure uploaded filenames are safe.
        Only .csv extensions are permitted to mitigate potential security threats.

Intended Purpose:

This tool's primary intent is to assist in merging specific data from one CSV file to another based on the existence of certain criteria (in this case, an ip_address). This is especially useful for tasks that require consolidating data from various sources without manually going through each record.
Usage:

    Starting the Application:

    bash

    $ python app.py

    This will start the Flask server, and the application should be accessible via http://127.0.0.1:5000/.

    Uploading Files:
        Navigate to the provided URL.
        Use the upload buttons to select your two CSV files.
        Click "Submit" to process.

    Downloading Processed File:
    Once the files are processed, the updated first CSV will be automatically downloaded.

Dependencies:

    Flask: For the web interface.
    pandas: For CSV file processing.
