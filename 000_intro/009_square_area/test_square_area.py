from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("7.5\n", "The area is: 56.25"),
        ("12.3\n", "The area is: 151.29"),
        ("5.0\n", "The area is: 25.00"),
    ],
)
def test_square_area(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "square_area.py"

    if not script_path.exists():
        pytest.skip("Solution file square_area.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
