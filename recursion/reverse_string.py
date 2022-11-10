def reverse(strng):
    assert isinstance(strng, str), 'Input value must be a string'

    if len(strng) == 1:
        return strng

    return strng[-1:] + reverse(strng[:-1])


print(reverse('123'))