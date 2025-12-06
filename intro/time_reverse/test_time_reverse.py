from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("186330\n", "Time format: 2:03:45:30"),
        ("88200\n", "Time format: 1:00:30:00"),
        ("8145\n", "Time format: 0:02:15:45"),
    ],
)
def test_time_reverse(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "time_reverse.py"

    if not script_path.exists():
        pytest.skip("Solution file time_reverse.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
