class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LL:
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        l = 0
        t = self.head

        while t:
            l += 1
            t = t.next

        return l

    def swap_node(self, k):
        '''swap kth node from the beginning with kth node from the end'''
        l = len(self)

        if l < k or l == 2*k-1:
            return None

        kn, pk = self.head, None
        lkn, lpk = self.head, None

        for i in range(1, l):
            if i < k:
                pk = kn
                kn = kn.next
            if i < l-k+1:
                lpk = lkn
                lkn = lkn.next

        if pk:
            pk.next = lkn

        if lpk:
            lpk.next = kn

        kn.next, lkn.next = lkn.next, kn.next

        if k == 1:
            self.head = lkn
        elif k == l:
            self.head = kn


if __name__ == '__main__':
    ll = LL(head=Node(1))
    p = ll.head
    p.next = Node(2, Node(3, Node(4, Node(5, Node(6)))))

    print('Original List', end=': ')

    while p.next:
        print(p.data, end=' -> ')
        p = p.next

    print(p.data)

    import random

    ll.swap_node(random.randint(1, 6))

    print('New List', end=': ')
    p = ll.head

    while p.next:
        print(p.data, end=' -> ')
        p = p.next

    print(p.data)
