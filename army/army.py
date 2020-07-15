from soldier import *
from map import Map
from meta_singleton import MetaSingleton


class Army(metaclass=MetaSingleton):
    __soldiers = []
    __map = Map(compare_key)

    def add_soldiers(self, *soldier: Soldier):
        for soldier in soldier:
            self.__soldiers.append(soldier)
            for soldier in self.__soldiers:
                if not isinstance(soldier, Soldier):
                    for soldier in soldier:
                        self.__map.add(soldier.get_soldier_key(), soldier)
                else:
                    self.__map.add(soldier.get_soldier_key(), soldier)

    def get_soldiers(self):
        return self.__map.get_items()

    def remove_soldier(self, soldier: Soldier):
        self.__map.remove(soldier.get_soldier_key())

    def army_weapon_price(self):
        gen_soldiers = self.get_soldiers()
        result = next(gen_soldiers).get_weapon_price()
        for key in gen_soldiers:
            result = result.add(key.get_weapon_price())
        return result
