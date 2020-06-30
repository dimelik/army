from . import ColdWeapon


class SaapperBlade(ColdWeapon):
    _handleLength = None

    @property
    def handleLength(self):
        return self._handleLength

    @handleLength.setter
    def handleLength(self, value):
        self._handleLength = value