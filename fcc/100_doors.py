"""
Problem: you have 100 doors in a row that are all initially closed. you make 100
passes by the doors starting with the first door every time. the first time through
you visit every door and toggle the door (if the door is closed, you open it, if
its open, you close it). the second time you only visit every 2nd door
(door #2, #4, #6). the third time, every 3rd door (door #3, #6, #9), etc,
until you only visit the 100th door.

question: what state are the doors in after the last pass? which are open
which are closed?
"""
import math


def count_factors(num):
    if num < 1:
        return None
    if num == 1:
        return 1

    count = 1

    for i in range(2, num+1):
        if num % i == 0:
            count += 1

    return count


def is_open(num):
    return count_factors(num) % 2 == 1


# This can be solved by taking factors of the given number
def get_state(numDoors):
    return [i for i in range(1, numDoors+1) if is_open(i)]


def is_perfect_square(num):
    sq_root = math.sqrt(num)
    return math.floor(sq_root) == math.ceil(sq_root)

# after testing, i realized that only perfect squares will be open


def get_state_efficient(numDoors):
    return [i for i in range(1, numDoors+1) if is_perfect_square(i)]


if __name__ == "__main__":
    print(get_state(100))
    print(get_state_efficient(100))
