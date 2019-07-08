"""
Counting Sort: A sorting algorithm that sorts n elements, all of them occurring in
    a range k. The complexity increases or decreases based on the value of k.
    In case one or more of the integer is -ve, add abs(min) value to all.
    In case all the elements are greater than 0, subtract the min value from all.
Time Complexity: O(n+k)
Space Complexity: O(n+k)
Stable: Yes
Inplace: No
"""


def counting_sort(arr: list) -> list:
    """
    Create a count array of k elements.
    In count array store the running sum of all the elements upto current.
    Traverse the original array and store the element at their position,
    while decreasing the count.
    The count array at any point gives the last position of the element it contains
    """
    min_el = max_el = arr[0]
    length: int = len(arr)

    for el in arr:
        if el < min_el:
            min_el = el
        if el > max_el:
            max_el = el

    k = max_el - min_el + 1
    count_arr = [0] * k

    for i in range(length):
        count_arr[arr[i] - min_el] += 1

    for i in range(1, k):  # running sum of counts
        count_arr[i] += count_arr[i - 1]

    res = [None] * length

    for el in arr[::-1]:
        # reversing is important for stability (here it doesn't matter)
        res[count_arr[el - min_el] - 1] = el
        count_arr[el - min_el] -= 1

    return res


if __name__ == "__main__":
    arr1 = [1, 4, 1, 2, 7, 5, 2]
    print(arr1, counting_sort(arr1), sep="->")
    arr2 = [-5, -10, 0, -3, 8, 5, -1, 10]
    print(arr2, counting_sort(arr2), sep="->")
