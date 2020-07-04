from currency import Currency


class Money:

    def __init__(self, amount: int, currency: Currency):
        self.__amount = amount * currency.cents
        self.__currency = currency
        self.__as_string = str(self.__amount / self.__currency.cents) + ' ' + self.__currency.currency

    def add(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount, self.__currency)
        else:
            raise Exception("currency or class money not right")

    @property
    def currency(self):
        return self.__currency

    @property
    def amount(self):
        return self.__amount / self.__currency.cents

    @property
    def print_amount(self):
        return self.__as_string

