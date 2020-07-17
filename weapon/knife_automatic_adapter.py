from automatic import Automatic
from knife import Knife


class KnifeAutomaticAdapter(Knife):
    def __init__(self, automatic: Automatic):
        self.__automatic = automatic

    @property
    def armor_piercing(self):
        return self.__automatic.rate_fire

    @property
    def blade_length(self):
        return self.__automatic.caliber

    @property
    def material(self):
        return self.__automatic.range

    @property
    def name(self):
        return self.__automatic.name

    @property
    def price(self):
        return self.__automatic.price
