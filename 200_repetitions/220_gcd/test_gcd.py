from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "num1, num2, expected_gcd",
    [
        ("12", "8", "4"),
        ("48", "18", "6"),
        ("17", "19", "1"),
        ("100", "50", "50"),
        ("21", "14", "7"),
        ("15", "25", "5"),
    ],
)
def test_gcd(script_runner, num1, num2, expected_gcd):
    script_path = Path(__file__).parent / "gcd.py"

    if not script_path.exists():
        pytest.skip("Solution file gcd.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=f"{num1}\n{num2}\n")

    assert expected_gcd in result.stdout
