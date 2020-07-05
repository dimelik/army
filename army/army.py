from soldier import Soldier
from bubble_sort import bubble_sorted_set

class Army:

    def __init__(self, *soldier: Soldier):
        self.__soldiers = bubble_sorted_set(soldier)

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
