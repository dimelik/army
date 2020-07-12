from bug import Bug
from soldier_key import SoldierKey


def compare_object(arg1, arg2):
    if arg1.name > arg2.name:
        return 1
    if arg1.name < arg2.name:
        return -1
    if arg1.name == arg2.name:
        return 0


class Soldier:

    def __init__(self, soldier_key: SoldierKey):
        self.__bug = Bug()
        self.__soldier_key = soldier_key

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
