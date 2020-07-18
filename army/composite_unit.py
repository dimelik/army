from __future__ import annotations
from abc import ABC, abstractmethod


class CompositeUnit(ABC):

    _children = []

    def add(self, component: CompositeUnit):
        pass

    def remove(self, component: CompositeUnit):
        pass

    @property
    def units(self):
        return iter(self._children)

    @abstractmethod
    def get_weapon_price(self):
        pass

    @abstractmethod
    def name(self):
        pass
