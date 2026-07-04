class ExitRequest:
    def __init__(self, exit_id, tenant_id, request_date, status):
        self.exit_id = exit_id
        self.tenant_id = tenant_id
        self.request_date = request_date
        self.status = status

    def to_record(self):
        return (f"{self.exit_id}|" f"{self.tenant_id}|" f"{self.request_date}|" f"{self.status}")