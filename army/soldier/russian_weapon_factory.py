from weapon_factory import WeaponFactory
from sapper_blade import SapperBlade
from automatic import Automatic
from pistol import Pistol
from knife import Knife
from currency import *
from money import Money


class RussianWeaponFactory(WeaponFactory):

    def create_pistol(self):
        pistol = Pistol(Money(1000, USD), 'PM')
        pistol.armor_piercing = 20
        pistol.caliber = 9
        pistol.range = 100
        return pistol

    def create_knife(self):
        knife = Knife(Money(300.05, USD), 'Vader')
        knife.armor_piercing = 80
        knife.blade_length = 20
        knife.material = 'steel'
        return knife

    def create_sapper(self):
        sapper = SapperBlade(Money(300.20, USD), 'Sapp')
        sapper.handle_length = 20
        sapper.blade_length = 15
        sapper.material = 'steel'
        return sapper

    def create_automatic(self):
        automatic = Automatic(Money(2300, USD), 'AK')
        automatic.rate_fire = 30
        automatic.caliber = 6.2
        automatic.range = 3000
        return automatic
