class Map:

    def __init__(self):
        self.__items = dict()

    def add(self, key, value):
        self.__items[key] = value

    def get(self, key):
        return self.__items

    def remove(self, key):
        del self.__items[key]

    def get_size(self):
        return len(self.__items)
