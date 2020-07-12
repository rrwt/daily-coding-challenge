from typing import Iterable, List


def job_sequencing(job_ids: Iterable[str], deadlines: Iterable[int], profits: Iterable[int]) -> List[str]:
    # O(n * n). Sort the jobs by decreasing order of profit and work on them
    res = [''] * (max(deadlines) + 1)  # maximum number of possible jobs

    for (job_id, deadline, profit) in sorted(zip(job_ids, deadlines, profits), reverse=True, key=lambda item: item[2]):
        for index in range(deadline, 0, -1):
            if res[index] == '':
                res[index] = job_id
                break

    return list(filter(lambda el: el != '', res))


if __name__ == "__main__":
    assert job_sequencing(["a", "b", "c", "d"], [4, 1, 1, 1], [20, 10, 40, 30]) == ["c", "a"]
    assert job_sequencing(["a", "b", "c", "d", "e"], [2, 1, 2, 1, 3], [100, 19, 27, 25, 15]) == ["c", "a", "e"]
