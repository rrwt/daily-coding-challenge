"""
Write an algorithm to justify text.
Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces,
if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
you should return the following:
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""
from typing import List


def get_spaced_string(string_list: List[str], string_len: int, line_length: int) -> str:
    if string_len == line_length:
        return " ".join(string_list)

    length_list: int = len(string_list)

    if length_list == 1:
        return string_list[0].ljust(line_length, " ")

    spaces_required: int = line_length - string_len
    new_space_list: List[int] = [0] * length_list
    i: int = 0

    while spaces_required:
        new_space_list[i] += 1
        spaces_required -= 1
        i = (i + 1) % (
            length_list - 1
        )  # the last word doesn't get extra space after it

    for i in range(length_list - 1):  # the last word doesn't get extra space after it
        string_list[i] = string_list[i] + " " * new_space_list[i]

    return " ".join(string_list)


def word_wrap(words: List[str], line_length: int) -> List[str]:
    length: int = len(words)
    length_arr: List[int] = [len(word) for word in words]

    if length <= 1:
        return words

    i: int = 0
    res: List[str] = []

    while i < length:
        cur_len: int = length_arr[i]
        j: int = i + 1

        while j < length:
            new_len = cur_len + length_arr[j] + 1  # 1 for extra space

            if new_len > line_length:
                break
            cur_len = new_len
            j += 1

        if cur_len > line_length:
            raise Exception("the algorithm was not implemented correctly")

        res.append(get_spaced_string(words[i:j], cur_len, line_length))
        i = j

    return res


if __name__ == "__main__":
    word_list: List[str] = [
        "the",
        "quick",
        "brown",
        "fox",
        "jumps",
        "over",
        "the",
        "lazy",
        "dog",
    ]
    k: int = 16
    print(word_list)
    print(*word_wrap(word_list, k), sep="\n")

    word_list: List[str] = [
        "This",
        "is",
        "an",
        "example",
        "of",
        "text",
        "justification.",
    ]
    print(word_list)
    print(*word_wrap(word_list, k), sep="\n")
