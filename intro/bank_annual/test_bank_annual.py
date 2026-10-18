import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("1000.00\n4.5\n3\n", "1141.17"),
        ("2500.00\n3.25\n5\n", "2933.53"),
        ("500.00\n2.8\n1\n", "514.00"),
    ],
)
def test_bank_annual(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
