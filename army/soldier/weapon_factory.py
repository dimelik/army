from abc import ABC, abstractmethod


class WeaponFactory(ABC):
    @abstractmethod
    def create_pistol(self):
        pass

    @abstractmethod
    def create_knife(self):
        pass

    @abstractmethod
    def create_sapper(self):
        pass

    @abstractmethod
    def create_automatic(self):
        pass
