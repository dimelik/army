from abc import ABC, abstractmethod
from soldier import Soldier


class Sergeant(ABC):

    def __init__(self, military_unit_number, name):
        self.__soldier = self.create_sergeant(military_unit_number, name)

    @abstractmethod
    def add_weapon_sergeant(self):
        pass

    def create_sergeant(self, military_unit_number, name):
        return Soldier(military_unit_number, name).clone()

    @property
    def soldier(self):
        return self.__soldier
