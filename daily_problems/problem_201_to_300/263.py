"""
Create a basic sentence checker that takes in a stream of characters and
determines whether they form valid sentences. If a sentence is valid,
the program should print it out.
We can consider a sentence valid if it conforms to the following rules:
    The sentence must start with a capital letter,
    followed by a lowercase letter or a space.
    All other characters must be lowercase letters,
    separators (,,;,:) or terminal marks (.,?,!,‽).
    There must be a single space between each word.
    The sentence must end with a terminal mark immediately following a word.
"""


class SentenceChecker:
    def __init__(self):
        self.separators = {",", ";", ":"}
        self.terminal_marks = {".", "?", "!"}
        self.lowercase = set([chr(x) for x in range(97, 123)])

    def is_valid(self, text: str) -> bool:
        if not text:
            return False

        if not text[0].istitle():
            return False

        for index, char in enumerate(text[1:], start=1):
            if char == " " and text[index - 1] == " ":
                return False
            elif char in self.separators and text[index - 1] not in self.lowercase:
                return False
            elif char in self.terminal_marks:
                if (
                    (len(text) > index + 1 and text[index + 1] != " ")
                    or index == 1
                    or text[index - 1] not in self.lowercase
                ):
                    return False
            elif not (char == " " or char in self.lowercase):
                return False

        if text[-1] not in self.terminal_marks or text[-2] not in self.lowercase:
            return False

        print(text)
        return True


if __name__ == "__main__":
    sc = SentenceChecker()
    assert sc.is_valid("Valid sentence.") is True
    assert sc.is_valid("Invalid sentence") is False
    assert sc.is_valid("INvalid sentence.") is False
    assert sc.is_valid("A valid sentence.") is True
