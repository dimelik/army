from weapon_factory import WeaponFactory
from sapper_blade import SapperBlade
from automatic import Automatic
from pistol import Pistol
from knife import Knife
from currency import *
from money import Money


class AmericanWeaponFactory(WeaponFactory):

    def create_pistol(self):
        pistol = Pistol(Money(1500, self._currency), 'Colt')
        pistol.armor_piercing = 30
        pistol.caliber = 9
        pistol.range = 200
        return pistol

    def create_knife(self):
        knife = Knife(Money(200, self._currency), 'Fook')
        knife.armor_piercing = 60
        knife.blade_length = 30
        knife.material = 'steel'
        return knife

    def create_sapper(self):
        sapper = SapperBlade(Money(100, self._currency), 'Blader')
        sapper.handle_length = 30
        sapper.blade_length = 20
        sapper.material = 'steel'
        return sapper

    def create_automatic(self):
        automatic = Automatic(Money(2400, self._currency), 'M-18')
        automatic.rate_fire = 25
        automatic.caliber = 5.4
        automatic.range = 2500
        return automatic
