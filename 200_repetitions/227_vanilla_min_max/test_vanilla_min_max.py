import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["5", "12", "3", "8", "15", ""], "Minimum: 3\nMaximum: 15"),
    (["-5", "-2", "-10", "-1", ""], "Minimum: -10\nMaximum: -1"),
    (["7", ""], "Minimum: 7\nMaximum: 7"),
    ([""], "Error"),
])
def test_vanilla_min_max(inputs, expected):
    test_input_output("200_repetitions/227_vanilla_min_max/vanilla_min_max.py", inputs, expected)
