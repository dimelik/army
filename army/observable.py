from abc import ABC


class Observable(ABC):
    _companies = {}

    def attach(self, event, callback):
        self._companies[event] = callback

    def detach(self, event, callback):
        for key, value in self._companies.items():
            if key == event and value == callback:
                value()

    def notify(self, event):
        for key, value in self._companies.items():
            if key == event:
                value()
