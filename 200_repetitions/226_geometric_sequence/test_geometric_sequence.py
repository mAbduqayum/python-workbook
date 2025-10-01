import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["2", "5", "3"], "2.0\n6.0\n18.0\n54.0\n162.0"),
    (["100", "4", "0.5"], "100.0\n50.0\n25.0\n12.5"),
    (["5", "1", "2"], "5.0"),
    (["5", "0", "2"], "Error"),
])
def test_geometric_sequence(inputs, expected):
    test_input_output("200_repetitions/226_geometric_sequence/geometric_sequence.py", inputs, expected)
