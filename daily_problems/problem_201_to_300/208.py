"""
Given a linked list of numbers and a pivot k, partition the linked list so that
all nodes less than k come before nodes greater than or equal to k.
For example,
    given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3,
    the solution could be 1 -> 0 -> 5 -> 8 -> 3.
"""
from daily_problems.linked_list import Node, create_ll_from_list, print_ll


def partition_list(head: Node, k: int) -> Node:
    smaller, larger = head, head

    while larger and larger.data < k:
        larger = larger.next
        smaller = smaller.next

    while larger is not None:
        if larger.data < k:
            smaller.data, larger.data = larger.data, smaller.data
            smaller = smaller.next
        larger = larger.next

    return head


if __name__ == "__main__":
    head_node = create_ll_from_list([2, 5, 1, 8, 0, 3])
    print_ll(partition_list(head_node, 3))
