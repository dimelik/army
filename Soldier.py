import sys
sys.path.append('Weapon/ColdWeapon/')
sys.path.append('Weapon/GunshotWeapon/')
from Knife import Knife
from SapperBlade import SapperBlade
from Automatic import Automatic
from Pistol import Pistol


class Soldier(object):
    __knife = None
    __sapperBlade = None
    __automatic = None
    __pistol = None
    __weaponPrice = 0

    @property
    def knife(self):
        return self.__knife

    @knife.setter
    def knife(self, value):
        if not isinstance(value, Knife):
            raise Exception("Not Knife in setter")
        self.__knife = value
        self.__weaponPrice += value.price

    @property
    def sapperBlade(self):
        return self.__sapperBlade

    @sapperBlade.setter
    def sapperBlade(self, value):
        if not isinstance(value, SapperBlade):
            raise Exception("Not sapperBlade in setter")
        self.__sapperBlade = value
        self.__weaponPrice += value.price

    @property
    def automatic(self):
        return self.__automatic

    @automatic.setter
    def automatic(self, value):
        if not isinstance(value, Automatic):
            raise Exception("Not automatic in setter")
        self.__automatic = value
        self.__weaponPrice += value.price

    @property
    def pistol(self):
        return self.__pistol

    @pistol.setter
    def pistol(self, value):
        if not isinstance(value, Pistol):
            raise Exception("Not automatic in setter")
        self.__pistol = value
        self.__weaponPrice += value.price

    @property
    def weaponPrice(self):
        return self.__weaponPrice

