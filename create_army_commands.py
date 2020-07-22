from print_army import print_army
from military_unit import MilitaryUnit
from russian_weapon_factory import RussianWeaponFactory
from american_weapon_factory import AmericanWeaponFactory
from currency import *
from commands.add_soldier_to_company_command import AddSoldierToCompanyCommand
from commands.add_unit_to_army_command import AddUnitToArmyCommand


def create_army_commands(army):
    army = army
    rus = RussianWeaponFactory(USD)
    usa = AmericanWeaponFactory(USD)
    while True:
        print("""
                    please choice:        1 - create american army
                                          2 - create russian army
                                          0 - exit
                    """)
        army_factor = input()
        if army_factor == '0':
            break
        print('create companies for army now')
        while True:
            print('input 1 to exit, or something to create company')
            x = input()
            if x == '1':
                break
            print('input name for company')
            name = input()
            unit = MilitaryUnit(name)
            print('How many soldiers you want?')
            amount = input()
            if army_factor == '1':
                company = AddSoldierToCompanyCommand(unit, usa, amount).execute()
            if army_factor == '2':
                company = AddSoldierToCompanyCommand(unit, rus, amount).execute()
            AddUnitToArmyCommand(army, company).execute()
        print_army(army)
        # while True:
        #     print('if you want to kill a soldier, enter the soldier\'s name or enter 1 to continue')
        #     name = input()
        #     if name == "1":
        #         break
        #     killer = SoldierKiller()
        #     killer.attach(army)
        #     soldier = army.get_unit(name)
        #     soldier.kill()
        # killer.notify()
        return army

