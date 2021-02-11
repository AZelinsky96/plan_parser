import logging
import os
from flask import Flask, render_template, request, url_for, redirect, session, send_file
from file_handlers.utls import (
    parse_file_names, validate_file_presence, build_file_path, validate_output_type, validate_file_path
    )
from file_handlers.main import process_output
from file_handlers.main import write_output


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['FILE_UPLOADS'] = os.path.join(os.getcwd(), "plan_parser", "static", "file_uploads")
app.config['FILE_OUTPUTS'] = os.path.join(os.getcwd(), "plan_parser", "static", "file_outputs")

@app.route("/")
def landing_page():
    return render_template("base_page/landing_page.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        if request.files:
            requested_files = request.files.getlist('file')
            if len(requested_files) != 3:
                return render_template("plan_parsing/uploadError.html")
            
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
            file_path = app.config['FILE_UPLOADS']
            validate_file_presence(file_names, file_path)
            complete_files = [build_file_path(file_path, file_) for file_ in file_names]
            output = process_output(complete_files)
            if output:
                session['file_output'] = output
            # Ensure that all three files are present.
    return render_template('plan_parsing/download.html')


@app.route("/download_files", methods=["GET", "POST"])
def download_files():

    output_file_name = request.form.get("file_output")

    output_true = validate_output_type(output_file_name)
    if not output_true:
        return render_template('plan_parsing/downloadError.html')
    output_data = session.get("file_output")
    if (output_data != None) & (output_file_name != None):
        output_file_path = app.config['FILE_OUTPUTS']
        validate_file_path(output_file_path)
        file_path = build_file_path(output_file_path, output_file_name)
        write_output(file_path, output_data)

        return send_file(file_path, attachment_filename=output_file_name)

app.run(debug=True, host='0.0.0.0')
