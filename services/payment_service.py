from datetime import datetime

from config.constants import (
    PAYMENTS_FILE,
    RENTS_FILE,
    PAYMENT_PREFIX,
    PENDING,
    PAID,
    TENANTS_FILE
)

from models.payment import Payment

from utils.file_handler import FileHandler
from utils.id_generator import IdGenerator


class PaymentService:

    REQUESTED = "Requested"
    APPROVED = "Approved"

    @staticmethod
    def send_payment_request(tenant_id):

        rent_id = input(
            "Enter Rent ID: "
        ).strip()

        rent_records = FileHandler.read_records(
            RENTS_FILE
        )

        rent_found = False
        rent_amount = None
        rent_status = None

        for record in rent_records:

            data = record.split("|")

            if (
                data[0] == rent_id
                and
                data[1] == tenant_id
            ):
                rent_found = True
                rent_amount = data[4]
                rent_status = data[5]
                break

        errors = []

        if not rent_found:
            errors.append(
                "Rent record not found."
            )

        if (
            rent_found
            and
            rent_status == PAID
        ):
            errors.append(
                "This rent has already been paid."
            )

        payment_records = FileHandler.read_records(
            PAYMENTS_FILE
        )

        for record in payment_records:

            data = record.split("|")

            if (
                data[1] == rent_id
                and
                data[5] == PaymentService.REQUESTED
            ):
                errors.append(
                    "Payment request already exists for this rent."
                )
                break

        if errors:

            for error in errors:
                print(error)

            return

        payment_id = IdGenerator.generate_id(
            PAYMENTS_FILE,
            PAYMENT_PREFIX
        )

        request_date = datetime.now().strftime(
            "%d-%m-%Y"
        )

        payment = Payment(
            payment_id,
            rent_id,
            tenant_id,
            rent_amount,
            request_date,
            PaymentService.REQUESTED
        )

        FileHandler.write_record(
            PAYMENTS_FILE,
            payment.to_record()
        )

        print(
            f"Payment request submitted successfully. Payment ID: {payment_id}"
        )

    @staticmethod
    def approve_payment():

        payment_id = input(
            "Enter Payment ID: "
        ).strip()

        payment_records = FileHandler.read_records(
            PAYMENTS_FILE
        )

        payment_found = False
        rent_id = None

        updated_payments = []

        for record in payment_records:

            data = record.split("|")

            if data[0] == payment_id:

                payment_found = True

                if (
                    data[5]
                    == PaymentService.APPROVED
                ):
                    print(
                        "Payment already approved."
                    )
                    return

                rent_id = data[1]

                data[5] = (
                    PaymentService.APPROVED
                )

            updated_payments.append(
                "|".join(data)
            )

        if not payment_found:

            print(
                "Payment request not found."
            )

            return

        FileHandler.overwrite_records(
            PAYMENTS_FILE,
            updated_payments
        )

        rent_records = FileHandler.read_records(
            RENTS_FILE
        )

        updated_rents = []

        for record in rent_records:

            data = record.split("|")

            if data[0] == rent_id:
                data[5] = PAID

            updated_rents.append(
                "|".join(data)
            )

        FileHandler.overwrite_records(
            RENTS_FILE,
            updated_rents
        )

        print(
            "Payment approved successfully."
        )

    @staticmethod
    def view_payment_history():

        payment_records = FileHandler.read_records(
            PAYMENTS_FILE
        )

        if not payment_records:

            print(
                "No payment records found."
            )

            return

        tenant_map = {}

        tenant_records = FileHandler.read_records(
            TENANTS_FILE
        )

        for record in tenant_records:

            data = record.split("|")

            tenant_map[data[0]] = data[1]

        rent_map = {}

        rent_records = FileHandler.read_records(
            RENTS_FILE
        )

        for record in rent_records:

            data = record.split("|")

            rent_map[data[0]] = data[3]

        print(
            "\n{:<10} {:<20} {:<15} {:<10} {:<15} {:<12}".format(
                "PAY ID",
                "TENANT",
                "MONTH",
                "AMOUNT",
                "DATE",
                "STATUS"
            )
        )

        print("-" * 90)

        for record in payment_records:

            data = record.split("|")

            print(
                "{:<10} {:<20} {:<15} {:<10} {:<15} {:<12}".format(
                    data[0],
                    tenant_map.get(
                        data[2],
                        "N/A"
                    ),
                    rent_map.get(
                        data[1],
                        "N/A"
                    ),
                    data[3],
                    data[4],
                    data[5]
                )
            )

    @staticmethod
    def view_tenant_payments(
        tenant_id
    ):

        payment_records = FileHandler.read_records(
            PAYMENTS_FILE
        )

        rent_records = FileHandler.read_records(
            RENTS_FILE
        )

        rent_map = {}

        for record in rent_records:

            data = record.split("|")

            rent_map[data[0]] = data[3]

        found = False

        print(
            "\n{:<10} {:<15} {:<10} {:<15} {:<12}".format(
                "PAY ID",
                "MONTH",
                "AMOUNT",
                "DATE",
                "STATUS"
            )
        )

        print("-" * 70)

        for record in payment_records:

            data = record.split("|")

            if data[2] == tenant_id:

                print(
                    "{:<10} {:<15} {:<10} {:<15} {:<12}".format(
                        data[0],
                        rent_map.get(
                            data[1],
                            "N/A"
                        ),
                        data[3],
                        data[4],
                        data[5]
                    )
                )

                found = True

        if not found:
            print(
                "No payment records found."
            )