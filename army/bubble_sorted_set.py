class BubbleSortedSet:

    def __init__(self):
        self.__sorted_set = []

    @property
    def get_items(self):
        return self.__sorted_set

    def remove(self, value):
        self.__sorted_set[value] = None

    def get_size(self):
        return len(self.__sorted_set)

    def clear(self):
        self.__sorted_set = []

    def add(self, value):
        if value not in self.__sorted_set:
            self.__sorted_set.append(value)
        else:
            raise Exception('It is not unique value')
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.__sorted_set) - 1):
                if value is not str or float or int:
                    if self.__sorted_set[i].name > self.__sorted_set[i + 1].name:
                        self.__sorted_set[i], self.__sorted_set[i + 1] = self.__sorted_set[i + 1], self.__sorted_set[i]
                else:
                    if self.__sorted_set[i].name > self.__sorted_set[i + 1].name:
                        # Меняем элементы
                        self.__sorted_set[i], self.__sorted_set[i + 1] = self.__sorted_set[i + 1], self.__sorted_set[i]
                        # Устанавливаем swapped в True для следующей итерации
                    swapped = True
