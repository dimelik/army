from ColdWeapon import ColdWeapon


class Knife(ColdWeapon):
    __armorPiercing = None

    @property
    def armor_piercing(self):
        return self.__armorPiercing

    @armor_piercing.setter
    def armor_piercing(self, value: int):
        self.__armorPiercing = value
