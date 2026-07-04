import os

class FileHandler:
    @staticmethod
    def create_file_if_not_exists(file_path):
        directory = os.path.dirname(file_path)
        
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass

    @staticmethod
    def read_records(file_path):
        FileHandler.create_file_if_not_exists(file_path)

        with open(file_path, "r") as file:
            records = []

            for line in file:
                line = line.strip()

                if line:
                    records.append(line)

            return records

    @staticmethod
    def write_record(file_path,record):
        FileHandler.create_file_if_not_exists(file_path)

        with open(file_path, "a") as file:
            file.write(record + "\n")

    @staticmethod
    def overwrite_records(file_path, records):
        FileHandler.create_file_if_not_exists(file_path)
        with open(file_path, "w") as file:

            for record in records:
                file.write(record + "\n")