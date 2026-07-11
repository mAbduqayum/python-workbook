from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "1"),
        ("3\n", "3\n2\n1"),
        ("5\n", "5\n4\n3\n2\n1"),
    ],
)
def test_countdown(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "countdown.py"

    if not script_path.exists():
        pytest.skip("Solution file countdown.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
