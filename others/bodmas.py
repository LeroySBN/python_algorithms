#!/usr/bin/python3
"""bodmas.py
"""

def solve(text_equation: str) -> str:
    """Computes the bodmas
    Args:
        text_equation - string representation of an equation
    Returns:
        ERROR
        or the result rounded off to two decimal places
    """
    try:
        result = round(eval(text_equation), 2)
        return f"{result:.2f}"
    except (ZeroDivisionError, SyntaxError):
        return "ERROR"

# Test cases
print(solve("3*2-4*2/3-0"))    # Output: 3.33
print(solve("4"))               # Output: 4.00
print(solve("2*2*2*2*2"))       # Output: 32.00
print(solve("2*2/0-2"))         # Output: ERROR
