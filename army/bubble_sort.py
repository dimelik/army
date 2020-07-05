def bubble_sorted_set(tuple_soldier):
    solder_set = []
    for sold in tuple_soldier:
        if sold not in solder_set:
            solder_set.append(sold)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(solder_set) - 1):
            if solder_set[i].name > solder_set[i + 1].name:
                # Меняем элементы
                solder_set[i], solder_set[i + 1] = solder_set[i + 1], solder_set[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return solder_set
