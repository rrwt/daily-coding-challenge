"""
What does the below code snippet print out?
How can we fix the anonymous functions to behave as we'd expect?
"""

print("original implementation")
functions = []
for i in range(10):
    functions.append(lambda: i)

for f in functions:
    print(f())


# Solution
# The lambda function is expected to print a variable i on its execution.
# after the for loop finishes, the value of i becomes 9.
# this i gets accessed by the lambda function when we try to execute it, i.e. in next for loop
# therefore, when we invoke lambda using f(), we print 9 each time.
# to fix it, we'd need to bind the value of i to anonymous function when we try to add it.
# https://stackoverflow.com/questions/2295290/what-do-lambda-function-closures-capture
# https://stackoverflow.com/questions/58280201/lambda-function-call

print("new implementation")
functions = []
for i in range(10):
    functions.append(lambda j=i: j)

for f in functions:
    print(f())
