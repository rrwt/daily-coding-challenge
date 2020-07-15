"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:
1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
"""


def print_matrix(matrix: list) -> None:
    i, j, x, y = 0, 0, len(matrix), len(matrix[0])

    while i < x and j < y:
        for k in range(j, y):
            print(matrix[i][k])
        i += 1

        for k in range(i, x):
            print(matrix[k][y - 1])
        y -= 1

        if i < x:
            for k in range(y - 1, j - 1, -1):
                print(matrix[x - 1][k])
            x -= 1

        if j < y:
            for k in range(x - 1, i - 1, -1):
                print(matrix[k][j])
            j += 1


if __name__ == "__main__":
    matrix: list = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    print_matrix(matrix)
