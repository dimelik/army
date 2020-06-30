import sys
sys.path.append('../')
from Weapon import *


class ColdWeapon(Weapon):
    _bladeLength = None
    _material = None

    @property
    def bladeLength(self):
        return self._bladeLength

    @bladeLength.setter
    def bladeLength(self, value):
        self._bladeLength = float(value)

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = str(value)
