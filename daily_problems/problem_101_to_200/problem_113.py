"""
Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""


def reverse_text(text: str) -> str:
    return " ".join(reversed(text.split(" ")))


def reverse_text_mutable(text: str) -> str:
    """
    Inplace solution
    """
    length = len(text)
    text = list(text)  # mutable string
    text.reverse()  # reverse the mutable string in place

    start = 0
    end = 0

    while end < length:
        while end < length and text[end] != " ":
            end += 1

        temp_s, temp_e = start, end - 1

        while temp_s < temp_e:
            text[temp_s], text[temp_e] = text[temp_e], text[temp_s]
            temp_e -= 1
            temp_s += 1

        start = end + 1
        end = start

    return "".join(text)


if __name__ == "__main__":
    assert reverse_text("hello world here") == "here world hello"
    assert reverse_text_mutable("hello world here") == "here world hello"
