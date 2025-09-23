from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("3\n4\n5\n", "Area of triangle: 6.00"),
        ("5\n6\n7\n", "Area of triangle: 14.70"),
        ("10\n10\n12\n", "Area of triangle: 48.00"),
    ],
)
def test_triangle_heron(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "triangle_heron.py"

    if not script_path.exists():
        pytest.skip("Solution file triangle_heron.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
