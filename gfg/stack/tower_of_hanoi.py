"""
Solve tower of hanoi iteratively
"""
import math


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
