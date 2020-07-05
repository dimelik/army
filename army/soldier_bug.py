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

    @property
    def stack(self):
        return self.__stack


x = Bug()
x.add('123')
x.add(123)
print(x.get_last_added())
