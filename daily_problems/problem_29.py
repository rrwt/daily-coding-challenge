"""
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count
and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded
have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""


def encode(text: str) -> str:
    if not text:
        return ""

    char_count = 1
    char = text[0]
    index = 1
    res = []

    while index < len(text):
        if text[index] == char:
            char_count += 1
        else:
            res.append(f"{char}{char_count}")
            char = text[index]
            char_count = 1

        index += 1

    res.append(f"{char}{char_count}")
    return "".join(res)


def decode(text: str) -> str:
    return "".join(
        [text[index] * int(text[index + 1]) for index in range(0, len(text), 2)]
    )


if __name__ == "__main__":
    string: str = "AAAABBBCCDAA"
    encoded: str = encode(string)
    assert decode(encoded) == string
