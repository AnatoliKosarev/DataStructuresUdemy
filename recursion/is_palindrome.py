def is_palindrome(word):
    assert isinstance(word, str), 'Input value must be a string'

    if len(word) <= 1:
        return True

    if word[:1] != word[-1:]:
        return False

    return is_palindrome(word[1:-1])


print(is_palindrome('amanaplanacanappanama'))
