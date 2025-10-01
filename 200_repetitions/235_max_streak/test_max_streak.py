from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n1\n1\n2\n2\n3\n3\n3\n3\n\n", "4"),
        ("5\n5\n5\n5\n5\n\n", "5"),
        ("1\n2\n3\n4\n\n", "1"),
        ("\n", "Error"),
    ],
)
def test_max_streak(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "max_streak.py"

    if not script_path.exists():
        pytest.skip("Solution file max_streak.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
