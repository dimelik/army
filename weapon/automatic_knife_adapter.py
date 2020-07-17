from automatic import Automatic
from knife import Knife


class AutomaticKnifeAdapter(Automatic):
    def __init__(self, knife: Knife):
        self.__knife = knife

    @property
    def rate_fire(self):
        return self.__knife.armor_piercing

    @property
    def caliber(self):
        return self.__knife.blade_length

    @property
    def range(self):
        return self.__knife.material

    @property
    def name(self):
        return self.__knife.name

    @property
    def price(self):
        return self.__knife.price
