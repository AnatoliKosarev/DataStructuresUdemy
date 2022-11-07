import math


# Only with sorted arrays
def binary_search(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end) / 2)
    print(start, middle, end)

    while array[middle] != value and start <= end:
        if value > array[middle]:
            start = middle + 1
        else:
            end = middle - 1

        middle = math.floor((start + end) / 2)
        print(start, middle, end)

    if value == array[middle]:
        return middle
    else:
        return -1


test_list = [2, 4, 6, 8, 10, 12, 14, 15, 19, 23]
print(binary_search(test_list, 8))
