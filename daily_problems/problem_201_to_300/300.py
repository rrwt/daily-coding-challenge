"""
On election day, a voting machine writes data in the form
(voter_id, candidate_id) to a text file. Write a program
that reads this file as a stream and returns the top 3
candidates at any given time. If you find a voter voting
more than once, report this as fraud.
"""
from collections import defaultdict
from typing import Tuple


class VotingMachine:
    def __init__(self) -> None:
        self.candidates = defaultdict(int)
        self.voters = set()

    def count_votes(self, file_path: str) -> None:
        with open(file_path, 'r') as file:
            for line in file.readlines():
                voter_id, candidate_id = line.strip().split(", ")

                if voter_id in self.voters:
                    print("Fraud Detected")
                    return None
                else:
                    self.voters.add(voter_id)

                self.candidates[candidate_id] += 1

    def top_candidates(self) -> Tuple[int, ...]:
        return list(
            zip(*sorted(self.candidates.items(), key=lambda item: item[1], reverse=True))
        )[0][:3]


if __name__ == "__main__":
    vm = VotingMachine()
    vm.count_votes("300_voters.txt")
    print(vm.top_candidates())
