"""
Search an element in a sorted and rotated array
"""


def get_first_position(arr: list, start: int, end: int) -> int:
    if arr[start] <= arr[end]:
        return start

    while start <= end:
        mid = start + int((end - start) / 2)

        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid + 1
        if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
            return mid
        elif arr[mid] > arr[0]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def bin_search(arr: list, start: int, end: int, k: int) -> int:
    while start <= end:
        mid = start + int((end - start) / 2)

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def rotated_bin_search(arr: list, k: int) -> int:
    """
    Find the starting point.
    Depending on the value of k, search in first or second half
    Time complexity: O(log(n))
    """
    start, end = 0, len(arr) - 1
    first = get_first_position(arr, start, end)

    if k > arr[-1]:
        end = first - 1
    else:
        start = first

    return bin_search(arr, start, end, k)


if __name__ == "__main__":
    print(rotated_bin_search([5, 6, 7, 8, 9, 10, 1, 2, 3], 3))
    print(rotated_bin_search([5, 6, 7, 8, 9, 10, 1, 2, 3], 30))
    print(rotated_bin_search([30, 40, 50, 10, 20], 10))
