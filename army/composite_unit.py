from __future__ import annotations
from abc import ABC, abstractmethod


class CompositeUnit(ABC):

    def add(self, component: CompositeUnit):
        pass

    def remove(self, component: CompositeUnit):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def get_weapon_price(self):
        pass
