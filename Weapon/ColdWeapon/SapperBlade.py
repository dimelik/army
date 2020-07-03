from ColdWeapon import ColdWeapon


class SapperBlade(ColdWeapon):
    __handleLength = None

    @property
    def handle_length(self):
        return self.__handleLength

    @handle_length.setter
    def handle_length(self, value: int):
        self.__handleLength = value
