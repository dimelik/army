class Map:

    def __init__(self):
        self.__items = dict()

    def add(self, key, value):
        if key not in self.__items:
            self.__items[key] = value
        else:
            raise Exception('It is not unique value')

    def get(self, key):
        return self.__items[key]

    def remove(self, key):
        del self.__items[key]

    def get_size(self):
        return len(self.__items)
