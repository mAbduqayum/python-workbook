from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "year, expected_output",
    [
        (1600, "Saturday"),
        (1700, "Friday"),
        (1800, "Wednesday"),
        (1900, "Monday"),
        (1999, "Friday"),
        (2000, "Saturday"),
        (2001, "Monday"),
        (2017, "Sunday"),
        (2018, "Monday"),
        (2019, "Tuesday"),
        (2020, "Wednesday"),
        (2021, "Friday"),
        (2022, "Saturday"),
        (2023, "Sunday"),
        (2024, "Monday"),
        (2025, "Wednesday"),
        (2100, "Friday"),
        (2200, "Wednesday"),
        (2300, "Monday"),
        (2400, "Saturday"),
    ],
)
def test_january_weekday(script_runner, year, expected_output):
    script_path = Path(__file__).parent / "january_weekday.py"

    if not script_path.exists():
        pytest.skip("Solution file january_weekday.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{year}\n", expected_output=expected_output
    )
