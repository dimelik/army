class Currency:

    def __init__(self, currency, convertation_factor):
        self.__currency = currency
        self.__convertation_factor = convertation_factor


    @property
    def currency(self):
        return self.__currency

    @property
    def cents(self):
        return self.__convertation_factor


USD = Currency('USD', 100)
OLD_BYR = Currency('OLD_BYR', 1)
