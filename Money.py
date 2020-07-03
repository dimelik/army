class Money:

    def __init__(self, currency='BYN'):
        self.__rate = 1
        self.currency(currency)

    def currency(self, currency):
        if currency == 'EUR':
            self.__rate = 2.76
        if currency == 'USD':
            self.__rate = 2.43
        if currency == 'BYN':
            self.__rate = 1

    def amount(self, value):
        return self.__rate * value
