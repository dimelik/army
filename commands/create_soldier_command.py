from soldier_builder import SoldierBuilder


class CreateSoldierCommand:
    def __init__(self, name, mill_number, strategy, weapon_factory):
        self._name = name
        self._mill_number = mill_number
        self._strategy = strategy
        self._weapon_factory = weapon_factory

    def execute(self):
        builder = SoldierBuilder(self._weapon_factory)
        builder.create_new_soldier(self._mill_number, self._name,
                                   self._strategy).add_knife().add_sapper().add_pistol().add_automatic()
        soldier = builder.soldier
        return soldier
