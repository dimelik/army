from american_weapon_factory import AmericanWeaponFactory
from certain_kill_strategy import CertainKillStrategy
from russian_weapon_factory import RussianWeaponFactory
from soldier_builder import SoldierBuilder
from currency import *
from commands.create_soldier_command import CreateSoldierCommand


def create_soldier_add_army():
    print("""
                    please choice:        1 - create american soldier
                                          2 - create russian soldier
                    """)
    choice = input()
    if choice == '1':
        weapon_factory = AmericanWeaponFactory(USD)
    if choice == '2':
        weapon_factory = RussianWeaponFactory(USD)
    print('name your soldier')
    name = input()
    print('military number your soldier')
    mill_number = input()
    mill_number = int(mill_number)
    soldier = CreateSoldierCommand(name, mill_number, CertainKillStrategy(), weapon_factory).execute()
    return soldier
