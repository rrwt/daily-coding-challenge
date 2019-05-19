"""
Write code to remove duplicates from an unsorted linked list
How would you solve this problem if a temporary buffer is not allowed?
"""


def remove_duplicates(llist):
    """
    time complexity: O(n)
    space complexity: O(n)
    return set(llist)  # array
    """
    s = set()
    i = 0

    while i < len(llist):  # len() is O(1)
        if llist[i] in s:
            del llist[i]
        else:
            s.add(llist[i])
            i += 1

    return llist


def remove_duplicates_without_buffer(llist):
    """
    time complexity: O(n*n)
    space complexity: O(1)
    """
    i = 0
    while i < len(llist):
        j = i + 1

        while j < len(llist):
            if llist[j] == llist[i]:
                del llist[j]
            else:
                j += 1

        i += 1

    return llist


if __name__ == "__main__":
    llist = [1, 5, 1, 1, 2, 3, 5, 2, 5, 3, 2]
    print(llist)
    print(remove_duplicates(llist))
    print(remove_duplicates_without_buffer(llist))
