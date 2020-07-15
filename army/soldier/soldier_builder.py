from soldier import Soldier


class SoldierBuilder:

    def __init__(self, military_unit_number: int, name: str, name_weapon_factory):
        self.__soldier = Soldier(military_unit_number, name)
        self.__weapon_factory = name_weapon_factory

    def reset(self, military_unit_number: int, name: str):
        self.__soldier = Soldier(military_unit_number, name)

    @property
    def soldier(self):
        soldier = self.__soldier
        return soldier

    def add_knife(self):
        knife = self.__weapon_factory.create_knife()
        self.__soldier.add_weapon(knife)

    def add_sapper(self):
        sapper = self.__weapon_factory.create_sapper()
        self.__soldier.add_weapon(sapper)

    def add_pistol(self):
        pistol = self.__weapon_factory.create_pistol()
        self.__soldier.add_weapon(pistol)

    def add_automatic(self):
        automatic = self.__weapon_factory.create_automatic()
        self.__soldier.add_weapon(automatic)
