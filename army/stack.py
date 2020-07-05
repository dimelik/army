class Stack:
    def __init__(self):
        self.__items = []

    def push(self, value):
        self.__items.append(value)

    def pop(self):
        if len(self.__items) == 0:
            return False
        return self.__items.pop()

    def top(self):
        if len(self.__items) == 0:
            return None
        return self.__items[-1]
