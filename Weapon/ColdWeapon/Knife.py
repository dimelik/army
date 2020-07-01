from ColdWeapon import ColdWeapon


class Knife(ColdWeapon):
    __armorPiercing = None

    @property
    def armorPiercing(self):
        return self.__armorPiercing

    @armorPiercing.setter
    def armorPiercing(self, value):
        self.__armorPiercing = value
