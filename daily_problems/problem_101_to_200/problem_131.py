"""
Given the head to a singly linked list, where each node also has a “random” pointer
that points to anywhere in the linked list, deep clone the list.
"""
from typing import Tuple


class Node:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.random = None


def deep_clone_ll(ll_head: Node) -> Tuple[Node, Node]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    runner = ll_head

    # get nodes of new linked list
    while runner:
        node = Node(runner.data)
        node.next = runner.next
        runner.next = node
        runner = runner.next.next

    # get random pointers of new ll
    runner = ll_head
    while runner:
        runner.next.random = runner.random.next
        runner = runner.next.next

    # detach two lists and fix their next pointers
    runner = ll_head
    new_head = ll_head.next

    while runner.next:
        next_node = runner.next

        if next_node.next:
            runner.next = next_node.next
            next_node.next = next_node.next.next
            runner = runner.next
        else:
            runner.next = None

    return ll_head, new_head


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head.next

    original, copied = deep_clone_ll(head)

    while original:
        print("orig node:", original.data, ", random:", original.random.data)
        print("copied node:", copied.data, ", random:", copied.random.data)
        original = original.next
        copied = copied.next
