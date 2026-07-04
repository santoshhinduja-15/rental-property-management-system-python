from services.auth_service import AuthService
from menus.admin_menu import AdminMenu
from menus.tenant_menu import TenantMenu
from utils.menu import Menu

class MainMenu:
    def start(self):
        while True:
            Menu.heading("RENTAL PROPERTY MANAGEMENT SYSTEM")
            print("1. Admin Login")
            print("2. Tenant Login")
            print("3. Exit")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":

                if AuthService.admin_login():
                    admin_menu = AdminMenu()
                    admin_menu.show()

            elif choice == "2":
                tenant_id = (AuthService.tenant_login())

                if tenant_id:
                    tenant_menu = TenantMenu(tenant_id)
                    tenant_menu.show()

            elif choice == "3":
                print("Thank You.")
                break

            else:
                print("Invalid choice.")