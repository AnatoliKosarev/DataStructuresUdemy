def product_of_array(arr):
    if len(arr) == 0:
        return 1

    return arr.pop() * product_of_array(arr)


print(product_of_array([1, 2, 3, 10]))