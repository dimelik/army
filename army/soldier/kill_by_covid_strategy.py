import random


class KillByCovidStrategy:

    def kill(self):
        x = random.randint(1, 100)
        if x > 15:
            return 0
        else:
            return 1
