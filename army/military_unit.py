from typing import List
from composite_unit import CompositeUnit


class MilitaryUnit(CompositeUnit):

    def __init__(self):
        self._children: List[CompositeUnit] = []

    def add(self, component: CompositeUnit):
        self._children.append(component)

    def remove(self, component: CompositeUnit):
        self._children.remove(component)

    def is_composite(self):
        return True

    def get_weapon_price(self) -> list:
        array = []
        for child in self._children:
            array.append(child.get_weapon_price())
        result = array.pop()
        for key in array:
            result = result.add(key)
        return result

