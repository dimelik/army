from stack import Stack


class Bug:
    def __init__(self):
        self.__stack = Stack()

    def add(self, value):
        self.__stack.push(value)

    def get_last_added(self):
        return self.__stack.top()

    def remove_last_added(self):
        return self.__stack.pop()

