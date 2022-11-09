# returns the sum of digits of the input number, e.g. 12 -> 3
def sum_of_digits(number):
    assert isinstance(number, int) and number >= 0, 'Input number must be a positive integer !'

    if number == 0:
        return 0

    a = number % 10
    b = number//10

    result = number % 10 + sum_of_digits(number//10)

    return result


print(sum_of_digits(22234))
