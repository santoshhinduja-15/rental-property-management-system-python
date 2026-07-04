from datetime import datetime

from config.constants import (
    ALLOCATIONS_FILE,
    PROPERTIES_FILE,
    TENANTS_FILE,
    ALLOCATION_PREFIX,
    OCCUPIED,
    VACANT
)

from models.allocation import Allocation

from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.validators import Validators


class AllocationService:

    @staticmethod
    def allocate_property():

        property_id = input(
            "Enter Property ID: "
        ).strip()

        tenant_id = input(
            "Enter Tenant ID: "
        ).strip()

        property_records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        tenant_records = FileHandler.read_records(
            TENANTS_FILE
        )

        property_exists = False
        tenant_exists = False
        property_status = None

        for record in property_records:

            data = record.split("|")

            if data[0] == property_id:
                property_exists = True
                property_status = data[5]
                break

        for record in tenant_records:

            data = record.split("|")

            if data[0] == tenant_id:
                tenant_exists = True
                break

        errors = Validators.validate_allocation(
            property_exists,
            tenant_exists,
            property_status,
            property_status == OCCUPIED
        )

        if (
            tenant_exists
            and
            AllocationService.tenant_has_active_allocation(
                tenant_id
            )
        ):
            errors.append(
                "Tenant already has an active property allocation."
            )

        if errors:

            for error in errors:
                print(error)

            return

        allocation_id = IdGenerator.generate_id(
            ALLOCATIONS_FILE,
            ALLOCATION_PREFIX
        )

        allocation_date = datetime.now().strftime(
            "%d-%m-%Y"
        )

        allocation = Allocation(
            allocation_id,
            property_id,
            tenant_id,
            allocation_date
        )

        FileHandler.write_record(
            ALLOCATIONS_FILE,
            allocation.to_record()
        )

        updated_properties = []

        for record in property_records:

            data = record.split("|")

            if data[0] == property_id:
                data[5] = OCCUPIED

            updated_properties.append(
                "|".join(data)
            )

        FileHandler.overwrite_records(
            PROPERTIES_FILE,
            updated_properties
        )

        print(
            f"Property allocated successfully. Allocation ID: {allocation_id}"
        )

    @staticmethod
    def view_allocations():

        allocation_records = FileHandler.read_records(
            ALLOCATIONS_FILE
        )

        if not allocation_records:
            print("No allocations found.")
            return

        property_records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        tenant_records = FileHandler.read_records(
            TENANTS_FILE
        )

        property_map = {}

        for record in property_records:

            data = record.split("|")

            property_map[data[0]] = data[1]

        tenant_map = {}

        for record in tenant_records:

            data = record.split("|")

            tenant_map[data[0]] = data[1]

        print(
            "\n{:<10} {:<20} {:<20} {:<15}".format(
                "ALLOC ID",
                "PROPERTY",
                "TENANT",
                "DATE"
            )
        )

        print("-" * 70)

        for record in allocation_records:

            data = record.split("|")

            allocation_id = data[0]
            property_id = data[1]
            tenant_id = data[2]
            allocation_date = data[3]

            property_name = property_map.get(
                property_id,
                "N/A"
            )

            tenant_name = tenant_map.get(
                tenant_id,
                "N/A"
            )

            print(
                "{:<10} {:<20} {:<20} {:<15}".format(
                    allocation_id,
                    property_name,
                    tenant_name,
                    allocation_date
                )
            )

    @staticmethod
    def tenant_has_active_allocation(
        tenant_id
    ):

        records = FileHandler.read_records(
            ALLOCATIONS_FILE
        )

        for record in records:

            data = record.split("|")

            if data[2] == tenant_id:
                return True

        return False

    @staticmethod
    def get_property_by_tenant(
        tenant_id
    ):

        records = FileHandler.read_records(
            ALLOCATIONS_FILE
        )

        for record in records:

            data = record.split("|")

            if data[2] == tenant_id:
                return data[1]

        return None

    @staticmethod
    def property_is_allocated_to_tenant(
        property_id,
        tenant_id
    ):

        records = FileHandler.read_records(
            ALLOCATIONS_FILE
        )

        for record in records:

            data = record.split("|")

            if (
                data[1] == property_id
                and
                data[2] == tenant_id
            ):
                return True

        return False

    @staticmethod
    def tenant_exists(
        tenant_id
    ):

        records = FileHandler.read_records(
            TENANTS_FILE
        )

        for record in records:

            data = record.split("|")

            if data[0] == tenant_id:
                return True

        return False

    @staticmethod
    def property_exists(
        property_id
    ):

        records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        for record in records:

            data = record.split("|")

            if data[0] == property_id:
                return True

        return False

    @staticmethod
    def view_tenant_allocation(
        tenant_id
    ):

        allocation_records = FileHandler.read_records(
            ALLOCATIONS_FILE
        )

        property_records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        property_map = {}

        for record in property_records:

            data = record.split("|")

            property_map[data[0]] = data[1]

        found = False

        for record in allocation_records:

            data = record.split("|")

            if data[2] == tenant_id:

                print(
                    f"\nAllocation ID : {data[0]}"
                )

                print(
                    f"Property      : {property_map.get(data[1], 'N/A')}"
                )

                print(
                    f"Date          : {data[3]}"
                )

                found = True

        if not found:
            print("No allocation found.")

    @staticmethod
    def remove_allocation(
        tenant_id
    ):

        allocation_records = FileHandler.read_records(
            ALLOCATIONS_FILE
        )

        property_id = None

        updated_allocations = []

        for record in allocation_records:

            data = record.split("|")

            if (
                data[2] == tenant_id
                and
                property_id is None
            ):
                property_id = data[1]
                continue

            updated_allocations.append(
                record
            )

        FileHandler.overwrite_records(
            ALLOCATIONS_FILE,
            updated_allocations
        )

        if property_id:

            property_records = FileHandler.read_records(
                PROPERTIES_FILE
            )

            updated_properties = []

            for record in property_records:

                data = record.split("|")

                if data[0] == property_id:
                    data[5] = VACANT

                updated_properties.append(
                    "|".join(data)
                )

            FileHandler.overwrite_records(
                PROPERTIES_FILE,
                updated_properties
            )

        return property_id