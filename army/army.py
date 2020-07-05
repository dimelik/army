from soldier import Soldier
from bubble_sorted_set import BubbleSortedSet


class Army:

    def __init__(self, *soldier: Soldier):
        self.__set = BubbleSortedSet()
        for soldier in soldier:
            self.__set.add(soldier)

    @property
    def soldiers(self):
        return self.__set.get_items

    @property
    def army_weapon_price(self):
        copy_soldiers = self.__set.get_items.copy()
        result = copy_soldiers.pop().weapon_price
        for soldier in copy_soldiers:
            result = result.add(soldier.weapon_price)
        return result
