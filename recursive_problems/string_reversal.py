#!/usr/bin/python3
"""string_reversal.py
"""


def string_reversal(word) -> str:
    """Reverses a string
    Arg:
        word: string to be reversed
    Return:
        Reversed string
    """
    if (word == ""):
        return word        
    return string_reversal(word[1:]) + word[0]

word = "desserts"
reversed = string_reversal(word)
print(f"The reversed word of {word} is {reversed}")
