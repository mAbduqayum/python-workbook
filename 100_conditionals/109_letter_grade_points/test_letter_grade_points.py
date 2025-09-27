from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "grade, expected_output",
    [
        ("A+", "4.0"),
        ("A", "4.0"),
        ("A-", "3.7"),
        ("B+", "3.3"),
        ("B", "3.0"),
        ("B-", "2.7"),
        ("C+", "2.3"),
        ("C", "2.0"),
        ("C-", "1.7"),
        ("D+", "1.3"),
        ("D", "1.0"),
        ("F", "0.0"),
        ("Z", "Invalid grade"),
        ("X", "Invalid grade"),
        ("", "Invalid grade"),
    ],
)
def test_letter_grade_points(script_runner, grade, expected_output):
    script_path = Path(__file__).parent / "letter_grade_points.py"

    if not script_path.exists():
        pytest.skip("Solution file letter_grade_points.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{grade}\n", expected_output=expected_output
    )