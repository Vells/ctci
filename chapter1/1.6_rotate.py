"""
Problem 1.6: Given an image represented by an N x N matrix, where
each pixel in the image is 4 bytes, write a method to rotate the
image by 90 degrees. Do this in place.
"""


def rotate_matrix(matrix):
    """
    Time complexity: O(n^2)
    """

    matrix_size = len(matrix)

    for layer in range(matrix_size / 2):
        for index in range(layer, matrix_size - 1 - layer):
            top_left = matrix[layer][index]
            top_right = matrix[index][matrix_size - 1 - layer]
            bottom_left = matrix[matrix_size - 1 - index][layer]
            bottom_right = matrix[matrix_size - 1 - layer][matrix_size - 1 - index]

            matrix[layer][index] = bottom_left
            matrix[index][matrix_size - 1 - layer] = top_left
            matrix[matrix_size - 1 - layer][matrix_size - 1 - index] = top_right
            matrix[matrix_size - 1 - index][layer] = bottom_right


matrix_a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix_b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print "Before: ", matrix_a
rotate_matrix(matrix_a)
print "After: ", matrix_a
print
print "Before: ", matrix_b
rotate_matrix(matrix_b)
print "After: ", matrix_b
