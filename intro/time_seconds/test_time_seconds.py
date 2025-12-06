from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("125\n", "125 seconds = 2 minutes and 5 seconds"),
        ("90\n", "90 seconds = 1 minutes and 30 seconds"),
        ("200\n", "200 seconds = 3 minutes and 20 seconds"),
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
