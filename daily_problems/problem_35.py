"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array
so that all the Rs come first, the Gs come second, and the Bs come last.
You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
from array import array


def segregate_rgb(arr: array) -> array:
    """
    Have 3 pointers, each tracking one code.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    r: int = 0
    b: int = len(arr) - 1

    while r < b and arr[r] == "R":
        r += 1
    while b > r and arr[b] == "B":
        b -= 1
    g = r

    while g <= b:
        if arr[g] == "R":
            arr[g], arr[r] = arr[r], arr[g]
            r += 1
        elif arr[g] == "B":
            arr[g], arr[b] = arr[b], arr[g]
            b -= 1
        else:
            g += 1

    return arr


if __name__ == "__main__":
    arr: array = array("u", ["G", "B", "R", "R", "B", "R", "G", "R"])
    assert segregate_rgb(arr) == array("u", ["R", "R", "R", "R", "G", "G", "B", "B"])
