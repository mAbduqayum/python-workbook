from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("0\n", "1"),
        ("5\n", "120"),
        ("10\n", "3628800"),
    ],
)
def test_factorial(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "factorial.py"

    if not script_path.exists():
        pytest.skip("Solution file factorial.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
