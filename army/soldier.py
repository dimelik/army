import sys

sys.path.append('../army/')
sys.path.append('../weapon/')
sys.path.append('../money/')
sys.path.append('../weapon/cold_weapon/')
sys.path.append('../weapon/gunshot_weapon/')
from soldier_bug import Bug
from weapon import Weapon
from knife import Knife
from sapper_blade import SapperBlade
from automatic import Automatic
from pistol import Pistol
from currency import *
from money import Money

class Soldier:

    def __init__(self, name: str):
        self.__bug = Bug()
        self.__name = name

    @property
    def weapon_price(self):
        copy_bug = self.bug.stack.copy()
        result = copy_bug.pop().price
        for weapon in copy_bug:
            result = result.add(weapon.price)
        return result

    @property
    def name(self):
        return self.__name

    @property
    def bug(self):
        return self.__bug.stack

    @property
    def weapon(self):
        return self.__bug.get_last_added

    @weapon.setter
    def weapon(self, value: Weapon):
        self.__bug.add(value)

    @property
    def remove_weapon(self):
        return self.__bug.remove_last_added


sol = Soldier('asd')
sapper = SapperBlade(Money(300.20, USD), 'Sapp')
sapper.handle_length = 20
sapper.blade_length = 15
sapper.material = 'steel'

sol.weapon = sapper
print(sol.weapon)
