"""
Print all permutations of a string
"""


def permutate(str_list: list, start: int, end: int) -> None:
    """
    Time Complexity: O(n*n!)
    """
    if start == end:
        print("".join(str_list))  # O(n)
    else:
        for i in range(start, end + 1):
            str_list[start], str_list[i] = str_list[i], str_list[start]
            permutate(str_list, start + 1, end)
            str_list[start], str_list[i] = str_list[i], str_list[start]


if __name__ == "__main__":
    print("permutation of ABC:")
    permutate(list("ABC"), 0, 2)
    print("Permutation of ABCD")
    permutate(list("ABCDE"), 0, 3)
