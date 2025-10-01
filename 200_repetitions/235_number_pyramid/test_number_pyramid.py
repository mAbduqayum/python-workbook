import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["5"], "    1\n   121\n  12321\n 1234321\n123454321"),
    (["3"], "  1\n 121\n12321"),
    (["1"], "1"),
    (["0"], "Error"),
])
def test_number_pyramid(inputs, expected):
    test_input_output("200_repetitions/235_number_pyramid/number_pyramid.py", inputs, expected)
