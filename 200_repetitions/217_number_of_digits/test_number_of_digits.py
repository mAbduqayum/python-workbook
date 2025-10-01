from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("12345\n", "5"),
        ("-987\n", "3"),
        ("0\n", "1"),
        ("7\n", "1"),
        ("1000000\n", "7"),
    ],
)
def test_number_of_digits(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "number_of_digits.py"

    if not script_path.exists():
        pytest.skip("Solution file number_of_digits.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
