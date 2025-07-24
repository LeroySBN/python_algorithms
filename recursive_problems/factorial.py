#!/usr/bin/python3
"""factorial.py
"""


# def main():
#     n = int(input("Please enter a whole number: "))
#     fact = 1
#     for factor in range(n,1,-1):
#         fact = fact * factor
#     string = 'The factorial of {:d} is {:d}'.format(n, fact)
#     print(string)
#     print("The factorial of", n, "is", fact)

# main ()

def factorial(n) -> int:
    """Computes the factorial of a number recursively
    Args:
        n - integer to be computed
    Returns:
        Factorial of n
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
