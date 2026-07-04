from utils.menu import Menu
from services.tenant_service import TenantService
from services.rent_service import RentService
from services.payment_service import PaymentService
from services.complaint_service import ComplaintService
from services.maintenance_service import MaintenanceService
from services.exit_request_service import ExitRequestService


class TenantMenu:

    def __init__(self, tenant_id):
        self.tenant_id = tenant_id

    def show(self):

        while True:
            Menu.heading("TENANT MENU")

            print("1. View Assigned Property")
            print("2. View Rent Details")
            print("3. Send Payment Request")
            print("4. View Payment History")
            print("5. Raise Complaint")
            print("6. View Complaint Status")
            print("7. Raise Maintenance Request")
            print("8. View Maintenance Status")
            print("9. Create Exit Request")
            print("10. Logout")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":
                TenantService.view_assigned_property(self.tenant_id)

            elif choice == "2":
                RentService.view_tenant_rents(self.tenant_id)

            elif choice == "3":
                PaymentService.send_payment_request(self.tenant_id)

            elif choice == "4":
                PaymentService.view_tenant_payments(self.tenant_id)

            elif choice == "5":
                ComplaintService.raise_complaint(self.tenant_id)

            elif choice == "6":
                ComplaintService.view_tenant_complaints(self.tenant_id)

            elif choice == "7":
                MaintenanceService.raise_request(self.tenant_id)

            elif choice == "8":
                MaintenanceService.view_tenant_requests(self.tenant_id)

            elif choice == "9":
                ExitRequestService.create_exit_request(self.tenant_id)

            elif choice == "10":
                print("Logout successful.")
                break

            else:
                print("Invalid choice.")

            Menu.pause()