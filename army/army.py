from soldier import Soldier


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
        copy_soldiers = self.__soldiers.copy()
        result = copy_soldiers.pop().weapon_price
        for soldier in copy_soldiers:
            result = result.add(soldier.weapon_price)
        return result
