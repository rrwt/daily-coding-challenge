"""
Given a dictionary that contains mapping of employee and his manager as a number of
(employee, manager) pairs like below.
{ "A", "C" },
{ "B", "C" },
{ "C", "F" },
{ "D", "E" },
{ "E", "F" },
{ "F", "F" } 

In this example C is manager of A, C is also manager of B, F is manager of C and so on.
Write a function to get no of employees under each manager in the hierarchy not just
their direct reports. It may be assumed that an employee directly reports to only one
manager. In the above dictionary the root node/ceo is listed as reporting to himself.
Output should be a Dictionary that contains following.
A - 0  
B - 0
C - 2
D - 0
E - 1
F - 5 
"""


def get_emp_heirarchy(manager: str, return_dict: dict, man_emp: dict) -> int:
    count = 0

    for employee in man_emp.get(manager, []):
        if employee not in return_dict:
            return_dict[employee] = get_emp_heirarchy(employee, return_dict, man_emp)
        count += return_dict[employee] + 1

    return count


def heirarchy(emp_man: dict) -> dict:
    """
    Create a manager - employee dictionary
    Recursively iterate over it to find the number of eemoloyees under each and every manager
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    man_emp: dict = {}
    return_dict: dict = {}

    for emp, man in emp_man.items():
        if emp == man:
            continue
        if man in man_emp:
            man_emp[man].append(emp)
        else:
            man_emp[man] = [emp]

    for manager in man_emp:
        return_dict[manager] = get_emp_heirarchy(manager, return_dict, man_emp)

    return return_dict


if __name__ == "__main__":
    emp_man: dict = {"A": "C", "B": "C", "C": "F", "D": "E", "E": "F", "F": "F"}
    print(heirarchy(emp_man))
