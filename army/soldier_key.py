class SoldierKey:
    def __init__(self, military_unit_number, name):
        self.__military_unit_number = str(military_unit_number)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def military_unit_number(self):
        return self.__military_unit_number
