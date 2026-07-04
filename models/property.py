class Property:
    def __init__(self, property_id, property_name, property_type, address,monthly_rent, status):
        self.property_id = property_id
        self.property_name = property_name
        self.property_type = property_type
        self.address = address
        self.monthly_rent = monthly_rent
        self.status = status

    def to_record(self):
        return (f"{self.property_id}|" f"{self.property_name}|" f"{self.property_type}|" f"{self.address}|" f"{self.monthly_rent}|" f"{self.status}" )