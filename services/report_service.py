from config.constants import (PROPERTIES_FILE, TENANTS_FILE, RENTS_FILE, VACANT, OCCUPIED, PAID, PENDING)
from utils.file_handler import FileHandler

class ReportService:
    @staticmethod
    def property_report():
        records = FileHandler.read_records(PROPERTIES_FILE)
        total = len(records)
        vacant = 0
        occupied = 0

        for record in records:
            data = record.split("|")

            if data[5] == VACANT:
                vacant += 1

            elif data[5] == OCCUPIED:
                occupied += 1

        print(f"Total Properties : {total}")
        print(f"Vacant Properties : {vacant}")
        print(f"Occupied Properties : {occupied}")

    @staticmethod
    def tenant_report():
        records = FileHandler.read_records(TENANTS_FILE)
        print(f"Total Tenants : {len(records)}")

    @staticmethod
    def rent_report():
        records = FileHandler.read_records(RENTS_FILE)
        total_rent = 0
        paid_rent = 0
        pending_rent = 0

        for record in records:
            data = record.split("|")
            amount = float(data[4])
            total_rent += amount

            if data[5] == PAID:
                paid_rent += amount

            elif data[5] == PENDING:
                pending_rent += amount

        print(f"Total Rent Generated : {total_rent}")
        print(f"Total Rent Collected : {paid_rent}")
        print(f"Pending Rent : {pending_rent}")

    @staticmethod
    def income_report():
        records = FileHandler.read_records(RENTS_FILE)
        total_income = 0

        for record in records:
            data = record.split("|")

            if data[5] == PAID:
                total_income += float(data[4])

        print(f"Total Income : {total_income}")