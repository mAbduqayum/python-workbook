from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("125\n", "125 second(s) = 2 minute(s) and 5 second(s)"),
        ("90\n", "90 second(s) = 1 minute(s) and 30 second(s)"),
        ("200\n", "200 second(s) = 3 minute(s) and 20 second(s)"),
    ],
)
def test_time_seconds(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "time_seconds.py"

    if not script_path.exists():
        pytest.skip("Solution file time_seconds.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
