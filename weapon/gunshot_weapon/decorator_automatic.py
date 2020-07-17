from automatic import Automatic


class DecoratorAutomatic:

    def __init__(self, automatic: Automatic, shot_volume):
        self.__automatic = automatic
        self.__shot_volume = shot_volume

    @property
    def shot_volume(self):
        return self.__shot_volume

    @property
    def automatic(self):
        return self.__automatic

    def add_muffler(self) -> None:
        self.__shot_volume = self.__shot_volume // 2
