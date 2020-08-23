"""
Implement an autocomplete system. That is, given a query string s
and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

from typing import List, Optional

words = [
    "ADOXOGRAPHY",
    "ADUMBRATE",
    "AEIPATHY",
    "AEONIAN",
    "AESTHETE",
    "AFFABLE",
    "AILUROPHILE",
    "AIRNESS",
    "ALACRITY",
    "ALIS PROPRIIS VOLAT",
    "BACKPFEIFENGESICHT",
    "BAILE",
    "BAKKUSHAN",
    "BALISTIC",
    "BASOREXIA",
    "BAUSNI",
    "BE EXTRAORDINARY",
    "BE HAPPY",
    "BEATHA",
    "BEATIFY",
    "CAFUNE",
    "CALCINATION",
    "CALM",
    "CAMHANAICH",
    "CANDOR",
    "CAPRICE",
    "CARE",
    "CARPE DIEM",
    "CARPE NOCTEM",
    "CASCADE",
    "CASHMERE",
    "CATHARSIS",
    "DAIL",
    "DAIMON",
    "DALISAY",
    "DALLIANCE",
    "DANDY",
    "DATHUIL",
    "DAUNTLESS",
    "DAUWTRAPPEN",
    "DAZZLED",
    "DAZZLING",
    "DEBONAIR",
    "DEFENESTRATION",
    "EAGERNESS",
    "EARNEST",
    "EASE",
    "EASE-OF-MIND",
    "EBULLIENCE",
    "EBULLIENT",
    "ECOSOPHY",
    "ECSTATIFY",
    "EFFERVESCENCE",
    "EFFERVESCENT",
    "EFFLORESCENCE",
    "FABULOUS",
    "FADO",
    "FAILEAS",
    "FAILTE",
    "FAIR",
    "FAIRNESS",
    "FAITH",
    "FAITHFUL",
    "FAME",
    "FAMILY",
    "FAMOUS",
    "FANAA",
    "FANCY",
    "FANTABULOUS",
    "GAEL",
    "GAIET",
    "GAISCE",
    "GAMBOL",
    "GARGANTUAN",
    "GEMUTLICHKEIT",
    "GENERAVITY",
    "GIDDY",
    "GIFT",
    "GIGGLING",
    "GIGIL",
    "GINGER",
    "GLAD",
    "GLAMOR",
    "HABIBI",
    "HABILIN",
    "HALAKHAK",
    "HALCYON",
    "HALO",
    "HANDSOME",
    "HANYAUKU",
    "HAPPINESS",
    "HAPPY HEARTED",
    "HAPPYHEARTED",
    "HAR",
    "HARBINGER",
    "HARMONY",
]


# O(n) for search. Naive algorithm
# TODO: Using Trie
def complete_me(prefix: str, word_list: List[str]) -> list:
    return [w for w in word_list if w.startswith(prefix)]


class Node:
    def __init__(self, char: str) -> None:
        self.char = char
        self.is_complete: bool = False
        self.children: List[Node] = []
        self.words: set = set()


class Trie:
    def __init__(self) -> None:
        self.root = Node("")

    def insert(self, word: str) -> None:
        runner = self.root
        index = 0
        l = len(word)

        while index < l and runner.children:
            for child in runner.children:
                if word[index] == child.char:
                    runner.words.add(word)
                    runner = child
                    break
            else:
                break
            index += 1

        for j in range(index, l):
            node = Node(word[j])
            runner.children.append(node)
            runner.words.add(word)
            j += 1
            runner = node

        runner.is_complete = True


def complete_me_trie(prefix: str, trie: Trie) -> Optional[list]:
    runner = trie.root
    l = len(prefix)
    index = 0

    while index < l and runner.children:
        for child in runner.children:
            if child.char == prefix[index]:
                runner = child
                break
        else:
            return None
        index += 1

    return sorted(list(runner.words))


if __name__ == "__main__":
    assert complete_me("AD", words) == ["ADOXOGRAPHY", "ADUMBRATE"]
    assert complete_me("BE", words) == ["BE EXTRAORDINARY", "BE HAPPY", "BEATHA", "BEATIFY"]

    trie = Trie()

    for word in words:
        trie.insert(word)

    assert complete_me_trie("AD", trie) == ["ADOXOGRAPHY", "ADUMBRATE"]
    assert complete_me_trie("BE", trie) == ["BE EXTRAORDINARY", "BE HAPPY", "BEATHA", "BEATIFY"]
