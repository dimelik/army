from knife import Knife
from sapper_blade import SapperBlade
from automatic import Automatic
from pistol import Pistol
from money import Money


class Soldier:
    __knife = None
    __sapperBlade = None
    __automatic = None
    __pistol = None
    __weaponPrice = None

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def knife(self):
        return self.__knife

    @knife.setter
    def knife(self, value: Knife):
        self.__knife = value

    @property
    def sapper_blade(self):
        return self.__sapperBlade

    @sapper_blade.setter
    def sapper_blade(self, value: SapperBlade):
        self.__sapperBlade = value

    @property
    def automatic(self):
        return self.__automatic

    @automatic.setter
    def automatic(self, value: Automatic):
        self.__automatic = value

    @property
    def pistol(self):
        return self.__pistol

    @pistol.setter
    def pistol(self, value: Pistol):
        self.__pistol = value

    @property
    def weapon_price(self):
        result = self.__knife.price.add(self.__pistol.price).add(self.__automatic.price).add(self.__sapperBlade.price)
        return result
