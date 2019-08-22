"""
You have given an array which contain 1 to n element, your task is to sort
this array in an efficient way and without replace with 1 to n numbers.
"""


def sort_n(arr: list) -> list:
    for i in range(len(arr)):
        x = arr[i]
        while x != arr[x - 1]:
            arr[x - 1], x = x, arr[x - 1]

    return arr


if __name__ == "__main__":
    print(sort_n([10, 7, 9, 2, 8, 3, 5, 4, 6, 1]))
