"""
Given a string and a set of delimiters, reverse the words in the string
while maintaining the relative order of the delimiters.
For example, given "hello/world:here", return "here/world:hello"
Follow-up: Does your solution work for the following case: "hello//world:here"
"""


def reverse_words_keeping_delimiters(text: str) -> str:
    delimiters = []
    text = list(text)

    for index, char in enumerate(text):  # mutate
        if char in ("/", ":"):
            delimiters.append(char)
            text[index] = " "

    text = "".join(text).split(" ")
    start = 0
    end = len(text) - 1

    while start < end:
        if text[start] == "":
            start += 1
        elif text[end] == "":
            end -= 1
        else:
            text[start], text[end] = text[end], text[start]
            start += 1
            end -= 1

    text = list(" ".join(text))

    ind_delimiters = 0

    for index, char in enumerate(text):
        if char == " ":
            text[index] = delimiters[ind_delimiters]
            ind_delimiters += 1

    return "".join(text)


if __name__ == "__main__":
    assert reverse_words_keeping_delimiters("hello/world:here") == "here/world:hello"
    assert reverse_words_keeping_delimiters("hello//world:here") == "here//world:hello"
