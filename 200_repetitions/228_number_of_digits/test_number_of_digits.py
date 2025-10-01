import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["12345"], "5"),
    (["-987"], "3"),
    (["0"], "1"),
    (["7"], "1"),
    (["1000000"], "7"),
])
def test_number_of_digits(inputs, expected):
    test_input_output("200_repetitions/228_number_of_digits/number_of_digits.py", inputs, expected)
