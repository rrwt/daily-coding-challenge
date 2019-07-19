"""
Given two singly linked lists that intersect at some point, find the intersecting node.
The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_count(head):
    count = 0

    while head:
        head = head.next
        count += 1

    return count


def intersecting_point(ll1: Node, ll2: Node) -> int:
    """
    Time complexity: O(m+n)
    """
    head1, head2 = ll1, ll2
    count_1 = get_count(head1)
    count_2 = get_count(head2)

    while count_1 > count_2:
        ll1 = ll1.next
    while count_2 > count_1:
        ll2 = ll2.next

    while ll1 and ll2:
        if ll1 == ll2:
            return ll1.data
        ll1 = ll1.next
        ll2 = ll2.next

    return -1


if __name__ == "__main__":
    ll1: Node = Node(3)
    ll1.next = Node(7)
    ll1.next.next = Node(8)
    ll1.next.next.next = Node(10)

    ll2: Node = Node(99)
    ll2.next = Node(1)
    ll2.next.next = ll1.next.next

    print("intersecting point:", intersecting_point(ll1, ll2))