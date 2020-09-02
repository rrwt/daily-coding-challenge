from typing import Optional, Union, List


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None


def print_ll(head: Node) -> None:
    runner = head

    while runner.next:
        print(runner.data, end="->")
        runner = runner.next

    if runner:
        print(runner.data)


def get_node_count(head: Node) -> int:
    runner = head
    count = 0

    while runner:
        count += 1
        runner = runner.next

    return count


def create_ll_from_list(values: List[Union[int, str]]) -> Node:
    head = tail = Node(values[0])

    for element in values[1:]:
        tail.next = Node(element)
        tail = tail.next

    return head
