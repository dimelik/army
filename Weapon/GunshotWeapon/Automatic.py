from GunshotWeapon import GunshotWeapon


class Automatic(GunshotWeapon):
    __rateFire = None

    @property
    def rateFire(self):
        return self.__rateFire

    @rateFire.setter
    def rateFire(self, value):
        self.__rateFire = value



