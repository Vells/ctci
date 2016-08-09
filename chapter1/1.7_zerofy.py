"""
Problem 1.7: Write an algorithm such that
if an element in an M x N matrix id 0,
its entire row and column are set to 0.
Do it in place!
"""


def nullify_row(matrix, row):
    for col, _ in enumerate(matrix[0]):
        matrix[row][col] = 0


def nullify_col(matrix, col):
    for row, _ in enumerate(matrix):
        matrix[row][col] = 0


def nullify_matrix(matrix):
    """
    Space complexity: O(1)
    Time complexity: O(n ^ 2)
    """

    if len(matrix) < 1:
        return

    row_num = len(matrix)
    col_num = len(matrix[0])
    nullify_first_row = True if 0 in matrix[0] else False
    nullify_first_col = False

    for row in matrix:
        if row[0] == 0:
            nullify_first_col = True

    for row in range(1, row_num):
        for col in range(1, col_num):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0

    for col in range(1, col_num):
        if matrix[0][col] == 0:
            nullify_col(matrix, col)

    for row in range(1, row_num):
        if matrix[row][0] == 0:
            nullify_row(matrix, row)

    if nullify_first_row:
        nullify_row(matrix, 0)
    if nullify_first_col:
        nullify_col(matrix, 0)


matrix_a = [
    [0, 0, 2],
    [3, 4, 5],
    [6, 1, 1]
]
print matrix_a
nullify_matrix(matrix_a)
print matrix_a
