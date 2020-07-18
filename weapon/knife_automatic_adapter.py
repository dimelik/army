from automatic import Automatic
from knife import Knife


class KnifeAutomaticAdapter(Knife):

    def __init__(self, automatic: Automatic):
        self.__automatic = automatic

    @property
    def armor_piercing(self):
        return None

    @property
    def blade_length(self):
        return None

    @property
    def material(self):
        return None

    @property
    def name(self):
        return self.__automatic.name

    @property
    def price(self):
        return self.__automatic.price
