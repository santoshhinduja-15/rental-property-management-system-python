from config.constants import (COMPLAINTS_FILE, COMPLAINT_OPEN, COMPLAINT_PREFIX, TENANTS_FILE)
from models.complaint import Complaint
from utils.file_handler import FileHandler
from utils.validators import Validators
from utils.id_generator import IdGenerator

class ComplaintService:
    @staticmethod
    def raise_complaint(tenant_id):
        title = input("Enter Complaint Title: ").strip()
        description = input("Enter Complaint Description: ").strip()
        errors = Validators.validate_complaint(title, description)

        if errors:

            for error in errors:
                print(error)

            return

        complaint_id = IdGenerator.generate_id(COMPLAINTS_FILE, COMPLAINT_PREFIX)
        complaint = Complaint(complaint_id, tenant_id, title, description, COMPLAINT_OPEN)
        FileHandler.write_record(COMPLAINTS_FILE, complaint.to_record())
        print(f"Complaint submitted successfully. Complaint ID: {complaint_id}")

    @staticmethod
    def view_complaints():
        complaint_records = FileHandler.read_records(COMPLAINTS_FILE)

        if not complaint_records:
            print("No complaints found.")
            return

        tenant_records = FileHandler.read_records(TENANTS_FILE)
        tenant_map = {}

        for record in tenant_records:
            data = record.split("|")
            tenant_map[data[0]] = data[1]
        print("\n" + "=" * 90)
        print(" " * 35 + "COMPLAINT LIST")
        print("=" * 90)

        for record in complaint_records:
            data = record.split("|")
            print(f"\nComplaint ID : {data[0]}")
            print(f"Tenant       : {tenant_map.get(data[1], 'N/A')}")
            print(f"Title        : {data[2]}")
            print(f"Description  : {data[3]}")
            print(f"Status       : {data[4]}")
            print("-" * 90)

    @staticmethod
    def update_complaint_status():
        complaint_id = input("Enter Complaint ID: ").strip()
        print("\n1. In Progress")
        print("2. Resolved")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            new_status = "In Progress"

        elif choice == "2":
            new_status = "Resolved"

        else:
            print("Invalid choice.")
            return

        records = FileHandler.read_records(COMPLAINTS_FILE)
        updated_records = []
        found = False

        for record in records:
            data = record.split("|")

            if data[0] == complaint_id:
                found = True
                current_status = data[4]
                errors = (Validators.validate_complaint_status_transition(current_status, new_status))

                if errors:

                    for error in errors:
                        print(error)

                    return

                data[4] = new_status
            updated_records.append("|".join(data))

        if not found:
            print("Complaint not found.")
            return

        FileHandler.overwrite_records(COMPLAINTS_FILE, updated_records)
        print("Complaint status updated successfully.")

    @staticmethod
    def view_tenant_complaints(tenant_id):
        records = FileHandler.read_records(COMPLAINTS_FILE)
        found = False

        print("\n" + "=" * 50)
        print("               MY COMPLAINTS")
        print("=" * 50)

        for record in records:
            data = record.split("|")

            if data[1] == tenant_id:
                print(f"\nComplaint ID : {data[0]}")
                print(f"Title        : {data[2]}")
                print(f"Description  : {data[3]}")
                print(f"Status       : {data[4]}")
                print("-" * 50)
                found = True

        if not found:
            print("No complaints found.")