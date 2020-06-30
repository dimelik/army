class Weapon(object):
    def __init__(self, price=100, name='asd'):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
