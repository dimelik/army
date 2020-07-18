from gunshot_weapon import GunshotWeapon


class Automatic(GunshotWeapon):
    __rateFire = None
    __shot_volume = None

    @property
    def rate_fire(self):
        return self.__rateFire

    @rate_fire.setter
    def rate_fire(self, value: int):
        self.__rateFire = value

    @property
    def shot_volume(self):
        return self.__shot_volume

    @shot_volume.setter
    def shot_volume(self, value):
        self.__shot_volume = value

    def add_muffler(self):
        self.shot_volume = self.shot_volume // 1.3
