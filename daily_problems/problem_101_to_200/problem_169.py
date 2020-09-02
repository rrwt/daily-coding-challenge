"""
Given a linked list, sort it in O(n log n) time and constant space.
"""

from daily_problems.linked_list import (
    Node,
    print_ll,
    get_node_count,
    create_ll_from_list,
)


def get_middle(head: Node, size: int) -> Node:
    runner = head

    for i in range(1, size // 2):
        runner = runner.next

    return runner


def _merge(first: Node, second: Node) -> Node:
    if first and second:
        if first.data <= second.data:
            head = Node(first.data)
            first = first.next
        else:
            head = Node(second.data)
            second = second.next
    elif first:
        return first
    else:
        return second

    tail = head

    while first and second:
        if first.data <= second.data:
            tail.next = Node(first.data)
            first = first.next
        else:
            tail.next = Node(second.data)
            second = second.next

        tail = tail.next

    while first:
        tail.next = Node(first.data)
        first = first.next
        tail = tail.next

    while second:
        tail.next = Node(second.data)
        second = second.next
        tail = tail.next

    return head


def _merge_sort(head: Node, size: int) -> Node:
    if size > 1:
        middle = get_middle(head, size)
        second_node = middle.next
        middle.next = None
        first = _merge_sort(head, size // 2)
        second = _merge_sort(second_node, size - size // 2)
        return _merge(first, second)

    return head


def merge_sort(head: Node) -> Node:
    """
    A linked list can be merge sorted in O(n * log(n)) time
    """
    size = get_node_count(head)
    return _merge_sort(head, size)


if __name__ == "__main__":
    print_ll(merge_sort(create_ll_from_list([4])))
    print_ll(merge_sort(create_ll_from_list([4, 1])))
    print_ll(merge_sort(create_ll_from_list([4, 1, 3])))
    print_ll(merge_sort(create_ll_from_list([4, 1, 3, 99])))
