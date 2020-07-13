from soldier import Soldier
from knife import Knife
from sapper_blade import SapperBlade
from automatic import Automatic
from pistol import Pistol


class SoldierBuilder:

    def __init__(self, military_unit_number, name):
        self.__soldier = Soldier(military_unit_number, name).clone()

    def reset(self, military_unit_number, name):
        self.__soldier = Soldier(military_unit_number, name).clone()

    @property
    def soldier(self) -> Soldier:
        soldier = self.__soldier
        return soldier

    def add_knife(self, knife: Knife):
        self.__soldier.add_weapon(knife)

    def add_sapper(self, sapper: SapperBlade):
        self.__soldier.add_weapon(sapper)

    def add_pistol(self, pistol: Pistol):
        self.__soldier.add_weapon(pistol)

    def add_automatic(self, automatic: Automatic):
        self.__soldier.add_weapon(automatic)
