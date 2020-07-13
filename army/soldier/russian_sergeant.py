from sergeant import Sergeant
from sapper_blade import SapperBlade
from automatic import Automatic
from pistol import Pistol


class RussianSergeant(Sergeant):

    def add_weapon_sergeant(self, sapper: SapperBlade, pistol: Pistol, automatic: Automatic):
        self.soldier.add_weapon(sapper)
        self.soldier.add_weapon(pistol)
        self.soldier.add_weapon(automatic)
        return self.soldier
