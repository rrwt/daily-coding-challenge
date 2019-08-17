"""
Sort an array in wave form
Given an unsorted array of integers, sort the array into a wave like array.
An array ‘arr[0..n-1]’ is sorted in wave form if
arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...
"""


def sort_in_wave(arr: list) -> list:
    l: int = len(arr)

    for i in range(l - 1):
        if i % 2 == 0:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


if __name__ == "__main__":
    arr_list: list = [[10, 5, 6, 3, 2, 20, 100, 80], [20, 10, 8, 6, 4, 2]]

    for arr in arr_list:
        print(sort_in_wave(arr))
