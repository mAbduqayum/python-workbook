from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("5\n20\n3\n", "5\n8\n11\n14\n17\n20"),
        ("10\n1\n-2\n", "10\n8\n6\n4\n2"),
        ("1\n1\n1\n", "1"),
    ],
)
def test_arithmetic_sequence(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "arithmetic_sequence.py"

    if not script_path.exists():
        pytest.skip("Solution file arithmetic_sequence.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
