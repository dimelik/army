def binary_search(array, value):
    value = value
    mid = len(array) // 2
    low = 0
    high = len(array) - 1

    while array[mid] != value and low <= high:
        if value > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("No value")
    else:
        return mid
