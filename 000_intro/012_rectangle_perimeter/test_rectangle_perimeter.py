from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("8.5\n5.2\n", "The perimeter is: 27.40"),
        ("12.3\n4.7\n", "The perimeter is: 34.00"),
        ("6.0\n6.0\n", "The perimeter is: 24.00"),
    ],
)
def test_rectangle_perimeter(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "rectangle_perimeter.py"

    if not script_path.exists():
        pytest.skip("Solution file rectangle_perimeter.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
