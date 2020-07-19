from currency import *
from command import Command
from army import Army


class ArmyCommand(Command):

    def __init__(self, receiver: Army, unit):

        self._receiver = receiver
        self._unit = unit

    def execute(self):
        self._receiver.add_soldiers(self._unit)
