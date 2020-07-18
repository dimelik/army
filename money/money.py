from currency import Currency


class Money:

    def __init__(self, amount: float, currency: Currency, other=None):
        if other == 1 or currency == 0:
            self.__amount = int(round(amount))
        else:
            self.__amount = int(round(amount * currency.convertation_factor))
        self.__currency = currency
        if currency != 0:
            self.__as_string = str(self.__amount / self.__currency.convertation_factor) + ' ' + self.__currency.currency
        else:
            self.__as_string = '0'

    def add(self, other):
        if isinstance(other, Money):
            if self.__currency == 0 or self.__currency.currency == other.currency.currency:
                return Money(self.amount + other.amount, other.__currency, other=1)
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


ZERO = Money(0, 0)
