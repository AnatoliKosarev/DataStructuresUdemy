# def find_max_prod(arr):
#     max_prod = 0
#     res_message = ''
#
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             temp = arr[i] * arr[j]
#             if temp > max_prod:
#                 max_prod = temp
#                 res_message = f'Max prod of {arr[i]} * {arr[j]} = {max_prod}'
#
#     return res_message

def find_max_prod(arr):
    max_num_1 = arr.pop(arr.index(max(arr)))
    max_num_2 = arr.pop(arr.index(max(arr)))

    return f'Max prod of {max_num_1} * {max_num_2} = {max_num_1 * max_num_2}'


test = [9, 10, 2, 3, 40, 5]
print(find_max_prod(test))
