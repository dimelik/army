from sorted_set import SortedSet
from soldier import Soldier

class Map:

    def __init__(self, compare):
        self.__keys = []
        self.__sorted_set = SortedSet(compare)

    def add(self, key, value):
        self.__sorted_set.add(value)
        self.__keys.append(key)

    def get(self, key):
        for item in self.__sorted_set.get_items:
            if isinstance(item, Soldier):
                if item.get_soldier_key() == key:
                    return item

    def remove(self, key):
        index_for_set = None
        for soldier in self.__sorted_set.get_items:
            if soldier.get_soldier_key() == key:
                index_for_set = soldier
        self.__sorted_set.remove(index_for_set)
        index = self.__keys.index(key)
        del self.__keys[index]

    def get_size(self):
        return len(self.__keys)
