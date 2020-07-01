import sys
sys.path.append('../')
from Weapon import *


class GunshotWeapon(Weapon):
    __caliber = None
    __range = None

    @property
    def caliber(self):
        return self.__caliber

    @caliber.setter
    def caliber(self, value):
        self.__caliber = value

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value):
        self.__range = value
