from weapon import Weapon


class Bug:

    def __init__(self):
        self.__weapons = []

    @property
    def weapon(self):
        return self.__weapons.pop()

    @weapon.setter
    def weapon(self, value: Weapon):
        self.__weapons.append(value)

    @property
    def next_weapon(self):
        return self.__weapons[list.count(self.__weapons)]

    @property
    def weapons(self):
        return self.__weapons
