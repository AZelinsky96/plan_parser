import logging
import os
from flask import Flask, render_template, request, url_for, redirect, session
from file_handlers.utls import parse_file_names, validate_file_presence

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['FILE_UPLOADS'] = os.path.join(os.getcwd(), "plan_parser", "static", "file_uploads")


@app.route("/")
def landing_page():
    return render_template("base_page/landing_page.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        if request.files:
            requested_files = request.files.getlist('file')
            file_names = []
            for uploaded_file in requested_files:
                file_name = uploaded_file.filename
                file_names.append(file_name)
                uploaded_file.save(os.path.join(app.config['FILE_UPLOADS'], file_name))
            
            return redirect(url_for("receive_files", file_names=file_names))
    return render_template("plan_parsing/upload.html")


@app.route("/receive_files/<file_names>", methods=["GET", "POST"])
def receive_files(file_names):
    session['files'] = parse_file_names(file_names)
    return render_template('plan_parsing/process.html', file_names=session['files'])


@app.route("/process_files", methods=['GET', 'POST'])
def process_files():
    if request.method == "POST":
        file_names = session.get("files", None)
        if file_names:
            print(f"Processing Files: {file_names}")
            validate_file_presence(file_names, app.config['FILE_UPLOADS'])
            # develop main method to intake files and parse them. Ensure that all three files are present.

        

    return render_template('plan_parsing/download.html')

app.run(debug=True, host='0.0.0.0')
