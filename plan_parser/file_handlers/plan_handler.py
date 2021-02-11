class PlanHandler:
    
    PLANS = ("bronze", "silver", "gold", "platinum")

    def __init__(self, plan_entries, zips, desired_zips):
        self.plan_entries = plan_entries
        self.zips = zips
        self.desired_zips = desired_zips
    # Create validation method to make sure that plans adhere to one of four above
    # Create validation method to make sure that the files entered have appropriate keys for zips and plans.
    
    def generate_output_plan(self, plan_type=None):
        plan_type = self.determine_plan_type(plan_type)
        plans_by_rate_area = self.determine_plans_by_area(self.plan_entries, plan_type)
        sorted_plans = self.sort_and_find_lowest_prices(plans_by_rate_area)
        zip_codes = self.create_zip_code_collections(self.zips)
        return self.create_output(sorted_plans, zip_codes)

    def determine_plan_type(self, plan_type):
        if plan_type:
            if isinstance(plan_type, str):
                plan = (plan_type,)
            else:
                plan = tuple(plan_type)
        else:
            plan = self.PLANS

        return plan


    def determine_plans_by_area(self, plans, plan_type):
        plans_by_rate_area = {}
        for line in plans:
            if line[2].lower() in plan_type:
                insert_value = float(line[3])
                key_value = (line[1], line[-1])
                if key_value not in plans_by_rate_area:
                    plans_by_rate_area[key_value] = [insert_value]
                else:
                    plans_by_rate_area[key_value].append(insert_value)
        
        return plans_by_rate_area


    def sort_and_find_lowest_prices(self, plans_by_rate_area):
        for key, value in plans_by_rate_area.items():
            set_value = set(value)
            if len(set_value) == 1:
                plans_by_rate_area[key] = [value[0]]
            else:
                sorted_list = sorted(set_value)
                plans_by_rate_area[key] = sorted_list[:2]
        
        return plans_by_rate_area


    def create_zip_code_collections(self, zip_codes):
        zip_code_info = {

        }

        for line in zip_codes:
            zip_ = line[0]
            insert_value = (line[1], line[-1])
            if zip_ not in zip_code_info:
                zip_code_info[zip_] = {
                    "identifying_area": [insert_value]
                }

            else:
                if insert_value not in zip_code_info[zip_]['identifying_area']:
                    zip_code_info[zip_]['identifying_area'].append(insert_value)
        
        return zip_code_info


    def create_output(self, sorted_plans, zip_codes_info):
        header = next(self.desired_zips)
        output_structure = [header]
        for zip_code in self.desired_zips:
            zip_ = zip_code[0]
            zip_code_info_data = zip_codes_info.get(zip_)
            identifying_areas = zip_code_info_data['identifying_area']
            if len(identifying_areas) == 1:
                identifying_area = identifying_areas[0]
                plan_prices = sorted_plans.get(identifying_area)
                if plan_prices:
                    if len(plan_prices) > 1:
                        output_structure.append((zip_, plan_prices[-1]))
                        pass
                    else:
                        output_structure.append((zip_,))
                else:
                    output_structure.append((zip_,))
            else:
                output_structure.append((zip_,))
        return output_structure

