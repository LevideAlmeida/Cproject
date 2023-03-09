# Recursive function
# - Are functions that call yourself
# - Useful for breaking big problems into small problems
# All recursive functions must have:
# - A problem that can be broken down into small problems
# - A recursive case that solve the small problem
# - A base case that stop the function
# Factorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120


def recursive(start=0, end=10):
    # Recursive case
    # Count to the end

    # Base case
    if start >= end:
        return end

    print(start, end)

    start += 1
    return recursive(start, end)

print(recursive())

def factorial(n):
    if n <= 1:
        return n

    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
print(factorial(100))
print(factorial(996))
