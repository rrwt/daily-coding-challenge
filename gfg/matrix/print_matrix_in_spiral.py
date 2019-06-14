"""
Write a program to print the contents of a matrix in a spiral order
"""


def print_matrix(matrix: list):
    y: int = len(matrix)
    x: int = len(matrix[0])
    a, b = 0, 0

    while a < x and b < y:
        for i in range(a, x):
            print(matrix[b][i], end=" ")

        b += 1

        for i in range(b, y):
            print(matrix[i][x - 1], end=" ")

        x -= 1

        if b < y:
            for i in range(x - 1, a - 1, -1):
                print(matrix[y - 1][i], end=" ")

            y -= 1

        if a < x:
            for i in range(y - 1, b - 1, -1):
                print(matrix[i][a], end=" ")

            a += 1

    print()


if __name__ == "__main__":
    print_matrix([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    print_matrix([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
