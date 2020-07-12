from abc import ABC, abstractmethod
from money import Money
from soldier import Soldier


class Capral(ABC):

    def __init__(self, military_unit_number, name):
        self.__soldier = Soldier(military_unit_number, name)

    @abstractmethod
    def create_knife(self, price: Money, name: str):
        pass

    @abstractmethod
    def create_sapper_blade(self, price: Money, name: str):
        pass

    @abstractmethod
    def create_pistol(self, price: Money, name: str):
        pass

    @abstractmethod
    def create_automatic(self, price: Money, name: str):
        pass
