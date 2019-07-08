"""
Radix Sort: If all the elements are in range 1 - n*n, then radix sort can
    provide linear time complexity.
Time Complexity: O(d*(n+b)) where b = base of numbers. For linear time b = n
Space Complexity: O(n+k)
Inplace: No
Stable: Yes
"""


def counting_sort(arr: list, exp: int, base: int = 10) -> None:
    """
    Modified counting sort, where k = base
    """
    length = len(arr)
    output = [None] * length
    count_arr = [0] * base

    for el in arr:
        index = el // exp
        count_arr[index % base] += 1

    for i in range(1, 10):
        count_arr[i] += count_arr[i - 1]

    for el in arr[::-1]:
        index = el // exp
        output[count_arr[index % base] - 1] = el
        count_arr[index % base] -= 1

    return output


def radix_sort(arr: list):
    exp = 1
    largest_element: int = max(arr)

    while int(largest_element / exp) > 0:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr


if __name__ == "__main__":
    print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
