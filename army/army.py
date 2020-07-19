from composite_unit import CompositeUnit
from soldier import compare_key
from map import Map
from meta_singleton import MetaSingleton
from iter import Iter
from money import ZERO


class Army(metaclass=MetaSingleton):
    __map = Map(compare_key)

    def __iter__(self):
        return Iter(self.__map.get_items())

    def add_soldiers(self, unit: CompositeUnit):
        self.__map.add(unit.name, unit)

    def get_soldiers(self):
        return self.__map.get_items()

    def remove_soldier(self, unit: CompositeUnit):
        self.__map.remove(unit.name)

    def army_weapon_price(self):
        result = ZERO
        for key in self:
            result = result.add(key.get_weapon_price())
        return result
