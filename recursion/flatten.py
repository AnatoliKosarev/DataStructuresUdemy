def flatten(arr):

    result_arr = []

    for el in arr:
        if isinstance(el, list):
            result_arr.extend(flatten(el))
        else:
            result_arr.append(el)

    return result_arr

print(flatten([1, [2, [3, 4], [[5]]]]))
