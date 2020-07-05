class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        return self.__stack.pop()

    def top(self):
        return self.__stack[-1]

    def stack(self):
        return self.__stack
