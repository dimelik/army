from currency import *
from command import Command
from military_unit import MilitaryUnit
from create_soldier import create_soldier


class CompanyCommand(Command):

    def __init__(self, receiver: MilitaryUnit, weapon_factory, amount):
        self._receiver = receiver
        self._unit = create_soldier(weapon_factory, amount)

    def execute(self):
        for unit in self._unit:
            self._receiver.add(unit)
