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

    def __repr__(self):
        return f"<{self.currency} {self.amount}>"

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

        


class Wallet:
    def __init__(self):
        self.moneys = []
        self.exchange_rate = {'USD->KRW': 1100, 'EUR->USD': 1.2}

    def add(self, *moneys):
        for money in moneys:
            self.moneys.append(money)

    def evaluate(self, currency):
        money_sum = 0
        for money in self.moneys:
            if currency == money.currency:        
                money_sum += money.amount
            else:
                exchange_key = f"{money.currency}->{currency}"
                exchange_rate = self.exchange_rate[exchange_key]
                money_sum += money.amount * exchange_rate
        return Money(money_sum, currency)