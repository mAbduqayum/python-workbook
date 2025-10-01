import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["20"], "2\n3\n5\n7\n11\n13\n17\n19"),
    (["10"], "2\n3\n5\n7"),
    (["2"], "2"),
    (["1"], "Error"),
])
def test_sieve_eratosthenes(inputs, expected):
    test_input_output("200_repetitions/233_sieve_eratosthenes/sieve_eratosthenes.py", inputs, expected)
