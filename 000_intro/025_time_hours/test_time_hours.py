from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("26.5\n", "26.5 hours = 1 days, 2 hours, and 30 minutes"),
        ("50.25\n", "50.25 hours = 2 days, 2 hours, and 15 minutes"),
        ("10.75\n", "10.75 hours = 0 days, 10 hours, and 45 minutes"),
    ],
)
def test_time_hours(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "time_hours.py"

    if not script_path.exists():
        pytest.skip("Solution file time_hours.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
