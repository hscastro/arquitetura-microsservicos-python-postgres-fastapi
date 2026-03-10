
class Payment:
    def __init__(self, id, order_id, amount, status, provider, created_at):
        self.id = id
        self.order_id = order_id
        self.amount = amount
        self.status = status
        self.provider = provider
        self.created_at = created_at