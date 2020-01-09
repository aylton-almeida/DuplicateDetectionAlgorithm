import csv


class FileHelper:
    file: str
    delimiter: str

    def __init__(self, file, delimiter):
        self.file = file
        self.delimiter = delimiter

    # Returns a dictionary from the file
    def read_file(self):
        with open(self.file) as file:
            reader = csv.DictReader(file, delimiter=self.delimiter)
            return list(reader)
