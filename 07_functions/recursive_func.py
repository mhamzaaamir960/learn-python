# How recursion works?
# A recursive function must have two things:
# 1. Base Case: A condition where the recursion stops.
# 2. Recursive Case: The function calls itself with a modified argument to move towards the base case.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(5))

