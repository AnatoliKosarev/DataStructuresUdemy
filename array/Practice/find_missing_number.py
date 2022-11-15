def find_missing_number(myList, totalCount):
    expected_sum = totalCount * (totalCount + 1) / 2
    actual_sum = sum(myList)

    return expected_sum - actual_sum


print(find_missing_number([1, 2, 3, 4, 6], 6))
