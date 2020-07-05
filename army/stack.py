class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        return self.__stack.pop()

    def top(self):
        if len(self.__stack) == 0:
            return False
        return self.__stack[-1]
