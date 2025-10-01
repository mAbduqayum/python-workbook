import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["5"], "    *\n   ***\n  *****\n *******\n*********"),
    (["3"], "  *\n ***\n*****"),
    (["1"], "*"),
    (["0"], "Error"),
])
def test_pyramid(inputs, expected):
    test_input_output("200_repetitions/224_pyramid/pyramid.py", inputs, expected)
