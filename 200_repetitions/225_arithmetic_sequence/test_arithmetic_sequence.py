import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["5", "20", "3"], "5\n8\n11\n14\n17\n20"),
    (["10", "1", "-2"], "10\n8\n6\n4\n2"),
    (["1", "1", "1"], "1"),
    (["1", "10", "0"], "Error"),
])
def test_arithmetic_sequence(inputs, expected):
    test_input_output("200_repetitions/225_arithmetic_sequence/arithmetic_sequence.py", inputs, expected)
