from array import array


class Stack:
    def __init__(self, k: int, n: int):
        """
        Implement k stacks using an array of size n
        """
        self.nos = k
        self.size = n
        self.array = array("b", (0 for i in range(n)))
        self.tos = [-1] * self.nos  # top of kth stack

        """
        when stack is empty: point to the next available index (for push)
        when stack has values: point to the previous element of the stack (for pop)
        """
        self.next_index = array("b", (i + 1 for i in range(n)))
        self.next_index[n - 1] = -1  # stack overflow
        self.next_available = 0  # which index to push to

    def is_full(self):
        return self.next_available == self.size

    def is_empty(self, k):
        return self.tos[k] == -1

    def push(self, k: int, data: int):
        """
        push data to kth stack
        """
        index = self.next_available
        self.array[index] = data
        self.next_available = self.next_index[index]
        self.next_index[index] = self.tos[k]  # from empty -> value
        self.tos[k] = index

    def pop(self, k):
        """
        pop out an element from the kth stack
        """
        if self.is_empty(k):
            return ValueError("Stack Underflow")

        tos = self.tos[k]
        self.tos[k] = self.next_index[tos]
        self.next_index[tos] = self.next_available  # from value -> empty
        self.next_available = tos
        return self.array[tos]


if __name__ == "__main__":
    s = Stack(4, 10)

    from random import randint

    for i in range(10):
        j = randint(0, 3)
        s.push(j, i)
