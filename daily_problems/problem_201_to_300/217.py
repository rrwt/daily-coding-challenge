"""
We say a number is sparse if there are no adjacent ones in its binary representation.
For example, 21 (10101) is sparse, but 22 (10110) is not.
For a given input N, find the smallest sparse number greater than or equal to N.
Do this in faster than O(N log N) time.
"""


def next_sparse(n: int) -> int:
    """
    1) Find binary of the given number and store it in a boolean array.
    2) Initialize last_finalized bit position as 0.
    3) Start traversing the binary from least significant bit.
        a) If we get two adjacent 1's such that next (or third) bit is not 1, then
            (i)  Make all bits after this 1 to last finalized bit (including last finalized) as 0.
            (ii) Update last finalized bit as next bit.
    """
    n = list(str(bin(n)))[2:]
    size = len(n)

    if size < 2:
        return int(n[0])

    index = size - 1

    while index > -1:
        while index > -1 and n[index] == "0":
            index -= 1
        while index > -1 and n[index] == "1":
            index -= 1

        j = index + 1

        if j > -1 and n[j] == "1" and (size - j > 1 and n[j + 1] == "1"):
            n[j:] = "0" * (size - j)

            if index > 0:
                n[index] = "1"
            else:
                n.insert(0, "1")
                break

        index -= 1

    return int("".join(n))


if __name__ == "__main__":
    for i in range(23):
        print(f"{i} -> {next_sparse(i)}")
