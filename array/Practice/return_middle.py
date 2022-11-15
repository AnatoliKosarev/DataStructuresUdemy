def return_middle(arr):
    # arr.pop()
    # arr.pop(0)

    arr = arr[1:-1]

    # del arr[0]
    # del arr[-1]

    return arr


test = [1, 2, 3, 4]
print(return_middle(test))