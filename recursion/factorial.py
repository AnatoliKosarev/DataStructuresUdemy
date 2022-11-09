def factorial(n):
    assert isinstance(n, int) and n >= 0, 'Input value must be a positive integer or 0 only!'

    if n in [0, 1]:
        return 1

    return n * factorial(n-1)


print(factorial(10))
