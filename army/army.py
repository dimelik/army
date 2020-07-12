from soldier import Soldier, compare_object
from map import Map


class Army:

    def __init__(self, *soldier: Soldier):
        self.__map = Map(compare_object)
        self.__soldiers_keys = []
        for soldier in soldier:
            self.__map.add(soldier.get_soldier_key(), soldier)
            self.__soldiers_keys.append(soldier.get_soldier_key())

    def get_soldiers(self):
        for soldier_key in self.__soldiers_keys:
            yield self.__map.get(soldier_key)

    def army_weapon_price(self):
        gen_soldiers = self.get_soldiers()
        result = next(gen_soldiers).get_weapon_price()
        for key in gen_soldiers:
            result = result.add(key.get_weapon_price())
        return result
