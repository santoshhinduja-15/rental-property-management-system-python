import re
from config.constants import (VACANT,OCCUPIED, PENDING, PAID, COMPLAINT_OPEN, COMPLAINT_IN_PROGRESS, COMPLAINT_RESOLVED, MAINTENANCE_PENDING, MAINTENANCE_IN_PROGRESS, MAINTENANCE_COMPLETED, EXIT_PENDING, EXIT_APPROVED)

class Validators:
    # PROPERTY VALIDATIONS
    @staticmethod
    def validate_property(property_id, property_name, address, monthly_rent, existing_property_ids):
        errors = []

        if not property_id.strip():
            errors.append("Property ID cannot be empty.")

        if property_id in existing_property_ids:
            errors.append("Property ID already exists.")

        if not property_name.strip():
            errors.append("Property name cannot be empty.")

        if not address.strip():
            errors.append("Address cannot be empty.")

        try:
            rent = float(monthly_rent)

            if rent <= 0:
                errors.append("Monthly rent must be greater than zero.")

        except ValueError:
            errors.append("Monthly rent must be numeric.")

        return errors

    # TENANT VALIDATIONS
    @staticmethod
    def validate_tenant(tenant_id, name, phone, email, username, existing_tenant_ids, existing_usernames):
        errors = []

        if not tenant_id.strip():
            errors.append("Tenant ID cannot be empty.")

        if tenant_id in existing_tenant_ids:
            errors.append("Tenant ID already exists.")

        if not name.strip():
            errors.append("Tenant name cannot be empty.")

        if not phone.strip():
            errors.append("Phone number cannot be empty.")
        
        else:
            if not phone.isdigit():
                errors.append("Phone number must contain only digits.")

            if len(phone) != 10:
                errors.append("Phone number must be exactly 10 digits.")

            if phone and phone[0] not in "6789":
                errors.append("Phone number must start with 6, 7, 8 or 9.")

            if len(phone) == 10 and len(set(phone)) == 1:
                errors.append("Phone number cannot contain the same digit repeated 10 times.")

        if not email.strip():
            errors.append("Email cannot be empty.")
        
        else:
            email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
            
            if not re.match(email_pattern, email):
                errors.append("Enter a valid email address.")

        if not username.strip():
            errors.append("Username cannot be empty.")

        if username in existing_usernames:
            errors.append("Username already exists.")

        return errors

    # ALLOCATION VALIDATIONS
    @staticmethod
    def validate_allocation(property_exists, tenant_exists, property_status, already_allocated):
        errors = []

        if not property_exists:
            errors.append("Property does not exist.")

        if not tenant_exists:
            errors.append("Tenant does not exist.")

        if property_exists and property_status != VACANT:
            errors.append("Only vacant properties can be allocated.")

        if already_allocated:
            errors.append("Property is already allocated.")

        return errors

    # RENT VALIDATIONS
    @staticmethod
    def validate_rent(amount, duplicate_month):
        errors = []

        try:
            amount = float(amount)

            if amount <= 0:
                errors.append("Rent amount must be greater than zero.")

        except ValueError:
            errors.append("Rent amount must be numeric.")

        if duplicate_month:
            errors.append("Rent for this month already exists for this tenant.")

        return errors

    # PAYMENT VALIDATIONS
    @staticmethod
    def validate_payment(
        rent_exists,
        rent_status
    ):

        errors = []

        if not rent_exists:
            errors.append("Rent record does not exist.")

        if rent_exists and rent_status == PAID:
            errors.append("This rent has already been paid.")

        return errors

    # COMPLAINT VALIDATIONS
    @staticmethod
    def validate_complaint(title, description):
        errors = []

        if not title.strip():
            errors.append("Complaint title cannot be empty.")

        if not description.strip():
            errors.append("Complaint description cannot be empty.")

        return errors

    # MAINTENANCE VALIDATIONS
    @staticmethod
    def validate_maintenance(description):
        errors = []

        if not description.strip():
            errors.append("Maintenance description cannot be empty.")

        return errors

    # EXIT REQUEST VALIDATIONS
    @staticmethod
    def validate_exit_request(active_property, pending_request_exists):
        errors = []

        if not active_property:
            errors.append("Tenant does not have any active property allocation.")

        if pending_request_exists:
            errors.append("A pending exit request already exists.")

        return errors

    # COMPLAINT TRANSITIONS
    @staticmethod
    def validate_complaint_status_transition(current_status, new_status):
        errors = []

        valid_transitions = {
            COMPLAINT_OPEN: [COMPLAINT_IN_PROGRESS],
            COMPLAINT_IN_PROGRESS: [COMPLAINT_RESOLVED],
            COMPLAINT_RESOLVED: []
        }

        if new_status not in valid_transitions.get(current_status, []):
            errors.append(
                f"Complaint status cannot be changed from "
                f"{current_status} to {new_status}."
            )

        return errors

    # MAINTENANCE TRANSITIONS
    @staticmethod
    def validate_maintenance_status_transition(current_status, new_status):
        errors = []

        valid_transitions = {
            MAINTENANCE_PENDING: [MAINTENANCE_IN_PROGRESS],
            MAINTENANCE_IN_PROGRESS: [MAINTENANCE_COMPLETED],
            MAINTENANCE_COMPLETED: []
        }

        if new_status not in valid_transitions.get(current_status, []):
            errors.append(
                f"Maintenance status cannot be changed from "
                f"{current_status} to {new_status}."
            )

        return errors

    # STATUS VALUE VALIDATIONS
    @staticmethod
    def validate_property_status(status):
        return status in [VACANT, OCCUPIED]

    @staticmethod
    def validate_rent_status(status):
        return status in [PENDING, PAID]

    @staticmethod
    def validate_complaint_status(status):
        return status in [
            COMPLAINT_OPEN,
            COMPLAINT_IN_PROGRESS,
            COMPLAINT_RESOLVED
        ]

    @staticmethod
    def validate_maintenance_status(status):
        return status in [
            MAINTENANCE_PENDING,
            MAINTENANCE_IN_PROGRESS,
            MAINTENANCE_COMPLETED
        ]

    @staticmethod
    def validate_exit_status(status):
        return status in [
            EXIT_PENDING,
            EXIT_APPROVED
        ]