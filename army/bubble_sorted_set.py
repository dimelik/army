class BubbleSortedSet:

    def __init__(self):
        self.__items = []

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
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.__items) - 1):
                if value is not str or float or int:
                    if self.__items[i].name > self.__items[i + 1].name:
                        self.__items[i], self.__items[i + 1] = self.__items[i + 1], self.__items[i]
                else:
                    if self.__items[i].name > self.__items[i + 1].name:
                        # Меняем элементы
                        self.__items[i], self.__items[i + 1] = self.__items[i + 1], self.__items[i]
                        # Устанавливаем swapped в True для следующей итерации
                    swapped = True
