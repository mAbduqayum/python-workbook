from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "age, expected_output",
    [
        (0, "Infant"),
        (1, "Infant"),
        (2, "Toddler"),
        (3, "Toddler"),
        (4, "Toddler"),
        (5, "Child"),
        (8, "Child"),
        (10, "Child"),
        (11, "Adolescent"),
        (15, "Adolescent"),
        (17, "Adolescent"),
        (18, "Young Adult"),
        (25, "Young Adult"),
        (39, "Young Adult"),
        (40, "Middle-aged"),
        (50, "Middle-aged"),
        (64, "Middle-aged"),
        (65, "Senior"),
        (70, "Senior"),
        (100, "Senior"),
        (-5, "Invalid age"),
        (-1, "Invalid age"),
    ],
)
def test_life_phases(script_runner, age, expected_output):
    script_path = Path(__file__).parent / "life_phases.py"

    if not script_path.exists():
        pytest.skip("Solution file life_phases.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{age}\n", expected_output=expected_output
    )
