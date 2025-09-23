from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("5.2\n", "The area is: 84.95"),
        ("3.7\n", "The area is: 43.01"),
        ("10.0\n", "The area is: 314.16"),
    ],
)
def test_circle_area(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "circle_area.py"

    if not script_path.exists():
        pytest.skip("Solution file circle_area.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
