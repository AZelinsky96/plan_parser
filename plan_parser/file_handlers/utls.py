import os
from plan_parser.csv_handler import CsvHandler


def parse_message(message):
    message = message['input_message']['message']
    return message


def open_files(files):
    return {file_.split(f"{os.sep}")[-1].split(".")[0]: CsvHandler(file_).create_csv_generator() for file_ in files}
