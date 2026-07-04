class Complaint:
    def __init__(self,complaint_id, tenant_id, title, description, status):
        self.complaint_id = complaint_id
        self.tenant_id = tenant_id
        self.title = title
        self.description = description
        self.status = status

    def to_record(self):
        return (f"{self.complaint_id}|" f"{self.tenant_id}|" f"{self.title}|" f"{self.description}|" f"{self.status}")