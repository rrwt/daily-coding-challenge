"""
Given a linked list, rearrange the node values such that they
appear in alternating low -> high -> low -> high ... form.
For example,
    given 1 -> 2 -> 3 -> 4 -> 5,
    you should return 1 -> 3 -> 2 -> 5 -> 4.
"""
from daily_problems.linked_list import Node, create_ll_from_list, print_ll


def rearrange_ll(head: Node) -> Node:
    odd = True
    runner = head

    while runner and runner.next:
        if odd:
            if runner.data > runner.next.data:
                runner.data, runner.next.data = runner.next.data, runner.data
            odd = False
        else:
            if runner.data < runner.next.data:
                runner.data, runner.next.data = runner.next.data, runner.data
            odd = True

        runner = runner.next

    return head


if __name__ == "__main__":
    for n in range(1, 7):
        ll = create_ll_from_list(list(range(n)))
        print("Original LL:")
        print_ll(ll)
        ll = rearrange_ll(ll)
        print("Rearranged LL:")
        print_ll(ll)

    ll = create_ll_from_list([5, 4, 3, 2, 1])
    print("Original LL:")
    print_ll(ll)
    ll = rearrange_ll(ll)
    print("Rearranged LL:")
    print_ll(ll)
