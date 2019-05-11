"""
Reverse a doubly linked list in groups of given size
e.g. input: 10-8-2-4, 2
    output: 8-10-4-2
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.len = 1

    def append(self, data):
        node = Node(data)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.len += 1
        return self

    def delete(self, data):
        h = self.head

        if h.data == data:
            self.head = h.next
            self.head.prev = None
            h.next = None
            del h
            self.len -= 1
        else:
            while h.next:
                h = h.next

                if h.data == data:
                    t = h.next
                    h.prev.next = h.next

                    if h.next:
                        h.next.prev = h.prev
                    else:
                        self.tail = h.prev

                    h = t
                    self.len -= 1
                    break

        return self

    def reverse(self):
        head = self.head
        prev_h = None

        while head:
            next_h = head.next
            head.next = prev_h
            head.prev = next_h
            prev_h = head
            head = next_h

        self.head, self.tail = self.tail, self.head


def reverse_in_groups(head, k):
    if k < 2 or k >= dll.len or not head:
        return None

    prev_h = head.prev
    local_head = head
    i = 0

    while i < k and local_head:
        next_head = local_head.next
        local_head.prev = next_head
        local_head.next = prev_h

        prev_h = local_head
        local_head = next_head
        i += 1

    head.next = reverse_in_groups(local_head, k)

    if prev_h:
        prev_h.prev = head.prev

    return prev_h


if __name__ == "__main__":
    dll = DLL(Node(1)).append(2).append(3).append(4).append(5)
    dll.delete(1).delete(3).delete(5)
    dll.append(10).append(8).append(100)

    h = dll.head

    while h.next:
        print(h.data, end='->')
        h = h.next

    print(h.data)

    dll.reverse()
    h = dll.head

    while h.next:
        print(h.data, end='->')
        h = h.next

    print(h.data)

    h = reverse_in_groups(dll.head, 2)

    while h.next:
        print(h.data, end='->')
        h = h.next

    print(h.data)
