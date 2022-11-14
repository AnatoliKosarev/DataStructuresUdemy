import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)


print('Inserting row')
print('=========================================')
matrix_with_added_row = np.insert(matrix, 0, [[100, 101, 102]], axis=0)
print(matrix_with_added_row)
print(matrix)

matrix_with_added_row = np.insert(matrix_with_added_row, 1, [[110, 111, 112]], axis=0)
print(matrix_with_added_row)

# adds to the end
matrix_with_added_row = np.append(matrix_with_added_row, [[120, 121, 122]], axis=0)
print(matrix_with_added_row)


print('Inserting column')
print('=========================================')
matrix_with_added_col = np.insert(matrix, 0, [[100, 101, 102]], axis=1)
print(matrix_with_added_col)
print(matrix)

matrix_with_added_col = np.insert(matrix_with_added_col, len(matrix_with_added_col[0]), [[110, 111, 112]], axis=1)
print(matrix_with_added_col)

# adds to the end
matrix_with_added_col = np.append(matrix_with_added_col, [[120], [121], [122]], axis=1)
print(matrix_with_added_col)


print('Accessing matrix element')
print('=========================================')
def access_matrix_element(matrix, row_index, column_index):
    if row_index >= len(matrix) or column_index >= len(matrix[0]):
        return 'Index out bounds'

    return matrix[row_index][column_index]


matrix_access = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_access)
print(access_matrix_element(matrix_access, 2, 1))


print('Deletin row / column')
print('=========================================')
print(matrix)

matrix_delete_row = np.delete(matrix, 0, axis=0)
print(matrix_delete_row)

matrix_delete_col = np.delete(matrix, -1, axis=1)  # deletes last column
print(matrix_delete_col)