from Money import Money


class Weapon:
    def __init__(self, price: Money, name: str):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price.amount

    @price.setter
    def price(self, value: Money):
        self.__price = value
