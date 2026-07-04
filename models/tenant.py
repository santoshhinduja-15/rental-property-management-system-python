class Tenant:
    def __init__(self, tenant_id, name, phone, email, username, password_hash):
        self.tenant_id = tenant_id
        self.name = name
        self.phone = phone
        self.email = email
        self.username = username
        self.password_hash = password_hash

    def to_record(self):
        return (f"{self.tenant_id}|" f"{self.name}|" f"{self.phone}|" f"{self.email}|" f"{self.username}|" f"{self.password_hash}")