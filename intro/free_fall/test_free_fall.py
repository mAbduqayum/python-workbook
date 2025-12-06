from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("10\n", "Final velocity: 14.00 m/s"),
        ("50\n", "Final velocity: 31.30 m/s"),
        ("100\n", "Final velocity: 44.27 m/s"),
    ],
)
def test_free_fall(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "free_fall.py"

    if not script_path.exists():
        pytest.skip("Solution file free_fall.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
