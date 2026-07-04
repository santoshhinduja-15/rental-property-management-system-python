class Payment:
    def __init__(self, payment_id, rent_id, tenant_id, amount, request_date, status):
        self.payment_id = payment_id
        self.rent_id = rent_id
        self.tenant_id = tenant_id
        self.amount = amount
        self.request_date = request_date
        self.status = status

    def to_record(self):
        return (f"{self.payment_id}|" f"{self.rent_id}|" f"{self.tenant_id}|" f"{self.amount}|" f"{self.request_date}|" f"{self.status}")