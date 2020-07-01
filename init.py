import sys

sys.path.append('Weapon/')
sys.path.append('Weapon/ColdWeapon/')
sys.path.append('Weapon/GunshotWeapon/')
from Army import Army
from Soldier import Soldier
from Knife import Knife
from SapperBlade import SapperBlade
from Automatic import Automatic
from Pistol import Pistol


automatic = Automatic(2, 'AK')
automatic.rateFire = 30
automatic.caliber = 6.2
automatic.range = 3000
pistol = Pistol(2, 'Colt')
pistol.armorPiercing = 30
pistol.caliber = 9
pistol.range = 200
knife = Knife(2, 'Knife')
knife.armorPiercing = 90
knife.bladeLength = 15
knife.material = 'steel'
sapper = SapperBlade(2, 'Sapp')
sapper.handleLength = 20
sapper.bladeLength = 15
sapper.material = 'steel'

soldier = Soldier()
soldier.pistol = pistol
soldier.knife = knife
soldier.sapperBlade = sapper
soldier.automatic = automatic
army = Army(soldier, soldier, soldier, soldier, soldier, soldier, soldier)
print(army.armyWeaponPrice)
