"""
Given two (singly) linked lists, determine if the two lists intersect.
Return the inter­secting node. Note that the intersection is defined based
on reference, not value. That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the second linked
list, then they are intersecting.
"""
from typing import Optional

from list_structure import LinkedList, Node


def intersect(ll1: LinkedList, ll2: LinkedList) -> bool:
    """
    A simple solution would be O(n*n), where we try and match every node of first
    list to every node of second list.
    Another one would be to create a set of nodes of first list and find if a node
    of second list is in the hash.
    time complexity: O(n+m)
    space complexity: O(n)
    """
    s: set = set()

    h: Node = ll1.head

    while h:
        s.add(h)
        h = h.next

    h: Node = ll2.head

    while h:
        if h in s:
            return h  # return the intersecting node
        h = h.next

    return False


def get_loop(ll: LinkedList) -> (bool, Optional[Node]):
    """
    Return the loop node and if there is a loop. Floyd's algorithm
    Note: Cannot find the length by counting the number of nodes untill None
    """
    slow: Node = ll.head
    fast: Node = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            break

    if not fast:
        return False, None

    """
    If we reinitialize the slow pointer and both pointers move at the
    same pace(slow), the intersection is found at the point they meet.
    """
    slow = ll.head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return True, slow


def intersect_without_extra_space(ll1: LinkedList, ll2: LinkedList) -> bool:
    """
    Assumption, end parts of the joined linkedlists is same (singly linked list).
    Solution: Make first list circular. Detect circle in the second list.
    If there is a circle, it means they intersect; otherwise no.
    Remove the circle from the first list.
    time complexity: O(n+m)
    extra space complexity: O(1)
    """
    h1: Node = ll1.head

    while h1.next:
        h1 = h1.next

    h1.next = ll1.head

    has_loop, node = get_loop(ll2)

    h1.next = None

    return node or has_loop


if __name__ == "__main__":
    ll1: LinkedList = LinkedList(Node(1))
    ll1.push(Node(3)).push(Node(5))
    node = Node(7)
    node.next = Node(9)
    node.next.next = Node(11)

    ll2: LinkedList = LinkedList(Node(2))
    ll2.head.next = node
    ll1.head.next.next.next = node

    node = intersect(ll1, ll2)
    print('intersecting node is', node.data, sep=' ')

    ll3: LinkedList = LinkedList(Node(11))
    ll3.push(13).push(15).push(17)

    assert intersect(ll1, ll3) == False
    assert intersect(ll2, ll3) == False

    node = intersect_without_extra_space(ll1, ll2)
    print('interseting node is', node.data, sep=' ')

    assert intersect_without_extra_space(ll1, ll3) == False
    assert intersect_without_extra_space(ll2, ll3) == False
