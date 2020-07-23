from commands.remove_soldier_from_company import RemoveSoldierFromCompany
from commands.remove_unit_from_army import RemoveUnitFromArmyCommand
from military_unit import MilitaryUnit
from commands.add_unit_to_army_command import AddUnitToArmyCommand
from create_soldier_add_army import create_soldier_add_army
from print_army import *
from currency import *
from create_army_commands import create_army_commands
from army import Army


class MenuInitCommand:
    def execute(self):
        company = None
        while True:
            print("""
                    Hello, please choice: 1 - create army with companies
                                          2 - create soldier and add to army
                                          3 - create company
                                          4 - add soldier to company
                                          5 - add  company in army
                                          6 - remove soldier from company
                                          7 - remove unit from army
                                          8 - kill soldier
                                          0 - exit
                    """)
            menu_input = input()
            army = Army()
            if menu_input == '0':
                break
            if menu_input == '1':
                create_army_commands(army)
                print_army(army)
            if menu_input == '2':
                soldier = create_soldier_add_army()
                AddUnitToArmyCommand(army, soldier).execute()
                print_army(army)
            if menu_input == '3':
                print('input name your company')
                name = input()
                company = MilitaryUnit(name)
                print('you create company ' + name)
            if menu_input == '4':
                soldier = create_soldier_add_army()
                company.add(soldier)
                print('your soldier add to ' + name + ' success')
                company_iter(company)
            if menu_input == '5':
                AddUnitToArmyCommand(army, company).execute()
                print_army(army)
            if menu_input == '6':
                print('input soldier name')
                name = input()
                soldier = company.get_soldier(name)
                RemoveSoldierFromCompany(company, soldier).execute()
                print('remove success')
                company_iter(company)
            if menu_input == '7':
                print('input unit name')
                name = input()
                unit = army.get_unit(name)
                RemoveUnitFromArmyCommand(army, unit).execute()
                print('remove success')
                print_army(army)
            if menu_input == '8':
                print('input unit name')
                name = input()
                unit = army.get_unit(name)
                unit.kill()
                print('kill success')
                print_army(army)