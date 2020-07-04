import sys
sys.path.append('army/')
sys.path.append('weapon/')
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


automatic = Automatic(Money(2300), 'AK')
automatic.rate_fire = 30
automatic.caliber = 6.2
automatic.range = 3000
pistol = Pistol(Money(1000), 'Colt')
pistol.armor_piercing = 30
pistol.caliber = 9
pistol.range = 200
knife = Knife(Money(300), 'Vader')
knife.price = Money(1000)
knife.armor_piercing = 80
knife.blade_length = 20
knife.material = 'steel'
knife2 = Knife(Money(200), 'Knife')
knife2.armor_piercing = 90
knife2.blade_length = 15
knife2.material = 'steel'
sapper = SapperBlade(Money(300), 'Sapp')
sapper.handle_length = 20
sapper.blade_length = 15
sapper.material = 'steel'

soldier = Soldier('capral')
soldier.pistol = pistol
soldier.knife = knife
soldier.sapper_blade = sapper
soldier.automatic = automatic

soldier2 = Soldier('easy')
soldier2.pistol = pistol
soldier2.knife = knife2
soldier2.sapper_blade = sapper
soldier2.automatic = automatic

army = Army(soldier, soldier2, soldier, soldier2)

army_print(army)

