from army import Army
from soldier import Soldier


def soldier_print(soldier: Soldier):
    print("Soldier name:", soldier.name)
    print("Soldier weapon: ")
    print("Knife: ", end=" ")
    print("name->", soldier.knife.name, ", price->", soldier.knife.price.amount_print,
          ", blade length->", soldier.knife.blade_length, ", material->", soldier.knife.material,
          ", armor_piercing->", soldier.knife.armor_piercing)
    print("SapperBlade: ", end=" ")
    print("name->", soldier.sapper_blade.name, ", price->", soldier.sapper_blade.price.amount_print,
          ", blade length->", soldier.sapper_blade.blade_length, ", material->", soldier.sapper_blade.material,
          ", handle length->", soldier.sapper_blade.handle_length)
    print("Pistol: ", end=" ")
    print("name->", soldier.pistol.name, ", price->", soldier.pistol.price.amount_print,
          ", caliber->", soldier.pistol.caliber, ", attack range->", soldier.pistol.range,
          ", armor piercing->", soldier.pistol.armor_piercing)
    print("Automatic: ", end=" ")
    print("name->", soldier.automatic.name, ", price->", soldier.automatic.price.amount_print,
          ", caliber->", soldier.automatic.caliber, ", attack range->", soldier.automatic.range,
          ", rate fire->", soldier.automatic.rate_fire)
    print("Soldier weapon price:", soldier.weapon_price.amount_print)


def army_print(army: Army):
    print("Army weapon price:", army.army_weapon_price.amount_print)
    for soldier in army.soldiers:
        soldier_print(soldier)
