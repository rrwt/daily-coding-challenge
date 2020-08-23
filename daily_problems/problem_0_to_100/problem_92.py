"""
We're given a hashmap associating each courseId key with a list of courseIds values,
which represents that the prerequisites of courseId are courseIds.
Return a sorted ordering of courses such that we can finish all courses.
Return null if there is no such ordering.

For example,
    given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
    should return ['CSC100', 'CSC200', 'CSC300'].
"""
from typing import List, Optional


def _course_order(independent: set, final_order: list, pre_reqs: dict) -> List:
    """
    One by one, remove course not dependent on remaining courses,
    and add those to the final order
    """
    if not independent:  # no starting point
        return []
    if not pre_reqs:  # nothing to see here
        return final_order

    new_indep = set()  # to not modify the dict within for loop

    for course, pre_requisites in pre_reqs.items():
        intersect = independent.intersection(pre_requisites)

        for c in intersect:
            pre_reqs[course].remove(c)

            if not pre_reqs[course]:
                independent.add(course)
                new_indep.add(course)
                final_order.append(course)

    for course in new_indep:
        del pre_reqs[course]

    return _course_order(independent, final_order, pre_reqs)


def course_order(pre_reqs: dict) -> List[Optional[str]]:
    independent = set()
    final_order = []

    for course, pre_requisites in pre_reqs.items():
        # if there is no pre-requisite, then the course is independent of any other
        if not pre_requisites:
            independent.add(course)
            final_order.append(course)
        else:  # convert to set for easy search
            pre_reqs[course] = set(pre_requisites)

    for course in independent:  # no need to process these courses
        del pre_reqs[course]

    return _course_order(independent, final_order, pre_reqs)


if __name__ == "__main__":
    assert course_order(
        {"300": ["100", "200"], "200": ["100"], "100": []}
    ) == ["100", "200", "300"]

    assert course_order({"300": [], "100": [], "200": []}) == ["300", "100", "200"]

    assert course_order(
        {"400": ["200"], "300": ["100", "200"], "200": ["100"], "100": []}
    ) == ["100", "200", "400", "300"]

    assert course_order(
            {"400": ["300"], "300": ["100", "200"], "200": ["100"], "100": ["400"]}
    ) == []
