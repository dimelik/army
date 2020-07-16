from soldier_builder import SoldierBuilder
import random
from random import choice
from string import ascii_lowercase


def create_soldier(weapon_factory):
    builder = SoldierBuilder(9999, 'john', weapon_factory)
    builder.add_knife()
    builder.add_sapper()
    builder.add_pistol()
    builder.add_automatic()
    soldiers = []
    for i in range(99):
        soldier = builder.soldier.clone()
        number_mill = random.randint(1000, 400000)
        name_soldier = ''.join(choice(ascii_lowercase) for i in range(12))
        soldier.add_soldier_key(number_mill, name_soldier)
        soldiers.append(soldier)
    return soldiers
