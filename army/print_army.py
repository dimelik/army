from army import Army
from composite_unit import CompositeUnit
from knife import Knife
from sapper_blade import SapperBlade
from automatic import Automatic
from pistol import Pistol
from soldier import Soldier


def unit_print(unit: CompositeUnit):
    if isinstance(unit, Soldier):
        print("soldier name:", unit.name)
        print("soldier weapon price:", unit.get_weapon_price().print_amount)
        print("soldier weapon: ")
        stack_list = []
        while True:
            weapon = unit.remove_top_weapon
            if weapon is not False:
                stack_list.append(weapon)
            else:
                break

        for stack_full in stack_list[::-1]:
            unit.add_weapon(stack_full)
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
                raise Exception("Your unit die now")
    else:
        print('Company name: ' + unit.name)


def print_army(army: Army):
    arm_price = army.army_weapon_price().print_amount
    for unit in army:
        company_iter(unit)
        unit_print(unit)
    print("Army weapon price; ", arm_price)


def company_iter(unit):
    for unit in unit:
        unit_print(unit)
        company_iter(unit)
