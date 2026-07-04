from config.constants import (
    PROPERTIES_FILE,
    PROPERTY_PREFIX,
    VACANT,
    OCCUPIED
)

from models.property import Property

from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator
from utils.validators import Validators


class PropertyService:

    @staticmethod
    def add_property():

        property_name = input(
            "Enter Property Name: "
        ).strip()

        property_type = input(
            "Enter Property Type: "
        ).strip()

        address = input(
            "Enter Address: "
        ).strip()

        monthly_rent = input(
            "Enter Monthly Rent: "
        ).strip()

        property_id = IdGenerator.generate_id(
            PROPERTIES_FILE,
            PROPERTY_PREFIX
        )

        records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        existing_ids = [
            record.split("|")[0]
            for record in records
        ]

        errors = Validators.validate_property(
            property_id,
            property_name,
            address,
            monthly_rent,
            existing_ids
        )

        if errors:

            for error in errors:
                print(error)

            return

        property_obj = Property(
            property_id,
            property_name,
            property_type,
            address,
            monthly_rent,
            VACANT
        )

        FileHandler.write_record(
            PROPERTIES_FILE,
            property_obj.to_record()
        )

        print(
            f"Property created successfully. Property ID: {property_id}"
        )

    @staticmethod
    def view_properties():

        records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        if not records:
            print("No properties found.")
            return

        print(
            "\n{:<12} {:<20} {:<12} {:<20} {:<12} {:<12}".format(
                "PROPERTY ID",
                "PROPERTY NAME",
                "TYPE",
                "ADDRESS",
                "RENT",
                "STATUS"
            )
        )

        print("-" * 95)

        for record in records:

            data = record.split("|")

            print(
                "{:<12} {:<20} {:<12} {:<20} {:<12} {:<12}".format(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5]
                )
            )

    @staticmethod
    def update_property():

        property_id = input(
            "Enter Property ID: "
        ).strip()

        records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        found = False
        updated_records = []

        for record in records:

            data = record.split("|")

            if data[0] == property_id:

                found = True

                print(
                    "\nLeave blank to keep existing value."
                )

                property_name = input(
                    f"Property Name ({data[1]}): "
                ).strip()

                property_type = input(
                    f"Property Type ({data[2]}): "
                ).strip()

                address = input(
                    f"Address ({data[3]}): "
                ).strip()

                monthly_rent = input(
                    f"Monthly Rent ({data[4]}): "
                ).strip()

                new_name = (
                    property_name
                    if property_name
                    else data[1]
                )

                new_type = (
                    property_type
                    if property_type
                    else data[2]
                )

                new_address = (
                    address
                    if address
                    else data[3]
                )

                new_rent = (
                    monthly_rent
                    if monthly_rent
                    else data[4]
                )

                errors = []

                if not new_name.strip():
                    errors.append(
                        "Property name cannot be empty."
                    )

                if not new_address.strip():
                    errors.append(
                        "Address cannot be empty."
                    )

                try:

                    rent = float(
                        new_rent
                    )

                    if rent <= 0:
                        errors.append(
                            "Monthly rent must be greater than zero."
                        )

                except ValueError:

                    errors.append(
                        "Monthly rent must be numeric."
                    )

                if errors:

                    for error in errors:
                        print(error)

                    return

                data[1] = new_name
                data[2] = new_type
                data[3] = new_address
                data[4] = str(new_rent)

            updated_records.append(
                "|".join(data)
            )

        if not found:
            print("Property not found.")
            return

        FileHandler.overwrite_records(
            PROPERTIES_FILE,
            updated_records
        )

        print(
            "Property updated successfully."
        )

    @staticmethod
    def delete_property():

        property_id = input(
            "Enter Property ID: "
        ).strip()

        records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        found = False
        updated_records = []

        for record in records:

            data = record.split("|")

            if data[0] == property_id:

                found = True

                if data[5] == OCCUPIED:

                    print(
                        "Occupied property cannot be deleted."
                    )

                    return

                continue

            updated_records.append(
                record
            )

        if not found:

            print(
                "Property not found."
            )

            return

        FileHandler.overwrite_records(
            PROPERTIES_FILE,
            updated_records
        )

        print(
            "Property deleted successfully."
        )

    @staticmethod
    def view_vacant_properties():

        records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        found = False

        print(
            "\n{:<12} {:<20} {:<12} {:<20} {:<12} {:<12}".format(
                "PROPERTY ID",
                "PROPERTY NAME",
                "TYPE",
                "ADDRESS",
                "RENT",
                "STATUS"
            )
        )

        print("-" * 95)

        for record in records:

            data = record.split("|")

            if data[5] == VACANT:

                print(
                    "{:<12} {:<20} {:<12} {:<20} {:<12} {:<12}".format(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5]
                    )
                )

                found = True

        if not found:
            print("No vacant properties found.")

    @staticmethod
    def view_occupied_properties():

        records = FileHandler.read_records(
            PROPERTIES_FILE
        )

        found = False

        print(
            "\n{:<12} {:<20} {:<12} {:<20} {:<12} {:<12}".format(
                "PROPERTY ID",
                "PROPERTY NAME",
                "TYPE",
                "ADDRESS",
                "RENT",
                "STATUS"
            )
        )

        print("-" * 95)

        for record in records:

            data = record.split("|")

            if data[5] == OCCUPIED:

                print(
                    "{:<12} {:<20} {:<12} {:<20} {:<12} {:<12}".format(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5]
                    )
                )

                found = True

        if not found:
            print("No occupied properties found.")