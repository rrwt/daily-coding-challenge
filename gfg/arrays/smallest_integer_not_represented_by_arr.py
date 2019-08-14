"""
Given a sorted array (sorted in non-decreasing order) of positive numbers,
find the smallest positive integer value that cannot be represented as sum
of elements of any subset of given set. 
"""


def smallest_integer(arr: list) -> int:
    """
    Time Complexity: O(n)
    If 1 is not the first element, then answer is 1.
    2nd element onwards, if the next element is <= current number being checked, then
    increment the number being checked by that number, else we found the result.
    Reason:
        adding k to a series of numbers will increment the current possible range by k.
        We can already create every number from 1 to current number being checked-1,
        Now we just need to check the rest (curr_sum + k onwards).
    """
    res: int = 1

    for element in arr:
        if element <= res:
            res += element
        else:
            break

    return res


if __name__ == "__main__":
    assert smallest_integer([1, 2, 4, 5]) == 13
    assert smallest_integer([1, 3, 4, 5]) == 2
    assert smallest_integer([1, 2, 6, 10, 11, 15]) == 4
    assert smallest_integer([1, 1, 1, 1]) == 5
    assert smallest_integer([1, 1, 3, 4]) == 10
