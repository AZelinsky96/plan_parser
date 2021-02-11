import csv


class CsvHandler:

    def __init__(self, file_name):
        self.file_name = file_name
    
    def create_csv_generator(self):
        with open(self.file_name) as infile:
            csv_reader = csv.reader(infile, delimiter=",")
            for line in csv_reader:
                yield line
    
    def write_to_csv(self, file_data):
        with open(self.file_name, mode="w") as outfile:
            outfile_writer = csv.writer(outfile, delimiter=",")
            for line in file_data:
                outfile_writer.writerow(line)
