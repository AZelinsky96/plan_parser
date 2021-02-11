import os
import pytest
import csv

from unittest.mock import patch 
from plan_parser.file_handlers.csv_handler import (
    CsvHandler
)

@pytest.fixture
def csv_object():
    return CsvHandler(file_name=None)

class TestCsvHandler:
    FILE_PATH = os.path.join("tests", "test_data")

    def test_create_csv_generator(self, csv_object):
        csv_object.file_name = os.path.join(self.FILE_PATH, "test.csv")
        expected_head = ["test_head_1", "test_head_2"]
        assert expected_head == next(csv_object.create_csv_generator())
    
    def test_write_to_csv(self, csv_object):
        test_name = "test_output.csv"
        csv_object.file_name = os.path.join(self.FILE_PATH, test_name)
        test_data = [
            ("foo", "bar"),
            ("foo1", "bar2")
        ]

        csv_object.write_to_csv(test_data)
        test_file_path = os.path.join(self.FILE_PATH, test_name)
        result = os.path.exists(test_file_path)
        if result:
            os.remove(test_file_path)

        assert result