from soldier_builder import SoldierBuilder
import random
from random import choice
from string import ascii_lowercase
from certain_kill_strategy import CertainKillStrategy


def create_soldier(weapon_factory, amount):
    strategy = CertainKillStrategy()
    amount = int(amount)
    builder = SoldierBuilder(weapon_factory)
    builder.create_new_soldier(9999, 'john'). add_strategy_kill(strategy).add_knife().add_sapper().add_pistol().add_automatic()
    soldiers = []
    for i in range(amount):
        soldier = builder.soldier.clone()
        age = random.randint(25, 100)
        number_mill = random.randint(1000, 400000)
        name_soldier = ''.join(choice(ascii_lowercase) for i in range(12))
        soldier.add_soldier_key(number_mill, name_soldier)
        soldier.age = age
        soldiers.append(soldier)
    return soldiers
