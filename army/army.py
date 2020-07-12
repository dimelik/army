from soldier import *
from map import Map


class Army:

    def __init__(self, *soldier: Soldier):
        self.__map = Map(compare_key)
        for soldier in soldier:
            self.__map.add(soldier.get_soldier_key(), soldier)

    def get_soldiers(self):
        return self.__map.get_items()

    def army_weapon_price(self):
        gen_soldiers = self.get_soldiers()
        result = next(gen_soldiers).get_weapon_price()
        for key in gen_soldiers:
            result = result.add(key.get_weapon_price())
        return result
