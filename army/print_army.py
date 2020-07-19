from army import Army
from composite_unit import CompositeUnit
from knife import Knife
from sapper_blade import SapperBlade
from automatic import Automatic
from pistol import Pistol


def soldier_print(unit: CompositeUnit):
    print("Company name: ", unit.name)
    for soldier in unit:
        print("Soldier name:", soldier.name)
        print("Soldier weapon price:", soldier.get_weapon_price().print_amount)
        print("Soldier weapon: ")
        stack_list = []
        while True:
            weapon = soldier.remove_top_weapon
            if weapon is not False:
                stack_list.append(weapon)
            else:
                break

        for stack_full in stack_list[::-1]:
            soldier.add_weapon(stack_full)
        for weapon in stack_list:
            if weapon.__class__ == Knife:
                print("Knife: ", end=" ")
                print("name->", weapon.name, ", price->", weapon.price.print_amount,
                    ", blade length->", weapon.blade_length, ", material->", weapon.material,
                    ", armor_piercing->", weapon.armor_piercing)
            elif weapon.__class__ == SapperBlade:
                print("SapperBlade: ", end=" ")
                print("name->", weapon.name, ", price->", weapon.price.print_amount,
                    ", blade length->", weapon.blade_length, ", material->", weapon.material,
                    ", handle length->", weapon.handle_length)
            elif weapon.__class__ == Pistol:
                print("Pistol: ", end=" ")
                print("name->", weapon.name, ", price->", weapon.price.print_amount,
                    ", caliber->", weapon.caliber, ", attack range->", weapon.range,
                    ", armor piercing->", weapon.armor_piercing)
            elif weapon.__class__ == Automatic:
                print("Automatic: ", end=" ")
                print("name->", weapon.name, ", price->", weapon.price.print_amount,
                    ", caliber->", weapon.caliber, ", attack range->", weapon.range,
                    ", rate fire->", weapon.rate_fire)
            else:
                raise Exception("Your soldier die now")


def print_army(army: Army):
    arm_price = army.army_weapon_price().print_amount
    for composite_unit in army:
        soldier_print(composite_unit)
    print("Army weapon price; ", arm_price)
