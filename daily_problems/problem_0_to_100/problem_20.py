"""
Given two singly linked lists that intersect at some point, find the intersecting node.
The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


def get_count(head):
    count = 0

    while head:
        head = head.next
        count += 1

    return count


def intersecting_point(linked_list_1: Node, linked_list_2: Node) -> int:
    """
    Time complexity: O(m+n)
    """
    head1, head2 = linked_list_1, linked_list_2
    count_1 = get_count(head1)
    count_2 = get_count(head2)

    while count_1 > count_2:
        linked_list_1 = linked_list_1.next
        count_1 -= 1
    while count_2 > count_1:
        linked_list_2 = linked_list_2.next
        count_2 -= 1

    while linked_list_1 and linked_list_2:
        if linked_list_1 == linked_list_2:
            return linked_list_1.data
        linked_list_1 = linked_list_1.next
        linked_list_2 = linked_list_2.next

    return -1


if __name__ == "__main__":
    ll1: Node = Node(3)
    ll1.next = Node(7)
    ll1.next.next = Node(8)
    ll1.next.next.next = Node(10)

    ll2: Node = Node(99)
    ll2.next = Node(1)
    ll2.next.next = Node(2)
    ll2.next.next.next = ll1.next

    print("intersecting point:", intersecting_point(ll1, ll2))
