"""
There are two sorted arrays. First one is of size m+n containing only m elements.
Another one is of size n and contains n elements. Merge these two arrays into the
first array of size m+n such that the output is sorted.
"""


def move_to_end(arr: list, m: int) -> None:
    """
    Move all elements to end
    """
    j, k = m - 1, m - 1

    while k >= 0:
        while arr[k] is None:
            k -= 1

        arr[j] = arr[k]
        j -= 1
        k -= 1


def merge(arrn: list, arrm: list) -> list:
    i, n, m = 0, len(arrn), len(arrm)
    j, k = n, 0

    move_to_end(arrm, m)

    while i < n and j < m:
        if arrn[i] < arrm[j]:
            arrm[k] = arrn[i]
            i += 1
        else:
            arrm[k] = arrm[j]
            j += 1
        k += 1

    while i < n:
        arrm[k] = arrn[i]
        k += 1
        i += 1

    return arrm


if __name__ == "__main__":
    arrm = [2, 8, None, None, None, 13, None, 15, 20]
    arrn = [5, 7, 9, 25]
    print(merge(arrn, arrm))
