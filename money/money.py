from currency import Currency


class Money:

    def __init__(self, amount: float, currency: Currency, other=None):
        if other == 1:
            self.__amount = int(round(amount))
        else:
            self.__amount = int(round(amount * currency.convertation_factor))
        self.__currency = currency
        self.__as_string = str(self.__amount / self.__currency.convertation_factor) + ' ' + self.__currency.currency

    def add(self, other):
        if isinstance(other, Money):
            if self.__currency.currency == other.currency.currency:
                return Money(self.amount + other.amount, self.__currency, other=1)
        else:
            raise Exception("currency or class money not right")

    @property
    def currency(self):
        return self.__currency

    @property
    def amount(self):
        return self.__amount

    @property
    def print_amount(self):
        return self.__as_string

