from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("6\n4\n", "Area of regular polygon: 41.57"),
        ("8\n3\n", "Area of regular polygon: 43.46"),
        ("5\n5\n", "Area of regular polygon: 43.01"),
    ],
)
def test_regular_polygon(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "regular_polygon.py"

    if not script_path.exists():
        pytest.skip("Solution file regular_polygon.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
