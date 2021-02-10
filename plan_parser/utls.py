import os
from plan_parser.file_handlers.csv_handler import CsvHandler


def parse_file_names(file_names):
    return [file_name.replace(" ", "").replace("'", "") for file_name in file_names.replace("[", "").replace("]", "").split(",")]

def validate_file_presence(file_names):
    for file_ in file_names:
        if not os.path.exists(os.path.join(app.config['FILE_UPLOADS'], file_)):
            raise ValueError(f"Invalid File: {file_}. Check pathway of uploaded file and Config for file path.")
# def parse_message(message):
#     message = message['input_message']['message']
#     return message


# def open_files(files):
#     return {file_.split(f"{os.sep}")[-1].split(".")[0]: CsvHandler(file_).create_csv_generator() for file_ in files}
