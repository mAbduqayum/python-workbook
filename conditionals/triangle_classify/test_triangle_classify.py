from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "side1, side2, side3, expected_output",
    [
        (3, 3, 3, "equilateral"),
        (5, 5, 8, "isosceles"),
        (3, 4, 5, "scalene"),
        (7, 9, 7, "isosceles"),
        (2, 2, 2, "equilateral"),
        (10, 10, 15, "isosceles"),
        (6, 8, 10, "scalene"),
        (4, 4, 4, "equilateral"),
        (12, 5, 12, "isosceles"),
        (100, 100, 100, "equilateral"),
        (13, 14, 15, "scalene"),
    ],
)
def test_triangle_classify(script_runner, side1, side2, side3, expected_output):
    script_path = Path(__file__).parent / "triangle_classify.py"

    if not script_path.exists():
        pytest.skip("Solution file triangle_classify.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{side1}\n{side2}\n{side3}\n", expected_output=expected_output
    )
