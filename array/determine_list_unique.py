# def list_contains_unique_elements(arr):
#     arr.sort()
#
#     for i in range(1, len(arr)):
#         if arr[i] == arr[i - 1]:
#             print(arr[i])
#             return False
#
#     return True

def list_contains_unique_elements(arr):
    if len(set(arr)) != len(arr):
        return False

    return True


test = [10, 1, 2, 3, 13, 4, 5, 10]
print(list_contains_unique_elements(test))
