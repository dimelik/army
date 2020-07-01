import sys
sys.path.append('Weapon/ColdWeapon/')
sys.path.append('Weapon/GunshotWeapon/')
from Knife import Knife
from SapperBlade import SapperBlade
from Automatic import Automatic
from Pistol import Pistol


class Soldier(object):
    __knife = Knife(0, '')
    __sapperBlade = SapperBlade(0, '')
    __automatic = Automatic(0, '')
    __pistol = Pistol(0, '')
    __weaponPrice = 0

    @property
    def knife(self):
        return self.__knife

    @knife.setter
    def knife(self, value):
        if not isinstance(value, Knife):
            raise Exception("Not Knife in setter")
        self.__knife = value

    @property
    def sapperBlade(self):
        return self.__sapperBlade

    @sapperBlade.setter
    def sapperBlade(self, value):
        if not isinstance(value, SapperBlade):
            raise Exception("Not sapperBlade in setter")
        self.__sapperBlade = value

    @property
    def automatic(self):
        return self.__automatic

    @automatic.setter
    def automatic(self, value):
        if not isinstance(value, Automatic):
            raise Exception("Not automatic in setter")
        self.__automatic = value

    @property
    def pistol(self):
        return self.__pistol

    @pistol.setter
    def pistol(self, value):
        if not isinstance(value, Pistol):
            raise Exception("Not automatic in setter")
        self.__pistol = value

    @property
    def weaponPrice(self):
        return self.__knife.price + self.__pistol.price + self.__automatic.price + self.__sapperBlade.price

