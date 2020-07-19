from __future__ import annotations
import copy
from abc import ABC, abstractmethod
from iter import Iter


class CompositeUnit(ABC):

    _children = []

    def __iter__(self):
        return Iter(self._children)

    def add(self, component: CompositeUnit):
        pass

    def remove(self, component: CompositeUnit):
        pass

    @property
    def units(self):
        return copy.copy(self._children)

    @abstractmethod
    def get_weapon_price(self):
        pass

    @abstractmethod
    def name(self):
        pass
