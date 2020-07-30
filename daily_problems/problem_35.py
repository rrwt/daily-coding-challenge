"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array
so that all the Rs come first, the Gs come second, and the Bs come last.
You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
from array import array


def segregate_rgb(input_arr: array) -> array:
    """
    Have 3 pointers, each tracking one code.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    r, g, b = 0, 0, len(input_arr) - 1

    while g <= b:
        if input_arr[g] == "R":
            input_arr[g], input_arr[r] = input_arr[r], input_arr[g]
            r += 1
            g += 1
        elif input_arr[g] == "B":
            input_arr[g], input_arr[b] = input_arr[b], input_arr[g]
            b -= 1
        else:
            g += 1

    return input_arr


if __name__ == "__main__":
    arr: array = array("u", ["G", "B", "R", "R", "B", "R", "G", "R"])
    assert segregate_rgb(arr) == array("u", ["R", "R", "R", "R", "G", "G", "B", "B"])

    arr: array = array("u", ["R", "G", "G", "R", "G", "B", "G", "B", "R", "R", "R", "G"])
    assert segregate_rgb(arr) == array("u", ["R", "R", "R", "R", "R", "G", "G", "G", "G",
                                       "G", "B", "B"])
