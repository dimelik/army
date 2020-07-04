from weapon import Weapon


class GunshotWeapon(Weapon):
    __caliber = None
    __range = None

    @property
    def caliber(self):
        return self.__caliber

    @caliber.setter
    def caliber(self, value: float):
        self.__caliber = value

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value: int):
        self.__range = value
