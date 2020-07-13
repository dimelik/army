from sergeant import Sergeant
from knife import Knife
from automatic import Automatic
from pistol import Pistol


class AmericanSergeant(Sergeant):

    def add_weapon_sergeant(self, knife: Knife, pistol: Pistol, automatic: Automatic):
        self.soldier.add_weapon(knife)
        self.soldier.add_weapon(pistol)
        self.soldier.add_weapon(automatic)
        return self.soldier
