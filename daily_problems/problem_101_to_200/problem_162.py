"""
Given a list of words, return the shortest unique prefix of each word.
For example, given the list:
    dog cat apple apricot fish
Return the list:
    d c app apr f
"""


class Trie:
    def __init__(self):
        self.size = 0
        self.letter_map = dict()

    def __repr__(self):
        return str(self.letter_map)

    def add_word(self, word):
        if not word:
            return
        letter = word[0]

        if letter in self.letter_map:
            sub_trie = self.letter_map[letter]
        else:
            sub_trie = Trie()
            self.letter_map[letter] = sub_trie

        self.size += 1
        sub_trie.add_word(word[1:])

    def get_shortest_unique_prefix(self, word, prev):
        if self.size < 2:
            return prev

        letter = word[0]
        sub_trie = self.letter_map[letter]
        return sub_trie.get_shortest_unique_prefix(word[1:], prev + letter)


def get_shortest_unique_prefixes(words):
    trie = Trie()
    for word in words:
        trie.add_word(word)

    sups = []
    for word in words:
        sups.append(trie.get_shortest_unique_prefix(word, ""))

    return sups


if __name__ == "__main__":
    assert get_shortest_unique_prefixes(["dog", "cat", "apple", "apricot", "fish"]) == [
        "d",
        "c",
        "app",
        "apr",
        "f",
    ]
