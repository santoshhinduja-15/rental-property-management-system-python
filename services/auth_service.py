import hashlib

from config.constants import (ADMIN_USERNAME, ADMIN_PASSWORD, TENANTS_FILE)
from utils.file_handler import FileHandler

class AuthService:
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def admin_login():
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        if (username == ADMIN_USERNAME and password == ADMIN_PASSWORD):
            print("Login successful.")
            return True

        print("Invalid username or password.")
        return False

    @staticmethod
    def tenant_login():
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        password_hash = AuthService.hash_password(password)
        records = FileHandler.read_records(TENANTS_FILE)

        for record in records:
            data = record.split("|")

            if len(data) < 6:
                continue

            tenant_id = data[0]
            stored_username = data[4]
            stored_password_hash = data[5]

            if (username == stored_username and password_hash == stored_password_hash):
                print("Login successful.")
                return tenant_id

        print("Invalid username or password.")
        return None