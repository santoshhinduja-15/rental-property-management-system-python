import re
from config.constants import (TENANTS_FILE, ALLOCATIONS_FILE, TENANT_PREFIX)
from models.tenant import Tenant
from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.validators import Validators
from services.auth_service import AuthService

class TenantService:
    @staticmethod
    def add_tenant():
        name = input("Enter Tenant Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        tenant_id = IdGenerator.generate_id(TENANTS_FILE,TENANT_PREFIX)
        records = FileHandler.read_records(TENANTS_FILE)
        existing_ids = []
        existing_usernames = []

        for record in records:
            data = record.split("|")
            existing_ids.append(data[0])
            existing_usernames.append(data[4])

        errors = Validators.validate_tenant(tenant_id, name, phone, email, username, existing_ids, existing_usernames)

        if errors:

            for error in errors:
                print(error)

            return

        password_hash = AuthService.hash_password(password)
        tenant = Tenant(tenant_id, name, phone, email, username, password_hash)
        FileHandler.write_record(TENANTS_FILE, tenant.to_record())
        print(f"Tenant created successfully. Tenant ID: {tenant_id}")

    @staticmethod
    def view_tenants():

        records = FileHandler.read_records(
            TENANTS_FILE
        )

        if not records:
            print("No tenants found.")
            return

        print(
            "\n{:<8} {:<20} {:<12} {:<30} {:<15}".format(
                "ID",
                "NAME",
                "PHONE",
                "EMAIL",
                "USERNAME"
            )
        )

        print("-" * 90)

        for record in records:

            data = record.split("|")

            print(
                "{:<8} {:<20} {:<12} {:<30} {:<15}".format(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4]
                )
            )

    @staticmethod
    def update_tenant():
        tenant_id = input("Enter Tenant ID: ").strip()
        records = FileHandler.read_records(TENANTS_FILE)
        found = False
        updated_records = []
        usernames = []

        for record in records:
            data = record.split("|")
            usernames.append(data[4])

        for record in records:
            data = record.split("|")

            if data[0] == tenant_id:
                found = True
                print("\nLeave blank to keep existing value.")
                name = input(f"Name ({data[1]}): ").strip()
                phone = input(f"Phone ({data[2]}): ").strip()
                email = input(f"Email ({data[3]}): ").strip()
                username = input(f"Username ({data[4]}): ").strip()

                new_name = (
                    name
                    if name
                    else data[1]
                )

                new_phone = (
                    phone
                    if phone
                    else data[2]
                )

                new_email = (
                    email
                    if email
                    else data[3]
                )

                new_username = (
                    username
                    if username
                    else data[4]
                )

                errors = []

                if not new_name.strip():
                    errors.append("Tenant name cannot be empty.")

                if not new_phone.isdigit():
                    errors.append("Phone number must contain only digits.")

                if len(new_phone) != 10:
                    errors.append("Phone number must be exactly 10 digits.")

                if new_phone and new_phone[0] not in "6789":
                    errors.append("Phone number must start with 6, 7, 8 or 9.")

                if len(new_phone) == 10 and len(set(new_phone)) == 1:
                    errors.append("Phone number cannot contain the same digit repeated 10 times.")

                email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
                if not re.match(email_pattern, new_email):
                    errors.append("Enter a valid email address.")

                for existing_username in usernames:
                    if existing_username == new_username and existing_username != data[4]:
                        errors.append("Username already exists.")
                        break

                if errors:

                    for error in errors:
                        print(error)

                    return

                data[1] = new_name
                data[2] = new_phone
                data[3] = new_email
                data[4] = new_username

            updated_records.append("|".join(data))

        if not found:
            print("Tenant not found.")
            return

        FileHandler.overwrite_records(TENANTS_FILE, updated_records)
        print("Tenant updated successfully.")

    @staticmethod
    def remove_tenant():
        tenant_id = input("Enter Tenant ID: ").strip()
        allocation_records = FileHandler.read_records(ALLOCATIONS_FILE)

        for record in allocation_records:
            data = record.split("|")

            if data[2] == tenant_id:
                print("Tenant with active property allocation cannot be removed.")
                return
        
        records = FileHandler.read_records(TENANTS_FILE)
        found = False
        updated_records = []

        for record in records:
            data = record.split("|")

            if data[0] == tenant_id:
                found = True
                continue

            updated_records.append(record)

        if not found:
            print("Tenant not found.")
            return

        FileHandler.overwrite_records(TENANTS_FILE, updated_records)
        print("Tenant removed successfully.")

    @staticmethod
    def view_assigned_property(tenant_id):
        allocation_records = FileHandler.read_records(ALLOCATIONS_FILE)
        property_id = None

        for record in allocation_records:
            data = record.split("|")

            if data[2] == tenant_id:
                property_id = data[1]
                break

        if not property_id:
            print("No property assigned.")
            return

        from config.constants import (PROPERTIES_FILE)
        property_records = FileHandler.read_records(PROPERTIES_FILE)

        for record in property_records:
            data = record.split("|")
            
            if data[0] == property_id:
                print("\nPROPERTY DETAILS")
                print("-" * 50)
                print(f"Property ID   : {data[0]}")
                print(f"Property Name : {data[1]}")
                print(f"Property Type : {data[2]}")
                print(f"Address       : {data[3]}")
                print(f"Monthly Rent  : {data[4]}")
                print(f"Status        : {data[5]}")

            return
        print("Assigned property record not found.")