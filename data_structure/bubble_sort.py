def bubble_sort(array, compare):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if compare(array[i], array[i + 1]) > 0:
                # Меняем элементы
                array[i], array[i + 1] = array[i + 1], array[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True


def compare_object(arg1, arg2):
    if arg1.name > arg2.name:
        return 1
    if arg1.name < arg2.name:
        return -1
    if arg1.name == arg2.name:
        return 0
