from sorted_set import SortedSet


class Map:

    def __init__(self, compare):
        self.__items = []
        self.__keys_with_items = []
        self.__sorted_set = SortedSet(compare)

    def add(self, key, value):
        if key is not None:
            if value is not None:
                self.__sorted_set.add(key)
                self.__items.append(value)
                key_index = self.__sorted_set.index_of(key)
                value_index = self.__items.index(value)
                self.__keys_with_items.insert(key_index, value_index)
            else:
                raise Exception('map method add must have two parameters(key, value)')
        else:
            raise Exception('map method add must have two parameters(key, value)')

    def get_item(self, key):
        if key is not None:
            index_value = self.__keys_with_items[self.__sorted_set.index_of(key)]
            if index_value is not None:
                return self.__items[index_value]
            else:
                raise Exception('Your map don\'t have this item')
        else:
            raise Exception('map method get_item must have one parameter(key)')

    def get_items(self):
        for item in self.__items:
            yield item

    def remove(self, key):
        if key is not None:
            set_key = self.__sorted_set.index_of(key)
            index_value = self.__keys_with_items[self.__sorted_set.index_of(key)]
            if set_key and index_value is None:
                raise Exception('Your map don\'t have this item')
            else:
                self.__sorted_set.remove(key)
                del self.__items[index_value]
                del self.__keys_with_items[set_key]
        else:
            raise Exception('map method remove must have one parameter(key)')

    def get_size(self):
        return len(self.__items)
