"""
Spreadsheets often use this alphabetical encoding for its columns:
"A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
Given a column number, return its alphabetical column id.
For example, given 1, return "A". Given 27, return "AA".
"""

hashmap = {key: chr(value) for key, value in zip(range(1, 27), range(65, 91))}


def column_id(column: int) -> str:
    column_list = []

    while column > 0:
        remainder = column % 26
        if remainder == 0:  # a multiple of 26
            column_list.append("Z")
            column = column // 26 - 1
        else:
            column_list.append(hashmap[remainder])
            column //= 26

    return "".join(reversed(column_list))


if __name__ == "__main__":
    assert column_id(1) == "A"
    assert column_id(26) == "Z"
    assert column_id(27) == "AA"
    assert column_id(52) == "AZ"
    assert column_id(53) == "BA"
    assert column_id(702) == "ZZ"
    assert column_id(703) == "AAA"
    assert column_id(728) == "AAZ"
