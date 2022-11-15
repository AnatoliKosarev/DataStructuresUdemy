import numpy as np


# def count_matrix_diagonal_sum(matrix):
#     matrix = np.array(matrix)
#     shape = matrix.shape
#     if shape[0] != shape[1]:
#         return 'Matrix should be square'
#
#     index = list(range(len(matrix)))
#     value_arr = matrix[[index], [index]]
#
#     return sum(*value_arr)


def count_matrix_diagonal_sum(matrix):
    result = 0

    for i in range(len(matrix)):
        result += matrix[i][i]

    return result


myList2D = [[1,2,3],[4,5,6],[7,8,9]]
print(count_matrix_diagonal_sum(myList2D))
