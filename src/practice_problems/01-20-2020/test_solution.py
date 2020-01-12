"""This module tests the examples given in the problem prompt to ensure correctness."""

import pytest

from solution import check_brackets

prompt_solutions_params = [
    ("([])[]({})", True),
    ("([)]", False),
    ("((()", False)
]


@pytest.fixture(params=prompt_solutions_params)
def prompt_solutions(request):
    """Fixture for the example solutions given in the prompt."""
    return request.param


def test_solutions(prompt_solutions):
    """Test function for the final solution by testing the examples given in the prompt."""
    brackets, answer = prompt_solutions
    closed = check_brackets(brackets)
    assert closed == answer
    