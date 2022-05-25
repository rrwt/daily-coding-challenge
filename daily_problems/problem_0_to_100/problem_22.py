"""
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example,
    given the set of words 'quick', 'brown', 'the', 'fox',
    and the string "thequickbrownfox",
    you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond',
and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
from typing import List, Tuple


def get_word_list(
    word_list: List[str], string: str, current_list: List[str] = None
) -> Tuple[bool, List[str]]:
    """
    Inefficient solution since it is checking every prefix.
    Efficient one will be with Trie ds.
    """
    if not current_list:
        current_list = []

    if not string:
        return True, current_list

    new_word_list = word_list[:]

    for word in word_list:
        if string.startswith(word):
            new_word_list.remove(word)
            found, final_list = get_word_list(
                new_word_list, string[len(word):], current_list + [word]
            )

            if found:
                return True, final_list

            new_word_list.append(word)

    return False, current_list


if __name__ == "__main__":
    print(get_word_list(["quick", "brown", "the", "fox"], "thequickbrownfox"))
    print(
        get_word_list(["bed", "bath", "bedbath", "and", "beyond"], "bedbathandbeyond")
    )
