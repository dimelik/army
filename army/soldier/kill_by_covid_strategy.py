import random

class KillByCovidStrategy:

    def kill(self, soldier):
        if soldier.age <= 60:
            return False
        else:
            x = random.randint(1, 100)
            if x > 15:
                return False
            else:
                return True
