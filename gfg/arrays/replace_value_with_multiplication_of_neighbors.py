"""
Given an array of integers, update every element with multiplication
of previous and next elements with following exceptions. 
    a) First element is replaced by multiplication of first and second.
    b) Last element is replaced by multiplication of last and second last.
"""


def replace(arr: list) -> list:
    if len(arr) < 2:
        return arr

    prev: int = arr[0]
    arr[0] *= arr[1]

    for i in range(1, len(arr) - 1):
        prev, arr[i] = arr[i], prev * arr[i + 1]

    arr[-1] *= prev
    return arr


if __name__ == "__main__":
    assert replace([2, 3, 4, 5, 6]) == [6, 8, 15, 24, 30]
