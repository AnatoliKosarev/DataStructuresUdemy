def get_first_second_best_score(arr):
    arr.sort(reverse=True)

    result = arr[:2]

    return result


my_list = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(get_first_second_best_score(my_list))