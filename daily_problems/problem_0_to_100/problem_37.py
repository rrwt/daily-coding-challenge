"""
The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3},
it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
"""


def power_set(original_set: list) -> list:  # All possible combinations
    if not original_set:
        return [[]]

    result: list = []

    for c in power_set(original_set[1:]):
        result += [c, c + [original_set[0]]]

    return result


def power_set2(original, index=0, size=None):
    if not size:
        size = len(original)

    if index >= size:
        return [[]]

    result = []
    for next_set in power_set2(original, index+1, size):
        result.append(next_set)
        result.append(next_set + [original[index]])

    return result


if __name__ == "__main__":
    print(power_set([1, 2, 3]))
    print(power_set2([1, 2, 3]))
