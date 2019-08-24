"""
Given a matrix, clockwise rotate elements in it.
"""


def print_matrix(matrix: list) -> None:
    for i in range(len(matrix)):
        print(matrix[i])


def rotate_clockwise(matrix: list) -> None:
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top < bottom and left < right:
        elem = matrix[top + 1][left]

        for i in range(left, right + 1):
            curr = matrix[top][i]
            matrix[top][i] = elem
            elem = curr

        top += 1

        for i in range(top, bottom + 1):
            curr = matrix[i][right]
            matrix[i][right] = elem
            elem = curr

        right -= 1

        for i in range(right, left - 1, -1):
            curr = matrix[bottom][i]
            matrix[bottom][i] = elem
            elem = curr

        bottom -= 1

        for i in range(bottom, top - 1, -1):
            curr = matrix[i][left]
            matrix[i][left] = elem
            elem = curr

        left += 1

    print_matrix(matrix)


if __name__ == "__main__":
    mat_list: list = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    ]

    for mat in mat_list:
        print("Input")
        print_matrix(mat)
        print("output")
        rotate_clockwise(mat)
