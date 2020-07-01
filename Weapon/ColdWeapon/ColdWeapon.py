import sys
sys.path.append('../')
from Weapon import *


class ColdWeapon(Weapon):
    __bladeLength = None
    __material = None

    @property
    def bladeLength(self):
        return self.__bladeLength

    @bladeLength.setter
    def bladeLength(self, value):
        self.__bladeLength = value

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value):
        self.__material = value
