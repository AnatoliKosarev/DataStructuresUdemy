def find_pair_sum(arr, n):
    result_list = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  # for previous (before i) do not count, because for them sum was already checked
            if arr[i] + arr[j] == n:
                result_list.append((i, j))

    return ', '.join(str(r) for r in result_list)


test = [1, 2, 5, 4, 7]
print(find_pair_sum(test, 6))
