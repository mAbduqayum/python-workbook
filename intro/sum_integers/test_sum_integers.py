from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("5\n", "15"),
        ("10\n", "55"),
        ("100\n", "5050"),
    ],
)
def test_sum_integers(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "sum_integers.py"

    if not script_path.exists():
        pytest.skip("Solution file sum_integers.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
