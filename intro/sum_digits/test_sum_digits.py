from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("47\n", "4 + 7 = 11"),
        ("82\n", "8 + 2 = 10"),
        ("95\n", "9 + 5 = 14"),
    ],
)
def test_sum_digits(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "sum_digits.py"

    if not script_path.exists():
        pytest.skip("Solution file sum_digits.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
