def partition(start, end, list_to_sort):
    i = start - 1
    pivot = list_to_sort[end]

    for j in range(start, end):
        if list_to_sort[j] <= pivot:
            i += 1
            if i != j:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]

    if i+1 != end:
        list_to_sort[i+1], list_to_sort[end] = list_to_sort[end], list_to_sort[i+1]

    return i+1


def quicksort(start, end, list_to_sort):
    if start < end:
        pi = partition(start, end, list_to_sort)
        quicksort(start, pi-1, list_to_sort)
        quicksort(pi+1, end, list_to_sort)


test_list = [7, 2, 6, 1, 4, 3]
quicksort(0, len(test_list) - 1, test_list)
print(test_list)