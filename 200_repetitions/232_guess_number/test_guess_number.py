import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["50", "75", "62", "68"], "Too low\nToo high\nToo low\nCorrect"),
    (["1"], "Too low\nCorrect"),
    (["100"], "Too high\nCorrect"),
])
def test_guess_number(inputs, expected):
    # Note: This test is simplified and may need adjustment based on actual implementation
    # The random number makes testing challenging
    test_input_output("200_repetitions/232_guess_number/guess_number.py", inputs, expected)
