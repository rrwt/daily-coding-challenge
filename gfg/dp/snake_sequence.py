"""
Given a grid of numbers, find maximum length Snake sequence and print it.
If multiple snake sequences exists with the maximum length, print any one of them.
A snake sequence is made up of adjacent numbers in the grid such that for each number,
the number on the right or the number below it is +1 or -1 its value.
For example,
    if you are at location (x, y) in the grid, you can either move right i.e. (x, y+1)
    if that number is ± 1 or move down i.e. (x+1, y) if that number is ± 1.
"""


def get_path(matrix: list, dp: list, max_h: int, max_w: int) -> list:
    path = []

    while max_h >= 0 and max_w >= 0:
        path.append(matrix[max_h][max_w])

        if max_h > 0 and dp[max_h][max_w] - dp[max_h - 1][max_w] == 1:
            max_h -= 1
        elif max_w > 0 and dp[max_h][max_w] - dp[max_h][max_w - 1] == 1:
            max_w -= 1
        else:
            break

    return path[::-1]


def snake_sequence(matrix: list) -> list:
    height = len(matrix)
    width = len(matrix[0])

    dp = [[0] * width for _ in range(height)]
    max_val, max_h, max_w = 0, 0, 0

    for h in range(height):
        for w in range(width):
            if h == 0:
                dp[h][w] = dp[h][w - 1] + 1 if w else 0
            elif w == 0:
                dp[h][w] = dp[h - 1][w] + 1
            else:
                if abs(matrix[h][w] - matrix[h - 1][w]) == 1:
                    dp[h][w] = dp[h - 1][w] + 1
                if abs(matrix[h][w] - matrix[h][w - 1]) == 1:
                    dp[h][w] = max(dp[h][w], 1 + dp[h][w - 1])

            if dp[h][w] > max_val:
                max_val = dp[h][w]
                max_h = h
                max_w = w

    return get_path(matrix, dp, max_h, max_w)


if __name__ == "__main__":
    print(snake_sequence([[9, 6, 5, 2], [8, 7, 6, 5], [7, 3, 1, 6], [1, 1, 1, 7]]))
