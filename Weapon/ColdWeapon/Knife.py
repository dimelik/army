from ColdWeapon import ColdWeapon


class Knife(ColdWeapon):
    _armorPiercing = None

    @property
    def armorPiercing(self):
        return self._armorPiercing

    @armorPiercing.setter
    def armorPiercing(self, value):
        self._armorPiercing = value

x = Knife(10000000, "sadasd")
print(x.price)