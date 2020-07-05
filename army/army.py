from soldier import Soldier
from sorted_set import SortedSet
from bubble_sort import compare_object


class Army:

    def __init__(self, *soldier: Soldier):
        self.__set = SortedSet(compare_object)
        for soldier in soldier:
            self.__set.add(soldier)

    @property
    def soldiers(self):
        return self.__set.get_items

    def army_weapon_price(self):
        copy_soldiers = self.__set.get_items
        result = next(copy_soldiers).weapon_price()
        for soldier in copy_soldiers:
            result = result.add(soldier.weapon_price())
        return result
