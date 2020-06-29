from . import GunshotWeapon


class Automatic(GunshotWeapon):
    _rateFire = None

    @property
    def rateFire(self):
        return self._rateFire

    @rateFire.setter
    def rateFire(self, value):
        self._rateFire = float(value)
