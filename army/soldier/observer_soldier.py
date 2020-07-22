from abc import ABC


class ObserverSoldier(ABC):
    def remove(self):
        pass

    def update(self):
        for unit in self:
            if unit.is_dead is True:
                self.remove(unit)
