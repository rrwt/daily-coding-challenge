"""Counting Sort
A sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind of hashing). 
"""


def counting_sort(arr: list) -> list:
    first, last = min(arr), max(arr)
    count_arr: list = [0] * (last - first + 1)

    for integer in arr:
        count_arr[integer - first] += 1

    for index in range(1, len(count_arr)):
        count_arr[index] += count_arr[index - 1]

    res_arr: list = [0] * len(arr)

    for integer in arr:
        res_arr[count_arr[integer - first] - 1] = integer
        count_arr[integer - first] -= 1

    return res_arr


def counting_sort_str(string: str) -> str:
    arr: list = [0] * len(string)

    for index, char in enumerate(string):
        arr[index] = ord(char)

    sorted_arr = [chr(integer) for integer in counting_sort(arr)]
    return "".join(sorted_arr)


if __name__ == "__main__":
    print(*counting_sort([-5, -3, -1, 0, 1, 4, 1, 2, 7, 5, 2]))
    print(counting_sort_str("geeksforgeeks"))
