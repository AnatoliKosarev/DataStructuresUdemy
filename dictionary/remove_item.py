def remove_item(dictionary, key):
    result_dict = dict(dictionary)

    if key in result_dict:
        # result_dict.pop(key)
        del result_dict[key]
    else:
        return 'Key not found'

    return result_dict


test = {1: 'one', 2: 'two'}
print(remove_item(test, 1))
print(test)