from soldier import Soldier
from commands.command import Command
from composite_unit import CompositeUnit


class RemoveSoldierFromCompany(Command):

    def __init__(self, company: CompositeUnit, soldier: Soldier):
        self._soldier = soldier
        self._company = company

    def execute(self):
        self._company.remove(self._soldier)
