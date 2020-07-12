from bubble_sort import bubble_sort
from binary_search import binary_search

class SortedSet:

    def __init__(self, compare):
        self.__items = []
        self.__compare = compare

    @property
    def get_items(self):
        for items in self.__items:
            yield items

    def remove(self, value):
        index = self.__items.index(value)
        del self.__items[index]

    def get_size(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    def add(self, value):
        if value not in self.__items:
            self.__items.append(value)
        else:
            raise Exception('It is not unique value')
        bubble_sort(self.__items, self.__compare)

    def index_of(self, value):
        result = binary_search(self.__items, value)
        return result
