"""
You are given a starting state start, a list of transition probabilities
for a Markov chain, and a number of steps num_steps. Run the Markov chain
starting from start for num_steps and compute the number of times we visited
each state.

For example, given the starting state a, number of steps 5000,
and the following transition probabilities:
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce
{ 'a': 3012, 'b': 1656, 'c': 332 }.
"""
from collections import defaultdict
from random import random


class MarkovChain:
    def __init__(self, transitions: list) -> None:
        self.start = transitions[0][0]
        self.transition_dict = self._construct_transition_dict(transitions)

    @staticmethod
    def _construct_transition_dict(transitions: list) -> dict:
        td = defaultdict(list)

        for (start, end, val) in transitions:
            if start in td:
                td[start][0].append(end)
                td[start][1].append(val + td[start][1][-1])
            else:
                td[start] = [[end], [val]]

        return td

    def run(self, times: int) -> dict:
        res = {state: 0 for state in self.transition_dict.keys()}

        state = self.start
        for _ in range(times):
            prob = random()
            res[state] += 1

            for index, p in enumerate(self.transition_dict[state][1]):
                if p >= prob:
                    next_state = self.transition_dict[state][0][index]
                    break
            else:
                raise Exception("cannot proceed")

            state = next_state

        return res


if __name__ == "__main__":
    mc = MarkovChain(
        [
            ("a", "a", 0.9),
            ("a", "b", 0.075),
            ("a", "c", 0.025),
            ("b", "a", 0.15),
            ("b", "b", 0.8),
            ("b", "c", 0.05),
            ("c", "a", 0.25),
            ("c", "b", 0.25),
            ("c", "c", 0.5),
        ]
    )

    print(mc.run(5000))
