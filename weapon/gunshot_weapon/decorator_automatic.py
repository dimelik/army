from automatic import Automatic


class DecoratorAutomatic:

    def __init__(self, automatic: Automatic):
        self.__automatic = automatic

    @property
    def automatic(self):
        return self.__automatic

    def add_muffler(self) -> None:
        self.automatic.shot_volume = self.automatic.shot_volume // 2
