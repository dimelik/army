class Money:

    __CENTS = 100
    __rate = 1

    def __init__(self, currency):
        self.currency(currency)

    def currency(self, currency):
        if currency == 'EUR':
            self.__rate = 2.76 * self.__CENTS
        if currency == 'USD':
            self.__rate = 2.43 * self.__CENTS
        if currency == 'BYN':
            self.__rate = 1 * self.__CENTS

    def amount(self, value):
        return (self.__rate * value) / self.__CENTS
