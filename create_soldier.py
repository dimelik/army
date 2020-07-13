from soldier_builder import SoldierBuilder
import random
from random import choice
from string import ascii_lowercase


def create_soldier(sapper, automatic, pistol, knife):
    builder = SoldierBuilder(9999, 'john')
    soldiers = []
    for i in range(99):
        number_mill = random.randint(1000, 400000)
        name_soldier = ''.join(choice(ascii_lowercase) for i in range(12))
        builder.add_knife(knife)
        builder.add_sapper(sapper)
        builder.add_pistol(pistol)
        builder.add_automatic(automatic)
        soldiers.append(builder.soldier)
        builder.reset(number_mill, name_soldier)
    return soldiers
