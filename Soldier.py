from Weapon.Weapon import *


class Soldier(object):
    _weapons = []
    _weaponPrice = 0

    @property
    def weapons(self):
        return self._weapons

    @weapons.setter
    def weapons(self, weapon):
        if not isinstance(weapon, Weapon):
            raise Exception("Not Knife in setter")
        self._weapons.append(weapon)
        self._weaponPrice += weapon.price

    @property
    def weaponPrice(self):
        return self._weaponPrice


x = Weapon(100000000000, "as")
sold = Soldier()
sold.weapons = x
sold.weapons = x
print(sold.weaponPrice)

