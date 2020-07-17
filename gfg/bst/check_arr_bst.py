"""
Check given array of size n can represent BST of n levels or not
"""
import math


def is_bst(values: list) -> bool:
    """
    time complexity: O(n)
    space complexity: O(1)

    iterate the array one by one and verify it is in the range(min_, max_)
    """
    min_ = -math.pow(2, 64)
    max_ = math.pow(2, 64)

    for i, el in enumerate(values[:-1]):
        if not min_ < el < max_:
            return False
        elif values[i + 1] < el:
            max_ = el
        else:
            min_ = el

    return True


if __name__ == "__main__":
    arr = [500, 200, 90, 250, 100]
    print(arr, is_bst(arr))
    arr = [5123, 3300, 783, 1111, 890]
    print(arr, is_bst(arr))
