import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("47\n", "11"),
        ("82\n", "10"),
        ("95\n", "14"),
    ],
)
def test_sum_digits(solution, input_params, expected_output):
    solution.check_output(input_text=input_params, expected_output=expected_output)
