from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("5\n", "1\n   121\n  12321\n 1234321\n123454321"),
        ("3\n", "1\n 121\n12321"),
        ("1\n", "1"),
        ("0\n", "Error"),
    ],
)
def test_number_pyramid(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "number_pyramid.py"

    if not script_path.exists():
        pytest.skip("Solution file number_pyramid.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
