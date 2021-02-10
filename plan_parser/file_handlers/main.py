import os

from plan_parser.csv_handler import CsvHandler
# from plan_parser.plan_handler import determine_second_lowest_silver_plan, create_zip_code_collections, create_output
from plan_parser.file_handlers.utls import open_files
from plan_parser.file_handlers.plan_handler import PlanHandler

from pprint import pprint

test_output = f"test_data{os.sep}output_data.csv"

test_message = {
    "input_message": {"message": [f'test_data{os.sep}plans.csv', f'test_data{os.sep}slcsp.csv', f'test_data{os.sep}zips.csv']}
}


def main():
    file_generators = open_files(files)
    output = PlanHandler(file_generators['plans'], file_generators['zips'], file_generators["slcsp"]).generate_output_plan("silver")
    CsvHandler(test_output).write_to_csv(output)


main()