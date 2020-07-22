from composite_unit import CompositeUnit
from soldier import compare_key
from map import Map
from meta_singleton import MetaSingleton
from iter import Iter
from money import ZERO
from observer_soldier import ObserverSoldier


def find_unit_in_companies(unit, name):
    for unit in unit:
        find_unit_in_companies(unit, name)
        if unit.name == name:
            return unit


class Army(ObserverSoldier):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self._instances[self]

    __map = Map(compare_key)

    def __iter__(self):
        return Iter(self.__map.get_items())

    def add(self, unit: CompositeUnit):
        self.__map.add(unit.name, unit)

    def get_units(self):
        return self.__map.get_items()

    def get_unit(self, name):
        for unit in self:
            if unit.name == name:
                return unit
            return find_unit_in_companies(unit, name)

    def remove(self, unit: CompositeUnit):
        self.__map.remove(unit.name)

    def army_weapon_price(self):
        result = ZERO
        for key in self:
            result = result.add(key.get_weapon_price())
        return result
