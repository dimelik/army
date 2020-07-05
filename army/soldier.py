from bug import Bug
from weapon import Weapon


class Soldier:

    def __init__(self, name: str):
        self.__bug = Bug()
        self.__name = name

    @property
    def weapon_price(self):
        stack_list = []
        while True:
            if not self.weapon:
                break
            else:
                stack_list.append(self.remove_weapon)
        first_from_stack_list = stack_list.pop()
        return_price = first_from_stack_list.price
        for price in stack_list[::-1]:
            return_price = return_price.add(price.price)
        stack_list.append(first_from_stack_list)
        for stack_full in stack_list[::-1]:
            self.add_weapon = stack_full
        return return_price

    @property
    def name(self):
        return self.__name

    @property
    def weapon(self):
        return self.__bug.get_last_added()

    @weapon.setter
    def add_weapon(self, value: Weapon):
        self.__bug.add(value)

    @property
    def remove_weapon(self):
        return self.__bug.remove_last_added()

