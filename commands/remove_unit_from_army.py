from commands.command import Command
from army import Army
from composite_unit import CompositeUnit


class RemoveUnitFromArmyCommand(Command):

    def __init__(self, army: Army, unit: CompositeUnit):
        self._army = army
        self._unit = unit

    def execute(self):
        self._army.remove_unit(self._unit)
