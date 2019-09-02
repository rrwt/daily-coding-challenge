"""
Solve tower of hanoi iteratively

Fact: Number oof moves: 2^n - 1
"""
import math


def toh_recursive(n: int, source: list, destination: list, aux: list) -> None:
    """
    1) Only one disk can be moved at a time.
    2) Each move consists of taking the upper disk from one of the stacks
        and placing it on top of another stack i.e. a disk can only be moved
        if it is the uppermost disk on a stack.
    3) No disk may be placed on top of a smaller disk.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
    else:
        # move the stack of n-1 disks from source to aux using dest as aux
        toh_recursive(n - 1, source, aux, destination)
        # move nth disk to it's destination
        print(f"move disk {n} from {source} to {destination}")
        # move the stack of n-1 disks from aux to destination using source as aux
        toh_recursive(n - 1, aux, destination, source)


def toh(source: list) -> None:
    def move_between(s, d):
        if s and d:
            if s[-1] > d[-1]:
                s.append(d.pop())
            else:
                d.append(s.pop())
        elif s:
            d.append(s.pop())
        else:
            s.append(d.pop())

        return s, d

    l: int = len(source)
    destination: list = []
    aux: list = []
    num_of_moves: int = int(math.pow(2, l) - 1)

    for i in range(num_of_moves):
        if i % 3 == 0:
            # between source and destination
            source, destination = move_between(source, destination)
        elif i % 3 == 1:
            # between source and aux"
            source, aux = move_between(source, aux)
        else:
            # between aux and destination
            aux, destination = move_between(aux, destination)

    # l is even, then exchange aux and destination
    if l % 2 == 0:
        print(aux)
    else:
        print(destination)


if __name__ == "__main__":
    from random import randint

    toh(list(range(3))[::-1])
    toh_recursive(3, "source", "destination", "auxilliary")
