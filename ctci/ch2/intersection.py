"""
Given two (singly) linked lists, determine if the two lists intersect.
Return the inter­secting node. Note that the intersection is defined based
on reference, not value. That is, if the kth node of the first linked list
is the exact same node (by reference) as the jth node of the second linked
list, then they are intersecting.
"""
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
            return True
        h = h.next

    return False


if __name__ == "__main__":
    ll1: LinkedList = LinkedList(Node(1))
    ll1.push(Node(3)).push(Node(5))
    node = Node(7)
    node.next = Node(9)
    node.next.next = Node(11)

    ll2: LinkedList = LinkedList(Node(2))
    ll2.head.next = node
    ll1.head.next.next.next = node

    assert intersect(ll1, ll2) == True

    ll3: LinkedList = LinkedList(Node(11))
    ll3.push(13).push(15).push(17)

    assert intersect(ll1, ll3) == False
    assert intersect(ll2, ll3) == False
