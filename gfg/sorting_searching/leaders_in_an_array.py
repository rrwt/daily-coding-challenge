"""
Write a program to print all the LEADERS in the array. An element is leader
if it is greater than all the elements to its right side. And the rightmost
element is always a leader. For example int the array {16, 17, 4, 3, 5, 2},
leaders are 17, 5 and 2.
"""


def leaders(arr: list) -> list:
    """
    Time Complexity: O(n)
    """
    leader_list: list = [arr[-1]]

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > leader_list[-1]:
            leader_list.append(arr[i])

    return list(reversed(leader_list))


if __name__ == "__main__":
    print(leaders([16, 17, 4, 3, 5, 2]))
