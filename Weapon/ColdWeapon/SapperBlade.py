from ColdWeapon import ColdWeapon


class SapperBlade(ColdWeapon):
    __handleLength = None

    @property
    def handleLength(self):
        return self.__handleLength

    @handleLength.setter
    def handleLength(self, value):
        self.__handleLength = value
