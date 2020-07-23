from currency import *
from commands.command import Command
from military_unit import MilitaryUnit
from create_soldier import create_soldier


class AddSoldierToCompanyCommand(Command):

    def __init__(self, company: MilitaryUnit, weapon_factory, amount):
        self._company = company
        self._unit = create_soldier(weapon_factory, amount)

    def execute(self):
        for unit in self._unit:
            self._company.add(unit)
        return self._company
