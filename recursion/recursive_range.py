def recursive_range(num):
    assert isinstance(num, int) and num >= 0, 'Num must be a positive integer'

    if num == 0:
        return 0

    return num + recursive_range(num-1)


print(recursive_range(10))