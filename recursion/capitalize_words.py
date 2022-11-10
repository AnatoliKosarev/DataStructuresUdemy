def capitalize_words(arr):
    result_list = []

    if len(arr) <= 0:
        return result_list

    result_list.append(str(arr[0]).upper())

    return result_list + capitalize_words(arr[1:])


print(capitalize_words(['i', 'am', 'learning', 'recursion']))