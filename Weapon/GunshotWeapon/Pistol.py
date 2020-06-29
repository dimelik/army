from .. import Weapon


class Pistol(Weapon):
    _armorPiercing = None

    @property
    def armorPiercing(self):
        return self._rateFire

    @armorPiercing.setter
    def armorPiercing(self, value):
        self._armorPiercing = float(value)
