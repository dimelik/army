from bug import Bug
from weapon import Weapon


class Soldier:

    def __init__(self, name: str):
        self.__bug = Bug()
        self.__name = name

    def weapon_price(self):
        stack_list = []
        while True:
            weapon = self.remove_weapon
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

    @property
    def name(self):
        return self.__name

    def add_weapon(self, value):
        self.__bug.add(value)

    @property
    def remove_weapon(self):
        return self.__bug.remove_last_added()

