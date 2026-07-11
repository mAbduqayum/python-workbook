from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "1"),
        ("5\n", "15"),
        ("100\n", "5050"),
    ],
)
def test_sum_to_n(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "sum_to_n.py"

    if not script_path.exists():
        pytest.skip("Solution file sum_to_n.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
