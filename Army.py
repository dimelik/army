class Army(object):
    __soldiers = []
    __weaponPrice = 0

    def __init__(self, *soldier):
        for sold in soldier:
            self.__soldiers.append(sold)

    @property
    def soldiers(self):
        return self.__soldiers

    @property
    def armyWeaponPrice(self):
        if self.__weaponPrice != 0:
            self.__weaponPrice = 0
        for soldier in self.__soldiers:
            self.__weaponPrice += soldier.weaponPrice
        return self.__weaponPrice
