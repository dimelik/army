from army import Army
from invoker import Invoker
from print_army import print_army
from military_unit import MilitaryUnit
from russian_weapon_factory import RussianWeaponFactory
from american_weapon_factory import AmericanWeaponFactory
from company_command import CompanyCommand
from currency import *
from print_composite_unit import print_composite_unit
from army_command import ArmyCommand


def interface_commands():
    soldiers = None
    rus = RussianWeaponFactory(USD)
    usa = AmericanWeaponFactory(USD)
    print("""
    Hello, please choice: 1 - create american army
                          2 - create russian army
    """)
    army_factor = input()
    army = Army()
    invoke = Invoker()
    print('create companies for army now')
    while True:
        print('input 1 to continue, or something to create company')
        x = input()
        if x == '1':
            break
        print('input name for company')
        name = input()
        unit = MilitaryUnit(name)
        print('How many soldiers you want?')
        amount = input()
        if army_factor == '1':
            company = CompanyCommand(unit, usa, amount)
        if army_factor == '2':
            company = CompanyCommand(unit, rus, amount)
        invoke.set_on_start(company)
        invoke.do_something()
        invoke.set_on_start(ArmyCommand(army, unit))
        invoke.do_something()
    print_army(army)