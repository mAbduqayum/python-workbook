import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("125\n", "2 5"),
        ("90\n", "1 30"),
        ("200\n", "3 20"),
        ("45\n", "0 45"),
    ],
)
def test_time_seconds(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
