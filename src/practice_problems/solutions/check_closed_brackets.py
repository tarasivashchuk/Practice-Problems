"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether
the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.

Brainstorming:
- Each bracket has to have it's closing character
- Has to be an even number of brackets
- In-between closing and opening has to be an even number of characters
- Groups can be checked by identifying the final closing character and then it will
    be easy to just check the first and final characters in each group until nothing is
    left
"""

import re

# Defining the options for opening and closing brackets as well as them in pairs
OPENING_BRACKETS = "([{<"
CLOSING_BRACKETS = ")]}>"
BRACKET_PAIRS = [("(", ")"), ("[", "]"), ("{", "}")]


def split_groups(brackets: str):
    """Splits a brackets string into it's independent sections by splitting anywhere
    a closing character is followed by an opening character."""
    pattern = re.compile("(?<=[)\]}>])(?=[(\[{<])")
    matches = pattern.split(brackets)
    return matches


def check_bracket_group(group):
    """Checks whether the passed bracket group is closed."""
    while len(group) > 1:
        start = group.pop(0)
        end = group.pop(-1)
        if (start, end) not in BRACKET_PAIRS:
            return False
    if len(group) != 0:
        return False
    return True


def check_brackets(bracket):
    """Checks whether the bracket is string is closed properly."""
    groups = split_groups(bracket)
    for group in groups:
        group = [char for char in group]
        closed = check_bracket_group(group)
        if not closed:
            return False
    return True
