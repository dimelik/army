from bug import Bug
from soldier_key import SoldierKey
import copy
from composite_unit import CompositeUnit
from certain_kill_strategy import CertainKillStrategy
from kill_by_covid_strategy import KillByCovidStrategy


def compare_object(arg1, arg2):
    if arg1.name > arg2.name:
        return 1
    if arg1.name < arg2.name:
        return -1
    if arg1.name == arg2.name:
        return 0


def compare_key(arg1, arg2):
    if arg1 > arg2:
        return 1
    if arg1 < arg2:
        return -1
    if arg1 == arg2:
        return 0


class Soldier(CompositeUnit):

    __age = None

    def __init__(self, military_unit_number, name, strategy):
        self.__strategy = strategy
        self.__kill = 0
        self.__bug = Bug()
        self.__name = name
        self.__military_unit_number = military_unit_number
        self.soldier_key = SoldierKey(self.__military_unit_number, self.__name)

    @property
    def is_die(self):
        return self.__kill

    def kill(self):
        if isinstance(self.__strategy, CertainKillStrategy):
            self.__kill = self.__strategy.kill()
        if isinstance(self.__strategy, KillByCovidStrategy):
            if self.__age > 60:
                self.__kill = self.__strategy.kill()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def get_weapon_price(self):
        stack_list = []
        while True:
            weapon = self.remove_top_weapon
            if weapon is not False:
                stack_list.append(weapon)
            else:
                break
        first_from_stack_list = stack_list.pop()
        return_price = first_from_stack_list.price
        for price in stack_list[::-1]:
            return_price = return_price.add(price.price)
        stack_list.append(first_from_stack_list)
        for stack_full in stack_list[::-1]:
            self.add_weapon(stack_full)
        return return_price

    def add_weapon(self, value):
        self.__bug.add(value)

    @property
    def remove_top_weapon(self):
        return self.__bug.remove_last_added()

    def get_soldier_key(self):
        return self.__soldier_key.name + self.__soldier_key.military_unit_number

    def add_soldier_key(self, military_unit_number, name):
        self.__soldier_key = SoldierKey(military_unit_number, name)

    @property
    def name(self):
        return self.__soldier_key.name

    def clone(self):
        return copy.deepcopy(self)
