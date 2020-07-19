from __future__ import annotations
from collections.abc import Iterator


class Iter(Iterator):

    _position: int = None

    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        if not isinstance(self._collection, list):
            try:
                value = next(self._collection)
            except IndexError:
                raise StopIteration()
        else:
            try:
                value = self._collection[self._position]
                self._position += 1
            except IndexError:
                raise StopIteration()

        return value
