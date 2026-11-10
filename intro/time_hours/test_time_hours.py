import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("26.5\n", "1 2 30"),
        ("50.25\n", "2 2 15"),
        ("10.75\n", "0 10 45"),
        ("4.1\n", "0 4 6"),
        ("1.01\n", "0 1 1"),
        ("1.999\n", "0 2 0"),
        ("23.999\n", "1 0 0"),
    ],
)
def test_time_hours(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
