import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["5"], "*\n**\n***\n****\n*****"),
    (["3"], "*\n**\n***"),
    (["1"], "*"),
    (["0"], "Error"),
])
def test_right_triangle(inputs, expected):
    test_input_output("200_repetitions/223_right_triangle/right_triangle.py", inputs, expected)
