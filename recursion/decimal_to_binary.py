def decimal_to_binary(n):
    assert isinstance(n, int), 'Number must be an integer only'

    if n == 0:
        return 0

    a = n % 2
    b = decimal_to_binary(int(n / 2))
    result = a + 10 * b

    return result


print(decimal_to_binary(10))
