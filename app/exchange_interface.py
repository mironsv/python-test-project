class ExchangeInterface:
    def __init__(self, name):
        self.name = name

    def send_order(self, amount):
        return amount
