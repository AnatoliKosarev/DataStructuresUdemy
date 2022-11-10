def capitalize_first(arr):
    result_list = []

    if len(arr) == 0:
        return result_list

    result_list.append(str(arr[0]).capitalize())
    return result_list + capitalize_first(arr[1:])


print(capitalize_first([123, 'taco', 'banana']))