class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


def copy_ll(head):
    temp = head

    while temp:
        next = temp.next
        temp.next = Node(temp.data)
        temp.next.next = next
        temp = temp.next.next

    temp = head

    while temp:
        temp.next.random = temp.random.next
        temp = temp.next.next

    new_head = head.next
    temp = head

    while temp.next:
        next = temp.next
        temp.next = next.next
        temp = next

    return new_head


if __name__ == "__main__":
    original_list = Node(1)
    original_list.next = Node(2)
    original_list.next.next = Node(3)
    original_list.next.next.next = Node(4)
    original_list.next.next.next.next = Node(5)

    original_list.random = original_list.next.next
    original_list.next.random = original_list
    original_list.next.next.random = original_list.next.next.next.next
    original_list.next.next.next.random = original_list.next.next.next.next
    original_list.next.next.next.next.random = original_list.next
    head = copy_ll(original_list)

    while head:
        print(head.data)
        head = head.next
