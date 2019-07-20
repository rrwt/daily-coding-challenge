"""
Rotate an array of size n by d positions
"""
from array import array


def gcd(a: int, b: int) -> int:
    """
    Eucledian Algorithm to calculate gcd of two integers
    """
    while b:
        a, b = b, a % b

    return a


def rotate(arr: array, n: int, d: int) -> array:
    """
    Calculate gcd of n and d.
    use gcd of n and d to make array elements jump that many positions.
    Time Complexity: O(n)  # excluding the gcd calculation
    Space Complexity: O(1)
    """
    cd = gcd(n, d)

    for i in range(cd):
        t = arr[i]
        j = i

        while True:
            k = j + d
            if k >= n:
                k -= n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = t

    return arr


def reverse_array(arr: array, start: int, end: int) -> array:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


def rotate_using_reversal_algorithm(arr: array, n: int, d: int) -> array:
    return reverse_array(
        reverse_array(reverse_array(arr, 0, d - 1), d, n - 1), 0, n - 1
    )


if __name__ == "__main__":
    n: int = 20

    for d in range(1, 5):
        print(rotate(array("B", list(range(20))), n, d))
        print(rotate_using_reversal_algorithm(array("B", list(range(20))), n, d))
