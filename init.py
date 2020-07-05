import sys

sys.path.append('army/')
sys.path.append('weapon/')
sys.path.append('money/')
sys.path.append('data_structure/')
sys.path.append('weapon/cold_weapon/')
sys.path.append('weapon/gunshot_weapon/')

from army import Army
from soldier import Soldier
from knife import Knife
from sapper_blade import SapperBlade
from automatic import Automatic
from pistol import Pistol
from money import Money
from print_army import *
from currency import *

automatic = Automatic(Money(2300, USD), 'AK')
automatic.rate_fire = 30
automatic.caliber = 6.2
automatic.range = 3000
pistol = Pistol(Money(1000, USD), 'Colt')
pistol.armor_piercing = 30
pistol.caliber = 9
pistol.range = 200
knife = Knife(Money(300.05, USD), 'Vader')
knife.armor_piercing = 80
knife.blade_length = 20
knife.material = 'steel'
knife2 = Knife(Money(400.3, USD), 'Knife')
knife2.armor_piercing = 90
knife2.blade_length = 15
knife2.material = 'steel'
sapper = SapperBlade(Money(300.20, USD), 'Sapp')
sapper.handle_length = 20
sapper.blade_length = 15
sapper.material = 'steel'

soldier = Soldier('ab')
soldier.add_weapon(pistol)
soldier.add_weapon(knife)
soldier.add_weapon(sapper)
soldier.add_weapon(automatic)

soldier2 = Soldier('aaa')
soldier2.add_weapon(pistol)
soldier2.add_weapon(knife2)
soldier2.add_weapon(sapper)
soldier2.add_weapon(automatic)

army = Army(soldier, soldier2)

print_army(army)


