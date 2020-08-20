"""
Given a word W and a string S, find all starting indices in S which are anagrams of W.
For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""
from collections import defaultdict
from typing import List


def get_anagrams(text: str, word: str) -> List[int]:
    """
    Naive Solution using set and dict
    """
    set_word = set(word)
    dict_word = defaultdict(int)
    dict_text = defaultdict(int)
    len_word = len(word)
    count_text = 0
    start_index = 0
    res = []

    for char in word:
        dict_word[char] += 1

    for index, char in enumerate(text):
        if char in set_word:
            dict_text[char] += 1
            count_text += 1
        else:
            start_index = index + 1
            dict_text = defaultdict(int)
            count_text = 0

        if count_text == len_word:
            for key, value in dict_text.items():
                if value > dict_word[key]:
                    while dict_text[key] > dict_word[key]:
                        cur_char = text[start_index]

                        if cur_char in dict_text and dict_text[cur_char] > 0:
                            dict_text[cur_char] -= 1
                            start_index += 1
                            count_text -= 1
                    break
            else:
                res.append(start_index)
                count_text -= 1
                dict_text[text[start_index]] -= 1
                start_index += 1

                while text[start_index] not in set_word:
                    start_index += 1

    return res


if __name__ == "__main__":
    # TODO: Rabin Karp solution
    assert get_anagrams("abxaba", "ab") == [0, 3, 4]
