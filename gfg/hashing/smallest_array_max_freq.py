"""
Given an array, A. Let x be an element in the array. x has the
maximum frequency in the array. Find the smallest subsegment of
the array which also has x as the maximum frequency element.
"""


def max_freq(arr: list) -> list:
    if not arr:
        return []

    hash_table: dict = {}
    max_occ: int = 0
    subseg: int = -1
    start_index: int = -1
    end_index: int = -1

    for index, value in enumerate(arr):
        if value in hash_table:
            hash_table[value][1] += 1
            hash_table[value][2] = index
        else:
            hash_table[value] = [index, 1, index]

        if (
            hash_table[value][1] > max_occ
            or hash_table[value][1] == max_occ
            and index - hash_table[value][0] < subseg
        ):
            max_occ = hash_table[value][1]
            subseg = index - hash_table[value][0]
            start_index = hash_table[value][0]
            end_index = index

    return arr[start_index : end_index + 1]


if __name__ == "__main__":
    print(max_freq([4, 1, 1, 2, 2, 1, 3, 3]))
    print(max_freq([1, 2, 2, 3, 1]))
