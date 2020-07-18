from typing import List
from composite_unit import CompositeUnit


class MilitaryUnit(CompositeUnit):

    def __init__(self, name):
        self._children: List[CompositeUnit] = []
        self.__name = name

    def is_composite(self):
        return True

    @property
    def units(self):
        return self._children

    @property
    def name(self):
        return self.__name

    def add(self, component: CompositeUnit):
        self._children.append(component)

    def remove(self, component: CompositeUnit):
        self._children.remove(component)

    def get_weapon_price(self):
        result = self._children[0].get_weapon_price()
        for child in self._children:
            if child is self._children[0]:
                continue
            result = result.add(child.get_weapon_price())
        return result

