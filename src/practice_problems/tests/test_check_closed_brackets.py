"""This module tests the examples given in the problem prompt to ensure correctness.

From the prompt:
    - For example, given the string "([])[]({})", you should return true.
    - Given the string "([)]" or "((()", you should return false.
"""

import pytest

from practice_problems.solutions.check_closed_brackets import (check_brackets,
                                                               split_groups, )

bracket_params = [
        ("([])[]({})", ["([])", "[]", "({})"], True),
        ("([)]", ["([)]"], False),
        ("((()", ["((()"], False),
]


@pytest.fixture(params=bracket_params)
def bracket_examples(request):
    """Fixture for passing along bracket strings."""
    return request.param


def test_split_groups(bracket_examples):
    brackets, groups, _ = bracket_examples
    test_groups = split_groups(brackets)
    assert test_groups == groups


def test_solutions(bracket_examples):
    """Tests whether or not check_brackets correctly identifies closed brackets."""
    brackets, _, answer = bracket_examples
    closed = check_brackets(brackets)
    assert closed == answer
