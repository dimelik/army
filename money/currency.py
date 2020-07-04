class Currency:
    __cents = 0

    def __init__(self, currency):
        self.__currency = currency
        if currency == 'USD':
            self.__cents = 10
        elif currency == 'OLD_BYR':
            self.__cents = 1000
        else:
            raise Exception("sorry, only USD/OLD_BYR")

    @property
    def currency(self):
        return self.__currency

    @property
    def cents(self):
        return self.__cents


USD = Currency('USD')
OLD_BYR = Currency('OLD_BYR')