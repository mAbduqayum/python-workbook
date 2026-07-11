from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "1"),
        ("3\n", "1\n2\n3"),
        ("5\n", "1\n2\n3\n4\n5"),
    ],
)
def test_first_n_numbers(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "first_n_numbers.py"

    if not script_path.exists():
        pytest.skip("Solution file first_n_numbers.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
