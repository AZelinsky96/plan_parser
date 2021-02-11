import os

from file_handlers.csv_handler import CsvHandler
from file_handlers.utls import open_files, build_file_path
from file_handlers.plan_handler import PlanHandler

from pprint import pprint


def process_output(files):
    file_generators = open_files(files)
    output = PlanHandler(file_generators['plans'], file_generators['zips'], file_generators["slcsp"]).generate_output_plan("silver")
    return output


def write_output(output_file_name, output):
    CsvHandler(output_file_name).write_to_csv(output)
