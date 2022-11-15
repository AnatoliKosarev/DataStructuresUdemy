# checks that lists contain the same elements
def lists_permutations(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    arr1.sort()
    arr2.sort()

    if arr1 != arr2:
        return False

    return True


test1 = [1, 3, 2, 5]
test2 = [5, 2, 1, 3]
print(lists_permutations(test1, test2))
