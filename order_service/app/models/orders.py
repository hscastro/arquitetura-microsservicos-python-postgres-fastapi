
class Order:
    def __init__(self, id, user_id, status, total_price, created_at):
        self.id = id
        self.user_id = user_id
        self.status = status
        self.total_price = total_price
        self.created_at = created_at
