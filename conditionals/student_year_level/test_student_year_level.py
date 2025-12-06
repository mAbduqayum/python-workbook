from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "year, expected_output",
    [
        (-1, "Invalid year"),
        (0, "Invalid year"),
        (1, "Freshman"),
        (2, "Sophomore"),
        (3, "Junior"),
        (4, "Senior"),
        (5, "Invalid year"),
    ],
)
def test_student_year_level(script_runner, year, expected_output):
    script_path = Path(__file__).parent / "student_year_level.py"

    if not script_path.exists():
        pytest.skip("Solution file student_year_level.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{year}\n", expected_output=expected_output
    )
