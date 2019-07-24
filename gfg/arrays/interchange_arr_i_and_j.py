"""
Given an array of size n where all elements are distinct and in range from 0 to n-1,
change contents of arr[] so that arr[i] = j is changed to arr[j] = i.
"""


def rearrange(arr: list) -> list:
    """
    Simplest approach would be to create and fill a temp array.
    But it would require extra space.
    In case there is only one cycle (test case 1), it is easy to do it
    in one loop.
    In case of multiple cycles(test case 2), the solution becomes more convulated
    We can convert the processed values as -ve of the values and use some special value for 0.
    We can also increment the values by 1 and save as -ve...
    Afterwards we revert them

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    l, i = len(arr), 0

    while i < l:  # let's use -l for 0
        if arr[i] >= 0:  # unprocessed
            j = arr[i]
            k = i

            while j != i:
                temp = arr[j]
                arr[j] = -(k if k != 0 else l)
                j, k = temp, j

            arr[i] = -(k if k != 0 else l)
        i += 1

    for i in range(l):
        arr[i] = -arr[i] % l

    return arr


if __name__ == "__main__":
    assert rearrange([1, 3, 0, 2]) == [2, 0, 3, 1]
    assert rearrange([2, 0, 1, 4, 5, 3]) == [1, 2, 0, 5, 3, 4]
