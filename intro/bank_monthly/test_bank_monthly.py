import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("1000.00\n4.0\n3\n", "1127.27"),
        ("5000.00\n3.5\n2\n", "5361.99"),
        ("2500.00\n2.25\n1\n", "2556.83"),
    ],
)
def test_bank_monthly(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
