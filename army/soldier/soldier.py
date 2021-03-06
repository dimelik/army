from bug import Bug
from soldier_key import SoldierKey
import copy
from composite_unit import CompositeUnit
from observable import Observable


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


class Soldier(CompositeUnit, Observable):

    __age = None
    __strategy = None
    __is_dead = False

    def __init__(self, military_unit_number, name):
        self.__bug = Bug()
        self.__name = name
        self.__military_unit_number = military_unit_number
        self.__soldier_key = SoldierKey(self.__military_unit_number, self.__name)

    def set_strategy_kill(self, strategy):
        self.__strategy = strategy

    def kill(self):
        if self.__strategy is not None:
            self.__is_dead = self.__strategy.kill(self)
        else:
            raise Exception('Please choice strategy for kill in set_strategy_kill method')
        Observable.notify(self, 'kill')

    @property
    def is_dead(self):
        return self.__is_dead

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
