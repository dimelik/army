from GunshotWeapon import GunshotWeapon


class Pistol(GunshotWeapon):
    __armorPiercing = None

    @property
    def armorPiercing(self):
        return self.__rateFire

    @armorPiercing.setter
    def armorPiercing(self, value):
        self.__armorPiercing = value
