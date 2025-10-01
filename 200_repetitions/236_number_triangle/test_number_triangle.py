import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["5"], "1\n12\n123\n1234\n12345"),
    (["3"], "1\n12\n123"),
    (["1"], "1"),
    (["0"], "Error"),
])
def test_number_triangle(inputs, expected):
    test_input_output("200_repetitions/236_number_triangle/number_triangle.py", inputs, expected)
