"""
Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"

TODO
Follow-up: given a mutable string representation, can you perform this operation in-place?
"""


def reverse_text(text: str) -> str:
    return " ".join(reversed(text.split(" ")))


if __name__ == "__main__":
    assert reverse_text("hello world here") == "here world hello"
