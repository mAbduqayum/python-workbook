import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["1", "1", "1", "2", "2", "3", "3", "3", "3", ""], "4"),
    (["5", "5", "5", "5", "5", ""], "5"),
    (["1", "2", "3", "4", ""], "1"),
    ([""], "Error"),
])
def test_max_streak(inputs, expected):
    test_input_output("200_repetitions/230_max_streak/max_streak.py", inputs, expected)
