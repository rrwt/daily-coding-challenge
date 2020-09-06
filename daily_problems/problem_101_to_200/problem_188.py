"""
What will this code print out?
How can we make it print out what we apparently want?

Sol:
    It will print 3, 3, 3 because functions are bound to variables
    when we call them and not when those functions are created

    To print 1, 2, 3:
        make print accept the variable it is going to print
"""


def make_functions():
    flist = []
    glist = []

    for i in [1, 2, 3]:
        # V1
        def print_i():
            print(i)  # printing non local variable i (closure)

        # V2
        def print_i2(i):
            print(i)  # printing i bound to current function

        flist.append(print_i)
        glist.append((print_i2, i))

    return flist, glist


funcs_1, funcs_2 = make_functions()

for f in funcs_1:
    f()

for f, _ in funcs_2:
    f(_)
