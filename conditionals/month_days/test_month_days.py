from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "month, expected_output",
    [
        ("January", "31"),
        ("february", "28 or 29"),
        ("March", "31"),
        ("April", "30"),
        ("May", "31"),
        ("June", "30"),
        ("July", "31"),
        ("August", "31"),
        ("September", "30"),
        ("October", "31"),
        ("November", "30"),
        ("DECEMBER", "31"),
        ("xyz", "Invalid month"),
        ("", "Invalid month"),
        ("jan", "Invalid month"),
    ],
)
def test_month_days(script_runner, month, expected_output):
    script_path = Path(__file__).parent / "month_days.py"

    if not script_path.exists():
        pytest.skip("Solution file month_days.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{month}\n", expected_output=expected_output
    )
