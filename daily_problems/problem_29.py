"""
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count
and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded
have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""


def encode(string: str) -> str:
    i = 0
    l = len(string)
    res: str = ""

    while i < l:
        char: str = string[i]
        length: int = 1
        i += 1

        while i < l and char == string[i]:
            length += 1
            i += 1

        res += str(length) + char

    return res


def decode(string: str) -> str:
    res = ""
    for i in range(0, len(string), 2):
        res += string[i + 1] * int(string[i])

    return res


if __name__ == "__main__":
    string: str = "AAAABBBCCDAA"
    encoded: str = encode(string)
    assert decode(encoded) == string
