def find_missing_el_in_list(input_list, n):
    expected_sum = n * (n + 1) / 2 # find expected sum of list with el from 1 to n if nothing missing
    act_sum = sum(input_list)

    return int(expected_sum - act_sum)


list_with_missing_el = [1, 2, 4, 5, 6, 7, 8, 9, 10]
print(find_missing_el_in_list(list_with_missing_el, 10))
