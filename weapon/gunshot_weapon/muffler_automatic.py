from automatic import Automatic


class MufflerAutomatic:

    def __init__(self, automatic: Automatic):
        self.__automatic = automatic

    @property
    def automatic(self):
        return self.__automatic

    @property
    def shot_volume(self):
        return self.automatic.shot_volume // 2
