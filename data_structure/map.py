from sorted_set import SortedSet
from soldier import Soldier


class Map:

    def __init__(self, compare):
        self.__items = []
        self.__keys_with_items = []
        self.__sorted_set = SortedSet(compare)

    def add(self, key, value):
        self.__sorted_set.add(key)
        self.__items.append(value)
        key_index = self.__sorted_set.index_of(key)
        value_index = self.__items.index(value)
        self.__keys_with_items.insert(key_index, value_index)

    def get_item(self, key):
        index_value = self.__keys_with_items[self.__sorted_set.index_of(key)]
        return self.__items[index_value]

    def get_items(self):
        for index_value in self.__keys_with_items:
            yield self.__items[index_value]

    def remove(self, key):
        index_for_set = None
        for soldier in self.__sorted_set.get_items:
            if soldier.get_soldier_key() == key:
                index_for_set = soldier
        self.__sorted_set.remove(index_for_set)
        index = self.__items.index(key)
        del self.__items[index]

    def get_size(self):
        return len(self.__items)
