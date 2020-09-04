"""
Given a linked list and a positive integer k, rotate the list to the right by k places.
For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
"""
from daily_problems.linked_list import Node, create_ll_from_list, print_ll


def right_shift_linked_list(head: Node, positions: int) -> Node:
    runner_1 = head
    runner_2 = head

    for _ in range(positions):
        runner_1 = runner_1.next

    while runner_1.next:
        runner_1 = runner_1.next
        runner_2 = runner_2.next

    runner_1.next = head
    head = runner_2.next
    runner_2.next = None
    return head


if __name__ == "__main__":
    ll = create_ll_from_list([1, 2, 3, 4, 5, 6, 7])
    print_ll(right_shift_linked_list(ll, 2))
