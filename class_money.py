class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divider):
        return Money(self.amount / divider, self.currency)

    def __add__(self, other):
        return Money(self.amount +other.amount, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency ==self.currency

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

        


class Wallet:
    def __init__(self):
        self.moneys = []
        self.amount = 0

    def add(self, *moneys):
        for money in moneys:
            self.moneys.append(money)
            self.amount += money.amount

    def evaluate(self, currency):
        money_sum = 0
        for money in self.moneys:
            money_sum += money.amount
        return money_sum