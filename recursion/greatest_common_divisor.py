def find_greatest_common_divisor(a, b):
    assert isinstance(a, int) and isinstance(b, int), 'Input numbers must be integers only !'
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)

    if b == 0:
        return a

    d = a % b
    result = find_greatest_common_divisor(b, a % b)

    return result


print(find_greatest_common_divisor(48, 18))
