from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("5.3\n3.2\n", "The area is: 16.96"),
        ("10.5\n7.8\n", "The area is: 81.90"),
        ("4.0\n6.5\n", "The area is: 26.00"),
    ],
)
def test_rectangle_area(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "rectangle_area.py"

    if not script_path.exists():
        pytest.skip("Solution file rectangle_area.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
