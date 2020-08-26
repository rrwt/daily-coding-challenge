"""
Given the head of a singly linked list, swap every two nodes and return its head.
For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""
from typing import Optional, List

from daily_problems.linked_list import Node


def swap_nodes_in_pairs(head: Optional[Node] = None) -> Optional[Node]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not (head and head.next):
        return head

    first = head
    second = head.next
    first.next = second.next
    second.next = first
    first.next = swap_nodes_in_pairs(first.next)

    return second


def list_to_ll(nums: List[int]) -> Node:
    head = tail = Node(nums[0])

    for val in nums[1:]:
        tail.next = Node(val)
        tail = tail.next

    return head


def print_ll(head: Node) -> None:
    runner = head

    while runner:
        print(runner.data, end=" ")
        runner = runner.next
    print()


if __name__ == "__main__":
    ll = list_to_ll([1, 2])
    print("original")
    print_ll(ll)
    print("new")
    print_ll(swap_nodes_in_pairs(ll))

    ll = list_to_ll([1, 2, 3])
    print("original")
    print_ll(ll)
    print("new")
    print_ll(swap_nodes_in_pairs(ll))

    ll = list_to_ll([1, 2, 3, 4])
    print("original")
    print_ll(ll)
    print("new")
    print_ll(swap_nodes_in_pairs(ll))

    ll = list_to_ll([1, 2, 3, 4, 5])
    print("original")
    print_ll(ll)
    print("new")
    print_ll(swap_nodes_in_pairs(ll))
