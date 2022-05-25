"""
Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x. If x is contained
within the list, the values of x only need to be after the elements less than x.
The partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from typing import Optional

from list_structure import LinkedList, Node


def partition(ll: LinkedList, x: int) -> LinkedList:
    """
    strategy: create two different lists and merge them afterwards
    """
    before: Optional[LinkedList] = None
    after: Optional[Node] = None
    head: Optional[Node] = ll.head
    p_before: Optional[Node] = None
    p_after: Optional[Node] = None

    while head:
        h_next = head.next

        if head.data < x:
            if p_before:
                p_before.next = head
                p_before = p_before.next
            else:
                before = LinkedList(head)
                p_before = before.head
        else:
            if p_after:
                p_after.next = head
                p_after = p_after.next
            else:
                p_after = after = head

        head = h_next

    p_after.next = None
    p_before.next = after

    return before


if __name__ == "__main__":
    ll = LinkedList(Node(3))
    ll.push(5).push(8).push(5).push(10).push(2).push(1)

    rearranged = partition(ll, 5)

    head: Node = rearranged.head

    while head:
        print(head.data)
        head = head.next
