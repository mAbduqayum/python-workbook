import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["12345"], "15"),
    (["-987"], "24"),
    (["0"], "0"),
    (["99"], "18"),
    (["1000"], "1"),
])
def test_digit_sum(inputs, expected):
    test_input_output("200_repetitions/229_digit_sum/digit_sum.py", inputs, expected)
