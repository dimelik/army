from soldier import Soldier, compare_object
from map import Map


class Army:

    def __init__(self, *soldier: Soldier):
        self.__map = Map()
        self.__soldiers_keys = []
        for soldier in soldier:
            self.__map.add(soldier.get_soldier_key(), soldier)
            self.__soldiers_keys.append(soldier.get_soldier_key())

    def get_soldiers(self):
        result = []
        for soldier_key in self.__soldiers_keys:
            result.append(self.__map.get(soldier_key))
        return result

    def army_weapon_price(self):
        result = self.get_soldiers()[0].get_weapon_price()
        for key in self.get_soldiers():
            if key != self.get_soldiers()[0]:
                result = result.add(key.get_weapon_price())
        return result
