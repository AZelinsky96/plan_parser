import os
import pytest

from unittest.mock import patch
from plan_parser.file_handlers.csv_handler import CsvHandler
from plan_parser.file_handlers.utls import (
    validate_file_presence, validate_file_path, validate_output_type,
    open_files, build_file_path
)

class TestUtls:
    FILE_PATH = os.path.join("tests", "test_data")
    
    def test_validate_file_presence(self):
        test_file = ["test.csv"]
        assert validate_file_presence(test_file, self.FILE_PATH) is None

    def test_validate_file_presence_error(self):
        test_file = ['gibberish.csv']
        with pytest.raises(ValueError):
            validate_file_presence(test_file, self.FILE_PATH)

    def test_validate_file_path(self):
        assert validate_file_path(self.FILE_PATH) is None

    def test_validate_file_path_error(self):
        with pytest.raises(ValueError):
            validate_file_path("gibberish")

    def test_validate_output_type(self):
        assert validate_output_type("output.csv") == True

    def test_validate_output_type_false(self):
        assert validate_output_type("gibberish") == False

    def test_open_files(self):
        test_files = [f"test{os.sep}data.csv"]
        expected_output = {'data': 'foobar'}
        with patch.object(CsvHandler, 'create_csv_generator', return_value="foobar") as mock_method:
            assert expected_output == open_files(test_files)
    
    def test_build_file_path(self):
        assert f"test{os.sep}data" == build_file_path("test", "data")
