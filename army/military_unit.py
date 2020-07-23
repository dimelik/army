from typing import List
from composite_unit import CompositeUnit
from money import ZERO
from soldier import Soldier


class MilitaryUnit(CompositeUnit):

    def __init__(self, name):
        self._children: List[CompositeUnit] = []
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def is_dead(self):
        return False

    def add(self, component: CompositeUnit):
        if isinstance(component, Soldier):
            component.attach('kill', self.update)
        if isinstance(component, CompositeUnit):
            self._children.append(component)
        else:
            raise Exception('only CompositeUnit object is available to add')

    def remove(self, component: CompositeUnit):
        component.detach('kill', self.remove)
        if isinstance(component, CompositeUnit):
            self._children.remove(component)
        else:
            raise Exception('only CompositeUnit object is available to add')

    def update(self):
        for unit in self:
            if unit.is_dead is True:
                self.remove(unit)

    def get_weapon_price(self):
        result = ZERO
        for child in self._children:
            result = result.add(child.get_weapon_price())
        return result

    def get_soldier(self, name):
        for soldier in self._children:
            if soldier.name == name:
                return soldier
