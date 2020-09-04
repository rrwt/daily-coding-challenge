"""
Your team is scrambling to decipher a recent message,
worried it's a plot to break into a major European National Cake Vault.
The message has been mostly deciphered, but all the words are backward!
Your colleagues have handed off the last step to you.
Write a function reverse_words() that takes a message as a list of
characters and reverses the order of the words in place.
"""
from typing import List


def reverse_words(text: List[str]) -> List[str]:
    length = len(text)
    start_index, end_index = 0, length - 1

    while start_index < end_index:
        # reverse everything
        text[start_index], text[end_index] = text[end_index], text[start_index]
        start_index += 1
        end_index -= 1

    start_index = 0
    # reverse word by word
    while start_index < length:
        end_index = start_index + 1

        while end_index < length and text[end_index] != " ":
            end_index += 1

        temp_start, temp_end = start_index, end_index - 1

        while temp_start < temp_end:
            text[temp_start], text[temp_end] = text[temp_end], text[temp_start]
            temp_start += 1
            temp_end -= 1

        start_index = end_index + 1

    return text


if __name__ == "__main__":
    assert reverse_words(
        ["c", "a", "k", "e", " ", "p", "o", "u", "n", "d", " ", "s", "t", "e", "a", "l"]
    ) == ["s", "t", "e", "a", "l", " ", "p", "o", "u", "n", "d", " ", "c", "a", "k", "e"]
