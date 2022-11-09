def calculate_power_of(base, exp):
    assert isinstance(exp, int) and exp >= 0, 'Exponent must be a positive integer only!'

    if base == 0:
        return 0

    if exp == 0:
        return 1

    return base * calculate_power_of(base, exp - 1)


print(calculate_power_of(4, 4))
