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
from Money import Money


def solder_weapon_print(soldier):
    print("Soldier name:", soldier.name)
    print("Soldier Weapon: ")
    print("Knife: ", end=" ")
    print("name->", soldier.knife.name, ", price->", soldier.knife.price,
          ", blade length->", soldier.knife.blade_length, ", material->", soldier.knife.material,
          ", armor_piercing->", soldier.knife.armor_piercing)
    print("SapperBlade: ", end=" ")
    print("name->", soldier.sapper_blade.name, ", price->", soldier.sapper_blade.price,
          ", blade length->", soldier.sapper_blade.blade_length, ", material->", soldier.sapper_blade.material,
          ", handle length->", soldier.sapper_blade.handle_length)
    print("Pistol: ", end=" ")
    print("name->", soldier.pistol.name, ", price->", soldier.pistol.price,
          ", caliber->", soldier.pistol.caliber, ", attack range->", soldier.pistol.range,
          ", armor piercing->", soldier.pistol.armor_piercing)
    print("Automatic: ", end=" ")
    print("name->", soldier.automatic.name, ", price->", soldier.automatic.price,
          ", caliber->", soldier.automatic.caliber, ", attack range->", soldier.automatic.range,
          ", rate fire->", soldier.automatic.rate_fire)
    print("Soldier weapon price:", soldier.weapon_price)


money = Money(0)

automatic = Automatic(Money(23), 'AK')
automatic.rateFire = 30
automatic.caliber = 6.2
automatic.range = 3000
pistol = Pistol(Money(10), 'Colt')
pistol.armor_piercing = 30
pistol.caliber = 9
pistol.range = 200
knife = Knife(Money(3), 'Vader')
knife.price = Money(10)
knife.armor_piercing = 80
knife.blade_length = 20
knife.material = 'steel'
knife2 = Knife(Money(2), 'Knife')
knife2.armor_piercing = 90
knife2.blade_length = 15
knife2.material = 'steel'
sapper = SapperBlade(Money(3), 'Sapp')
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
print("Army weapon price:", army.army_weapon_price)
for soldier in army.soldiers:
    solder_weapon_print(soldier)
