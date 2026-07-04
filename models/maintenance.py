class Maintenance:
    def __init__(self, maintenance_id, tenant_id, description, status):
        self.maintenance_id = maintenance_id
        self.tenant_id = tenant_id
        self.description = description
        self.status = status

    def to_record(self):
        return (f"{self.maintenance_id}|" f"{self.tenant_id}|" f"{self.description}|" f"{self.status}")