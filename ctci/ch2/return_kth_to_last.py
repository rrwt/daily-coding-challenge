"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""


def kth_to_last_element(llist: list, k: int) -> int:
    """
    O(n) & O(1)
    Steps:
        1. find length of linked list.
        2. move first pointer k steps ahead
        3. move second and first pointer until first pointer becomes none
        4. return the data at second pointer
    """
    l: int = len(llist)

    if l < k:
        return -1

    i: int = k
    j: int = 0

    while i < l:
        i += 1
        j += 1

    return llist[j]


if __name__ == "__main__":
    llist: list = [7, 6, 5, 4, 3, 2, 1]
    print(llist)
    assert kth_to_last_element(llist, 3) == 3
