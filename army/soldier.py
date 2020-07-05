from soldier_bug import Bug


class Soldier:

    def __init__(self, name: str):
        self.__bug = Bug()
        self.__name = name

    @property
    def weapon_price(self):
        copy_bug = self.__bug.weapons.copy()
        result = copy_bug.pop().price
        for weapon in copy_bug:
            result = result.add(weapon.price)
        return result

    @property
    def name(self):
        return self.__name

    @property
    def bug(self):
        return self.__bug

    @property
    def soldier_weapon(self):
        return self.__bug.weapon
