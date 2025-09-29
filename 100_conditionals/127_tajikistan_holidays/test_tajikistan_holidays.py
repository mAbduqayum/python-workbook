from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "month, day, expected_output",
    [
        (1, 1, "New Year's Day"),
        (1, 2, "Not a national holiday"),
        (2, 14, "Not a national holiday"),
        (3, 8, "International Women's Day"),
        (3, 19, "Not a national holiday"),
        (3, 20, "Not a national holiday"),
        (3, 21, "Navruz (Persian New Year)"),
        (3, 22, "Navruz (Persian New Year)"),
        (3, 23, "Navruz (Persian New Year)"),
        (3, 24, "Navruz (Persian New Year)"),
        (3, 25, "Not a national holiday"),
        (5, 1, "Labour Day"),
        (5, 9, "Victory Day"),
        (6, 27, "National Unity Day"),
        (7, 4, "Not a national holiday"),
        (9, 9, "Independence Day"),
        (10, 31, "Not a national holiday"),
        (11, 6, "Constitution Day"),
        (12, 25, "Not a national holiday"),
        (12, 31, "Not a national holiday"),
    ],
)
def test_tajikistan_holidays(script_runner, month, day, expected_output):
    script_path = Path(__file__).parent / "tajikistan_holidays.py"

    if not script_path.exists():
        pytest.skip("Solution file tajikistan_holidays.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{month}\n{day}\n", expected_output=expected_output
    )
