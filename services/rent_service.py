from config.constants import (
    RENTS_FILE,
    RENT_PREFIX,
    PENDING,
    PROPERTIES_FILE,
    TENANTS_FILE
)

from models.rent import Rent

from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.validators import Validators

from services.allocation_service import AllocationService


class RentService:

    @staticmethod
    def generate_rent():

        tenant_id = input(
            "Enter Tenant ID: "
        ).strip()

        property_id = input(
            "Enter Property ID: "
        ).strip()

        errors = []

        if not AllocationService.tenant_exists(
            tenant_id
        ):
            errors.append(
                "Tenant does not exist."
            )

        if not AllocationService.property_exists(
            property_id
        ):
            errors.append(
                "Property does not exist."
            )

        if (
            AllocationService.tenant_exists(
                tenant_id
            )
            and
            AllocationService.property_exists(
                property_id
            )
            and
            not AllocationService.property_is_allocated_to_tenant(
                property_id,
                tenant_id
            )
        ):
            errors.append(
                "Property is not allocated to the specified tenant."
            )

        month = input(
            "Enter Month (Example: July-2026): "
        ).strip()

        amount = input(
            "Enter Rent Amount: "
        ).strip()

        rent_id = IdGenerator.generate_id(
            RENTS_FILE,
            RENT_PREFIX
        )

        records = FileHandler.read_records(
            RENTS_FILE
        )

        duplicate_month = False

        for record in records:

            data = record.split("|")

            if (
                data[1] == tenant_id
                and
                data[3].lower() == month.lower()
            ):
                duplicate_month = True
                break

        errors.extend(
            Validators.validate_rent(
                amount,
                duplicate_month
            )
        )

        if errors:

            for error in errors:
                print(error)

            return

        rent = Rent(
            rent_id,
            tenant_id,
            property_id,
            month,
            amount,
            PENDING
        )

        FileHandler.write_record(
            RENTS_FILE,
            rent.to_record()
        )

        print(
            f"Rent generated successfully. Rent ID: {rent_id}"
        )

    @staticmethod
    def view_rents():

        records = FileHandler.read_records(
            RENTS_FILE
        )

        if not records:
            print("No rent records found.")
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
            "\n{:<10} {:<20} {:<20} {:<15} {:<12} {:<10}".format(
                "RENT ID",
                "TENANT",
                "PROPERTY",
                "MONTH",
                "AMOUNT",
                "STATUS"
            )
        )

        print("-" * 95)

        for record in records:

            data = record.split("|")

            print(
                "{:<10} {:<20} {:<20} {:<15} {:<12} {:<10}".format(
                    data[0],
                    tenant_map.get(
                        data[1],
                        "N/A"
                    ),
                    property_map.get(
                        data[2],
                        "N/A"
                    ),
                    data[3],
                    data[4],
                    data[5]
                )
            )

    @staticmethod
    def view_tenant_rents(
        tenant_id
    ):

        records = FileHandler.read_records(
            RENTS_FILE
        )

        property_records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        property_map = {}

        for record in property_records:

            data = record.split("|")

            property_map[data[0]] = data[1]

        found = False

        print(
            "\n{:<10} {:<20} {:<15} {:<12} {:<10}".format(
                "RENT ID",
                "PROPERTY",
                "MONTH",
                "AMOUNT",
                "STATUS"
            )
        )

        print("-" * 75)

        for record in records:

            data = record.split("|")

            if data[1] == tenant_id:

                print(
                    "{:<10} {:<20} {:<15} {:<12} {:<10}".format(
                        data[0],
                        property_map.get(
                            data[2],
                            "N/A"
                        ),
                        data[3],
                        data[4],
                        data[5]
                    )
                )

                found = True

        if not found:
            print("No rent records found.")

    @staticmethod
    def view_pending_rents():

        records = FileHandler.read_records(
            RENTS_FILE
        )

        if not records:
            print("No pending rents found.")
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

        found = False

        print(
            "\n{:<10} {:<20} {:<20} {:<15} {:<12} {:<10}".format(
                "RENT ID",
                "TENANT",
                "PROPERTY",
                "MONTH",
                "AMOUNT",
                "STATUS"
            )
        )

        print("-" * 95)

        for record in records:

            data = record.split("|")

            if data[5] == PENDING:

                print(
                    "{:<10} {:<20} {:<20} {:<15} {:<12} {:<10}".format(
                        data[0],
                        tenant_map.get(
                            data[1],
                            "N/A"
                        ),
                        property_map.get(
                            data[2],
                            "N/A"
                        ),
                        data[3],
                        data[4],
                        data[5]
                    )
                )

                found = True

        if not found:
            print("No pending rents found.")