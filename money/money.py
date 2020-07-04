from currency import Currency


class Money:

    def __init__(self, amount: float, currency: Currency):
        self.__amount = int(amount * currency.convertation_factor)
        self.__currency = currency
        self.__as_string = str(self.__amount / self.__currency.convertation_factor) + ' ' + self.__currency.currency

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
        return self.__amount

    @property
    def print_amount(self):
        return self.__as_string

