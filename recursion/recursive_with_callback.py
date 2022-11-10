def is_odd(num):
    if num % 2 == 0:
        return False

    return True


def recursive_with_callback(arr, cb):
    if len(arr) == 0:
        return False

    if cb(arr.pop()):
        return True

    return recursive_with_callback(arr, cb)


print(recursive_with_callback([8,2,4], is_odd))