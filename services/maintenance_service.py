from config.constants import (MAINTENANCE_FILE, MAINTENANCE_PENDING, MAINTENANCE_PREFIX, TENANTS_FILE)
from models.maintenance import Maintenance
from utils.file_handler import FileHandler
from utils.validators import Validators
from utils.id_generator import IdGenerator

class MaintenanceService:

    @staticmethod
    def raise_request(tenant_id):
        description = input("Enter Description: ").strip()
        errors = Validators.validate_maintenance(description)

        if errors:

            for error in errors:
                print(error)

            return

        maintenance_id = IdGenerator.generate_id(MAINTENANCE_FILE, MAINTENANCE_PREFIX)
        request = Maintenance(maintenance_id,tenant_id, description, MAINTENANCE_PENDING)
        FileHandler.write_record(MAINTENANCE_FILE, request.to_record())

        print(
            f"Maintenance request submitted successfully. "
            f"Maintenance ID: {maintenance_id}"
            )

    @staticmethod
    def view_requests():
        records = FileHandler.read_records(MAINTENANCE_FILE)

        if not records:
            print("No maintenance requests found.")
            return

        tenant_records = FileHandler.read_records(TENANTS_FILE)
        tenant_map = {}

        for record in tenant_records:
            data = record.split("|")
            tenant_map[data[0]] = data[1]

        print("\n{:<10} {:<20} {:<35} {:<15}".format("ID", "TENANT", "DESCRIPTION", "STATUS"))
        print("-" * 85)

        for record in records:
            data = record.split("|")

            print("{:<10} {:<20} {:<35} {:<15}".format(data[0],tenant_map.get(data[1], "N/A"),data[2], data[3]))

    @staticmethod
    def update_request_status():
        maintenance_id = input("Enter Maintenance ID: ").strip()

        print("\n1. In Progress")
        print("2. Completed")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            new_status = "In Progress"

        elif choice == "2":
            new_status = "Completed"

        else:
            print("Invalid choice.")
            return
        
        records = FileHandler.read_records(MAINTENANCE_FILE)
        updated_records = []
        found = False

        for record in records:
            data = record.split("|")

            if data[0] == maintenance_id:
                found = True
                current_status = data[3]
                errors = (Validators.validate_maintenance_status_transition(current_status, new_status))

                if errors:

                    for error in errors:
                        print(error)

                    return

                data[3] = new_status
            updated_records.append("|".join(data))

        if not found:
            print("Maintenance request not found.")
            return

        FileHandler.overwrite_records(MAINTENANCE_FILE,updated_records)
        print("Maintenance status updated successfully.")

    @staticmethod
    def view_tenant_requests(tenant_id):
        records = FileHandler.read_records(MAINTENANCE_FILE)
        found = False
        print("\n{:<10} {:<40} {:<15}".format("ID","DESCRIPTION", "STATUS"))
        print("-" * 70)

        for record in records:
            data = record.split("|")

            if data[1] == tenant_id:
                print("{:<10} {:<40} {:<15}".format(data[0], data[2], data[3]))
                found = True

        if not found:
            print("No maintenance requests found.")