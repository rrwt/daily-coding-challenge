"""
Given an array of elements of length N, ranging from 0 to N – 1.
All elements may not be present in the array. If element is not
present then there will be -1 present in the array.
Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.
"""


def rearrange(arr: list) -> list:
    l: int = len(arr)
    i: int = 0

    while i < l:
        while arr[i] not in (i, -1):
            # keep placing the current value to it's proper place
            x = arr[i]
            arr[i], arr[x] = arr[x], arr[i]

        i += 1
    return arr


if __name__ == "__main__":
    print(rearrange([-1, -1, 6, 1, 9, 3, 2, 0, 4, -1]))
    print(
        rearrange(
            [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
        )
    )
