from sorted_set import SortedSet


class Map:

    def __init__(self, compare):
        self.__keys = []
        self.__sorted_set = SortedSet(compare)

    def add(self, key, value):
        self.__sorted_set.add(value)
        self.__keys.append(key)

    def get(self, key):
        for soldier in self.__sorted_set.get_items:
            if soldier.get_soldier_key() == key:
                return soldier

    def remove(self, key):
        del self.__keys[key]

    def get_size(self):
        return len(self.__keys)
