from soldier import Soldier, compare_object
from sorted_set import SortedSet
from map import Map


class Army:

    def __init__(self, *soldier: Soldier):
        self.__map = Map()
        self.__soldiers_keys = []
        for soldier in soldier:
            self.__map.add(soldier.get_soldier_key(), soldier)
            self.__soldiers_keys.append(soldier.get_soldier_key())

    @property
    def soldiers(self):
        return self.__map.get_items

    def army_weapon_price(self):
        copy_soldiers = self.__map.get_items
        result = next(copy_soldiers).get_weapon_price()
        for soldier in copy_soldiers:
            result = result.add(soldier.get_weapon_price())
        return result
