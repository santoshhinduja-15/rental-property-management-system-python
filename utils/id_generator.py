from utils.file_handler import FileHandler

class IdGenerator:
    @staticmethod
    def generate_id(file_path, prefix):
        records = FileHandler.read_records(file_path)

        if not records:
            return f"{prefix}101"

        max_number = 100

        for record in records:
            data = record.split("|")
            current_id = data[0]

            try:
                number = int(current_id.replace(prefix, ""))

                if number > max_number:
                    max_number = number

            except ValueError:
                continue

        return f"{prefix}{max_number + 1}"