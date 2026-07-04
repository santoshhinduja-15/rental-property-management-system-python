class Allocation:
    def __init__(self,allocation_id, property_id, tenant_id, allocation_date):
        self.allocation_id = allocation_id
        self.property_id = property_id
        self.tenant_id = tenant_id
        self.allocation_date = allocation_date

    def to_record(self):
        return (f"{self.allocation_id}|" f"{self.property_id}|" f"{self. tenant_id}|" f"{self.allocation_date}")