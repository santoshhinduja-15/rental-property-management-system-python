from utils.menu import Menu

from services.property_service import PropertyService
from services.tenant_service import TenantService
from services.allocation_service import AllocationService
from services.rent_service import RentService
from services.payment_service import PaymentService
from services.complaint_service import ComplaintService
from services.maintenance_service import MaintenanceService
from services.exit_request_service import ExitRequestService
from services.report_service import ReportService


class AdminMenu:

    def show(self):

        while True:

            Menu.heading("ADMIN MENU")

            print("1. Add Property")
            print("2. View Properties")
            print("3. Update Property")
            print("4. Delete Property")

            print("5. Add Tenant")
            print("6. View Tenants")
            print("7. Update Tenant")
            print("8. Remove Tenant")

            print("9. Allocate Property")
            print("10. View Allocations")

            print("11. Generate Rent")
            print("12. View Rents")
            print("13. View Pending Rents")

            print("14. Approve Payment")
            print("15. View Payment History")

            print("16. View Complaints")
            print("17. Update Complaint Status")

            print("18. View Maintenance Requests")
            print("19. Update Maintenance Status")

            print("20. View Exit Requests")
            print("21. Approve Exit Request")

            print("22. Property Report")
            print("23. Tenant Report")
            print("24. Rent Report")
            print("25. Income Report")

            print("26. Logout")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":
                PropertyService.add_property()

            elif choice == "2":
                PropertyService.view_properties()

            elif choice == "3":
                PropertyService.update_property()

            elif choice == "4":
                PropertyService.delete_property()

            elif choice == "5":
                TenantService.add_tenant()

            elif choice == "6":
                TenantService.view_tenants()

            elif choice == "7":
                TenantService.update_tenant()

            elif choice == "8":
                TenantService.remove_tenant()

            elif choice == "9":
                AllocationService.allocate_property()

            elif choice == "10":
                AllocationService.view_allocations()

            elif choice == "11":
                RentService.generate_rent()

            elif choice == "12":
                RentService.view_rents()

            elif choice == "13":
                RentService.view_pending_rents()

            elif choice == "14":
                PaymentService.approve_payment()

            elif choice == "15":
                PaymentService.view_payment_history()

            elif choice == "16":
                ComplaintService.view_complaints()

            elif choice == "17":
                ComplaintService.update_complaint_status()

            elif choice == "18":
                MaintenanceService.view_requests()

            elif choice == "19":
                MaintenanceService.update_request_status()

            elif choice == "20":
                ExitRequestService.view_exit_requests()

            elif choice == "21":
                ExitRequestService.approve_exit_request()

            elif choice == "22":
                ReportService.property_report()

            elif choice == "23":
                ReportService.tenant_report()

            elif choice == "24":
                ReportService.rent_report()

            elif choice == "25":
                ReportService.income_report()

            elif choice == "26":
                print("Logout successful.")
                break

            else:
                print("Invalid choice.")

            Menu.pause()