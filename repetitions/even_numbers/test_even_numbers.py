from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("10\n", "2\n4\n6\n8\n10"),
        ("7\n", "2\n4\n6"),
        ("2\n", "2"),
    ],
)
def test_even_numbers(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "even_numbers.py"

    if not script_path.exists():
        pytest.skip("Solution file even_numbers.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
