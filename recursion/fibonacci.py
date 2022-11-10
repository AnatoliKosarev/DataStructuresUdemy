def fib(index, result_list=None):
    assert isinstance(index, int) and index >= 0, 'Input index must be a positive int or 0 only!'

    if result_list is None:
        result_list = [0, 1]

    if len(result_list) - 1 >= index:
        return result_list[index]

    if index <= 1:
        return index

    result = fib(index-1, result_list) + fib(index-2, result_list)
    result_list.append(result)

    return result

# def fib(num):
#     assert isinstance(num, int) and num >= 0, 'Num must be a positive integer'
#
#     result_list = [0, 1]
#
#     if num <= 1:
#         return num
#
#     for i in range(2, num + 1):
#         result = result_list[i - 1] + result_list[i - 2]
#         result_list.append(result)
#
#     return result_list[num]


print(fib(100))
