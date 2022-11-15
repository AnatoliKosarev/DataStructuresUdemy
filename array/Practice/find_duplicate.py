def find_duplicate(myList):
    myList.sort()
    result = []

    for i in range(1, len(myList)):
        if myList[i] == myList[i - 1]:
            result.append(myList[i])

    return result


print(find_duplicate([1, 1, 2, 2, 3, 4, 5]))