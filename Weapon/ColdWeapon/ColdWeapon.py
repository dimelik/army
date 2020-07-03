import sys
sys.path.append('../')
from Weapon import *


class ColdWeapon(Weapon):
    __bladeLength = None
    __material = None

    @property
    def blade_length(self):
        return self.__bladeLength

    @blade_length.setter
    def blade_length(self, value: float):
        self.__bladeLength = value

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value: str):
        self.__material = value
