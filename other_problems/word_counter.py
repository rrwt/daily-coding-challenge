"""
Implement a program that counts occurrences of words in a given file.
The input will have multiple lines, with each line containing one or more words.
The output will be each word and how many times it appears.
You should print each word and its count on a separate line.
The output should sort the words in lexicographically sorted order.
Sample Input
    hello world
    world hello
    hello
    howdy
Sample Output
    hello 3
    howdy 1
    world 2
"""
import fileinput
from collections import defaultdict
from typing import List, Tuple


def count_words() -> List[Tuple[str, int]]:
    counter = defaultdict(int)

    for line in fileinput.input("./word_counter.txt"):
        for word in line.strip().split(" "):
            counter[word] += 1

    return list(sorted(counter.items(), key=lambda item: item[0].lower()))


if __name__ == "__main__":
    print(*count_words(), sep="\n")
