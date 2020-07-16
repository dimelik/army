from abc import ABC, abstractmethod
from currency import *


class WeaponFactory(ABC):

    def __init__(self, currency: Currency):
        self._currency = currency

    @abstractmethod
    def create_pistol(self):
        pass

    @abstractmethod
    def create_knife(self):
        pass

    @abstractmethod
    def create_sapper(self):
        pass

    @abstractmethod
    def create_automatic(self):
        pass
