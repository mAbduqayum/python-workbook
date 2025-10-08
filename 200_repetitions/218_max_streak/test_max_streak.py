from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n1\n1\n0\n1\n1\n\n", "Maximum streak: 3"),
        ("1\n1\n1\n1\n1\n\n", "Maximum streak: 5"),
        ("0\n1\n0\n1\n1\n1\n0\n\n", "Maximum streak: 3"),
        ("0\n0\n0\n\n", "Maximum streak: 0"),
    ],
)
def test_max_streak(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "max_streak.py"

    if not script_path.exists():
        pytest.skip("Solution file max_streak.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
