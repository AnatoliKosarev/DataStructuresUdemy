def find_sum_pairs(myList, sum):
    result_list = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                result_list.append(f'{myList[i]}+{myList[j]}')

    return result_list


print(find_sum_pairs([2, 4, 3, 5, 6, -2, 4, 7, 8, 9, 0],7))
