def fibonacci(index, result_list=None):
    assert isinstance(index, int) and index >= 0, 'Input index must be a positive int or 0 only!'

    if result_list is None:
        result_list = [0, 1]

    if len(result_list) - 1 >= index:
        return result_list[index]

    if index <= 1:
        return result_list[index]

    result = fibonacci(index-1, result_list) + fibonacci(index-2, result_list)
    result_list.append(result)

    return result


print(fibonacci(100))
