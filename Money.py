class Money:

    def __init__(self, amount: int, currency='USD'):
        self.__amount = amount
        self.__currency = currency

    def add(self, other):
        print(type(self.amount))
        print(type(other.amount))
        # if isinstance(other, Money):
        #     if self.__currency == other.__currency:
        #         return Money(self.amount + other.amount)
        # else:
        #     raise Exception("currency or class Money not right")

    @property
    def amount(self):
        return self.__amount

    def amount_print(self):
        return str(self.__amount) + ' ' + self.__currency