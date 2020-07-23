from composite_unit import CompositeUnit
from soldier import compare_key
from map import Map
from meta_singleton import MetaSingleton
from iter import Iter
from money import ZERO
from soldier import Soldier


def find_unit_in_companies(unit, name):
    for unit in unit:
        find_unit_in_companies(unit, name)
        if unit.name == name:
            return unit


class Army:
    _instances = {}

    @classmethod
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    __map = Map(compare_key)

    def __iter__(self):
        return Iter(self.__map.get_items())

    def add(self, unit: CompositeUnit):
        if isinstance(unit, Soldier):
            unit.attach('kill', self.update)
        self.__map.add(unit.name, unit)

    def get_units(self):
        return self.__map.get_items()

    def get_unit(self, name):
        for unit in self:
            if unit.name == name:
                return unit
            return find_unit_in_companies(unit, name)

    def remove(self, unit: CompositeUnit):
        unit.detach('kill', self.remove)
        self.__map.remove(unit.name)

    def update(self):
        for unit in self:
            if unit.is_dead is True:
                self.remove(unit)

    def army_weapon_price(self):
        result = ZERO
        for key in self:
            result = result.add(key.get_weapon_price())
        return result
