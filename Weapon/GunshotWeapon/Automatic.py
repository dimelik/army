from GunshotWeapon import GunshotWeapon


class Automatic(GunshotWeapon):
    __rateFire = None

    @property
    def rate_fire(self):
        return self.__rateFire

    @rate_fire.setter
    def rate_fire(self, value: int):
        self.__rateFire = value



