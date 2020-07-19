from army import Army
from invoker import Invoker
from print_army import print_army
from military_unit import MilitaryUnit
from russian_weapon_factory import RussianWeaponFactory
from american_weapon_factory import AmericanWeaponFactory
from company_command import CompanyCommand
from currency import *
from army_command import ArmyCommand
from soldier_killer import SoldierKiller


def interface_commands():
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
        invoke.set_on_finish(ArmyCommand(army, unit))
        invoke.do_something()
    print_army(army)

    while True:
        print('if you want to kill a soldier, enter the soldier\'s name or enter 1 to continue')
        name = input()
        if name == "1":
            break
        print(army.get_soldier(name))
        killer = SoldierKiller()
        killer.attach(army)
        soldier = army.get_soldier(name)
        soldier.kill()
    killer.notify()
    print_army(army)

