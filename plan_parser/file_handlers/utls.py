import os
from plan_parser.file_handlers.csv_handler import CsvHandler


def validate_file_presence(file_names, file_pathway):
    for file_ in file_names:
        if not os.path.exists(os.path.join(file_pathway, file_)):
            raise ValueError(f"Invalid File: {file_}. Check pathway of uploaded file and Config for file path.")


def validate_file_path(file_path):
    if not(os.path.exists(file_path)):
        raise ValueError(f"Invalid File Path: {file_path}. Adjust config.")


def validate_output_type(file_name):
    if "csv" not in file_name:
        return False
    return True


def open_files(files):
    return {file_.split(f"{os.sep}")[-1].split(".")[0]: CsvHandler(file_).create_csv_generator() for file_ in files}


def build_file_path(leading_file_path, file_name):
    return os.path.join(leading_file_path, file_name)
