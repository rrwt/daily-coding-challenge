"""
There are 2 sorted arrays A and B of size n each. Write an algorithm to find the
median of the array obtained after merging the above 2 arrays(i.e. array of length 2n)
Time complexity: O(log(n))
"""
from typing import Union


def median(arr: list, n: int) -> int:
    if n % 2 == 0:
        return (arr[int(n / 2)] + arr[int(n / 2) - 1]) / 2
    return arr[int(n / 2)]


def median_arrays(a: list, b: list, n: int) -> Union[int, float]:
    """
    1. Get median of both arrays m1, m2
    2. m1 == m2? -> return m1 as median
    3. m1 < m2? -> median is in m1:last and start:m2 range (depending on length)
    4. m1 > m2? -> median is in m2:last and start:m1 range
    5. number of elements = 1 in each array -> return average
    6. number of elements = 2 in each array -> return average of middle two
    """
    if n == 1:
        return (a[0] + b[0]) / 2

    if n == 2:
        if b[0] > a[0] and b[1] > a[1]:
            return (a[1] + b[0]) / 2
        elif a[0] > b[0] and a[1] > b[1]:
            return (a[0] + b[1]) / 2
        elif a[0] < b[0] and a[1] > b[1]:
            return median(b, 2)
        else:
            return median(a, 2)

    m1 = median(a, n)
    m2 = median(b, n)

    if m1 == m2:
        return m1

    half = n // 2  # approx half
    if m1 > m2:
        if n % 2 == 0:
            return median_arrays(a[0: half + 1], b[half - 1:], half + 1)
        else:
            return median_arrays(a[0: half + 1], b[half:], half + 1)
    else:
        if n % 2 == 0:
            return median_arrays(a[half - 1:], b[0: half + 1], half + 1)
        else:
            return median_arrays(a[half:], b[0: half + 1], half + 1)


if __name__ == "__main__":
    arr1 = [1, 2, 3, 20, 25, 30]
    arr2 = [3, 5, 7, 9, 11, 13]
    print(arr1)
    print(arr2)
    print("median:", median_arrays(arr1, arr2, len(arr1)))
