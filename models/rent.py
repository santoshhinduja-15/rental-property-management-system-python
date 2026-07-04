class Rent:
    def __init__(self, rent_id, tenant_id, property_id, month, amount, status):
        self.rent_id = rent_id
        self.tenant_id = tenant_id
        self.property_id = property_id
        self.month = month
        self.amount = amount
        self.status = status

    def to_record(self):
        return (f"{self.rent_id}|" f"{self.tenant_id}|" f"{self.property_id}|" f"{self.month}|" f"{self.amount}|" f"{self.status}")