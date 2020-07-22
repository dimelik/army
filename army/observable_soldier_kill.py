from abc import ABC
from observer_soldier import ObserverSoldier


class ObservableSoldierKill(ABC):
    companies = []

    def attach(self, soldier: ObserverSoldier):
        self.companies.append(soldier)

    def detach(self, soldier: ObserverSoldier):
        self.companies.remove(soldier)

    def notify(self):
        for company in self.companies:
            company.update()




