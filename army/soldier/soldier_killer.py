class SoldierKiller:

    _army = []

    def attach(self, observer):
        self._army.append(observer)

    def detach(self, observer):
        self._army.remove(observer)

    def notify(self):
        for army in self._army:
            army.update()
