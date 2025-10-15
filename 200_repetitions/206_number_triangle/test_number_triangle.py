from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1\n", "1"),
        ("3\n", "1\n12\n123"),
        ("5\n", "1\n12\n123\n1234\n12345"),
    ],
)
def test_number_triangle(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "number_triangle.py"

    if not script_path.exists():
        pytest.skip("Solution file number_triangle.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
