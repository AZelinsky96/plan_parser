import os
import pytest

from plan_parser.file_handlers.plan_handler import PlanHandler
from plan_parser.file_handlers.csv_handler import CsvHandler

FILE_PATH = os.path.join("tests", "test_data")


@pytest.fixture
def plan_handler():

    return PlanHandler(
        CsvHandler(os.path.join(FILE_PATH, "test_plan.csv")).create_csv_generator(),
        CsvHandler(os.path.join(FILE_PATH, "test_zips.csv")).create_csv_generator(),
        CsvHandler(os.path.join(FILE_PATH, "test_slcsp.csv")).create_csv_generator()
    )

@pytest.fixture
def plan_output():
    return {('MO', '3'): [298.24, 361.15, 325.71], ('MT', '3'): [240.0], ('NJ', '1'): [262.65]}


@pytest.fixture
def sorted_plans():
    return {('MO', '3'): [298.24, 325.71], ('MT', '3'): [240.0], ('NJ', '1'): [262.65]}


@pytest.fixture
def zip_codes_info():
    return {'zipcode': {'identifying_area': [('state', 'rate_area')]},
            '64148': {'identifying_area': [('MO', '3')]}, 
            '40813': {'identifying_area': [('KY', '8')]}, 
            '54923': {'identifying_area': [('WI', '11'), ('WI', '15')]}, 
            '07184': {'identifying_area': [('NJ', '1')]}}

class TestPlanHandler:


    @pytest.mark.parametrize(
        'plan_type, expected',
        [
            ('foo', ('foo',)),
            (['foo', 'bar'], ('foo', 'bar')),
            ('', ("bronze", "silver", "gold", "platinum"))
        ]
    )
    def test_determine_plan_type_with_single_input(self, plan_handler, plan_type, expected):
        assert expected == plan_handler.determine_plan_type(plan_type)

    def test_determine_plans_by_area(self, plan_handler, plan_output):
        assert plan_output == plan_handler.determine_plans_by_area(plan_handler.plan_entries, ("silver", ))
    
    def test_sort_and_find_lowest_entries(self, plan_handler, plan_output, sorted_plans):
        assert sorted_plans == plan_handler.sort_and_find_lowest_prices(plan_output)
        
    def test_create_zip_code_collection(self, plan_handler, zip_codes_info):
        assert zip_codes_info == plan_handler.create_zip_code_collections(plan_handler.zips)

    def test_create_output(self, plan_handler, sorted_plans, zip_codes_info):
        expected = [['zipcode', 'rate'], ('64148', 325.71), ('40813',), ('54923',), ('07184',)]
        assert expected == plan_handler.create_output(sorted_plans, zip_codes_info)
