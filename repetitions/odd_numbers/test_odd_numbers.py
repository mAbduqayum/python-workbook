from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("9\n", "1\n3\n5\n7\n9"),
        ("6\n", "1\n3\n5"),
        ("1\n", "1"),
    ],
)
def test_odd_numbers(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "odd_numbers.py"

    if not script_path.exists():
        pytest.skip("Solution file odd_numbers.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
