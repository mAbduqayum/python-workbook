import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["5"], "2"),
    (["3"], "2"),
    (["1"], "2"),
    (["0"], "Error"),
])
def test_sum_table(inputs, expected):
    test_input_output("200_repetitions/234_sum_table/sum_table.py", inputs, expected)
