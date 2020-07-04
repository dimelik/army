from Soldier import Soldier
from Money import Money


class Army:
    __soldiers = []

    def __init__(self, *soldier: Soldier):
        for sold in soldier:
            if sold not in self.__soldiers:
                self.__soldiers.append(sold)

    @property
    def soldiers(self):
        return self.__soldiers

    @property
    def army_weapon_price(self):
        result = Money(0)
        for soldier in self.__soldiers:
            result.add(Money(soldier.weapon_price))
        return result
