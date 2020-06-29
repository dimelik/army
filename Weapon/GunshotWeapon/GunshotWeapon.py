from .. import Weapon


class GunshotWeapon(Weapon):
    _caliber = None
    _range = None

    @property
    def caliber(self):
        return self._caliber

    @caliber.setter
    def caliber(self, value):
        self._caliber = value

    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, value):
        self._range = value
