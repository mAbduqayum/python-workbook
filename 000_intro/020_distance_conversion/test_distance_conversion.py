from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("10\n", "Distance in feet: 32.81"),
        ("5\n", "Distance in feet: 16.40"),
        ("15\n", "Distance in feet: 49.21"),
    ],
)
def test_distance_conversion(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "distance_conversion.py"

    if not script_path.exists():
        pytest.skip("Solution file distance_conversion.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
