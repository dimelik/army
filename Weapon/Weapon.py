class Weapon:
    def __init__(self, price: float, name: str):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        self.__price = value
