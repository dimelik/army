from commands.command import Command
from army import Army
from composite_unit import CompositeUnit
from soldier import Soldier


class AddUnitToArmyCommand(Command):

    def __init__(self, army: Army, unit: CompositeUnit):
        self._army = army
        self._unit = unit

    def execute(self):
        if isinstance(self._unit, Soldier):
            self._unit.attach(self._army)
        self._army.add(self._unit)
        return self._unit
