from soldier import Soldier


class SoldierBuilder:

    def __init__(self, name_weapon_factory):
        self.__weapon_factory = name_weapon_factory
        self.__soldier = None

    def reset(self, military_unit_number: int, name: str):
        self.__soldier = Soldier(military_unit_number, name)

    @property
    def soldier(self):
        soldier = self.__soldier
        return soldier

    def create_new_soldier(self, military_unit_number: int, name: str):
        self.__soldier = Soldier(military_unit_number, name)
        return self

    def add_strategy_kill(self, strategy):
        self.__soldier.set_strategy_kill(strategy)
        return self

    def add_knife(self):
        knife = self.__weapon_factory.create_knife()
        self.__soldier.add_weapon(knife)
        return self

    def add_sapper(self):
        sapper = self.__weapon_factory.create_sapper()
        self.__soldier.add_weapon(sapper)
        return self

    def add_pistol(self):
        pistol = self.__weapon_factory.create_pistol()
        self.__soldier.add_weapon(pistol)
        return self

    def add_automatic(self):
        automatic = self.__weapon_factory.create_automatic()
        self.__soldier.add_weapon(automatic)
        return self
