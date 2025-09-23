from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("10.5\n5.2\n", "Area of triangle: 27.30"),
        ("8.3\n12.1\n", "Area of triangle: 50.22"),
        ("15.0\n7.8\n", "Area of triangle: 58.50"),
    ],
)
def test_triangle_area(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "triangle_area.py"

    if not script_path.exists():
        pytest.skip("Solution file triangle_area.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
