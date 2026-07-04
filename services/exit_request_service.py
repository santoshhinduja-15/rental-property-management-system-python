from datetime import datetime
from config.constants import (EXIT_REQUESTS_FILE, ALLOCATIONS_FILE, PROPERTIES_FILE, TENANTS_FILE, VACANT, EXIT_PENDING, EXIT_APPROVED, EXIT_PREFIX)
from models.exit_request import ExitRequest
from utils.file_handler import FileHandler
from utils.validators import Validators
from utils.id_generator import IdGenerator

class ExitRequestService:
    @staticmethod
    def create_exit_request(tenant_id):
        active_property = False
        allocation_records = FileHandler.read_records(ALLOCATIONS_FILE)

        for record in allocation_records:
            data = record.split("|")

            if data[2] == tenant_id:
                active_property = True
                break

        request_records = FileHandler.read_records(EXIT_REQUESTS_FILE)
        pending_request_exists = False

        for record in request_records:
            data = record.split("|")

            if (data[1] == tenant_id and data[3] == EXIT_PENDING):
                pending_request_exists = True
                break

        errors = Validators.validate_exit_request(active_property, pending_request_exists)
        if errors:

            for error in errors:
                print(error)

            return

        exit_id = IdGenerator.generate_id(EXIT_REQUESTS_FILE, EXIT_PREFIX)
        request_date = datetime.now().strftime("%d-%m-%Y")
        request = ExitRequest(exit_id, tenant_id, request_date, EXIT_PENDING)
        FileHandler.write_record(EXIT_REQUESTS_FILE, request.to_record())
        print(f"Exit request submitted successfully. Exit ID: {exit_id}")

    @staticmethod
    def approve_exit_request():
        exit_id = input("Enter Exit Request ID: ").strip()
        records = FileHandler.read_records(EXIT_REQUESTS_FILE)
        found = False
        tenant_id = None
        updated_records = []

        for record in records:
            data = record.split("|")

            if data[0] == exit_id:
                found = True

                if data[3] == EXIT_APPROVED:
                    print("Exit request already approved.")
                    return

                tenant_id = data[1]
                data[3] = EXIT_APPROVED
            
            updated_records.append("|".join(data))

        if not found:
            print("Exit request not found.")
            return

        FileHandler.overwrite_records(EXIT_REQUESTS_FILE, updated_records)
        allocation_records = FileHandler.read_records(ALLOCATIONS_FILE)
        property_id = None
        remaining_allocations = []

        for record in allocation_records:
            data = record.split("|")

            if (data[2] == tenant_id and property_id is None):
                property_id = data[1]
                continue

            remaining_allocations.append(record)
        FileHandler.overwrite_records(ALLOCATIONS_FILE, remaining_allocations)

        if property_id:
            property_records = FileHandler.read_records(PROPERTIES_FILE)
            updated_properties = []

            for record in property_records:
                data = record.split("|")

                if data[0] == property_id:
                    data[5] = VACANT

                updated_properties.append("|".join(data))
            FileHandler.overwrite_records(PROPERTIES_FILE, updated_properties)
        print("Exit request approved successfully.")

    @staticmethod
    def view_exit_requests():
        records = FileHandler.read_records(EXIT_REQUESTS_FILE)

        if not records:
            print("No exit requests found.")
            return

        tenant_records = FileHandler.read_records(TENANTS_FILE)
        tenant_map = {}

        for record in tenant_records:
            data = record.split("|")
            tenant_map[data[0]] = data[1]

        print("\n{:<10} {:<20} {:<15} {:<12}".format("EXIT ID","TENANT", "DATE", "STATUS"))
        print("-" * 60)

        for record in records:
            data = record.split("|")
            exit_id = data[0]
            tenant_id = data[1]
            request_date = data[2]
            status = data[3]

            print("{:<10} {:<20} {:<15} {:<12}".format(exit_id,tenant_map.get(tenant_id,"N/A"),request_date,status))