import numpy as np


def rotate_matrix_by_ninety_degrees_clockwise(matrix):
    matrix = matrix.T

    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]  # iterating over matrix rows reversing their values

    return matrix


def rotate_matrix_by_ninety_degrees_counterclockwise(matrix):
    matrix = matrix.T

    for i in range(len(matrix[0])):
        matrix[:, i] = matrix[:, i][::-1]  # iterating over matrix columns reversing their values

    return matrix


mat1 = np.arange(1, 10)
mat1 = mat1.reshape(3, 3)
print(mat1)

print(rotate_matrix_by_ninety_degrees_counterclockwise(mat1))