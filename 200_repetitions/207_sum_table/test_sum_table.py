from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (
            "5\n",
            "0  1  2  3  4  5\n 1  2  3  4  5  6\n 2  3  4  5  6  7\n 3  4  5  6  7  8\n 4  5  6  7  8  9\n 5  6  7  8  9 10",
        ),
        ("3\n", "0  1  2  3\n 1  2  3  4\n 2  3  4  5\n 3  4  5  6"),
        ("1\n", "0  1\n 1  2"),
    ],
)
def test_sum_table(script_runner, input_text, expected):
    script_path = Path(__file__).parent / "sum_table.py"

    if not script_path.exists():
        pytest.skip("Solution file sum_table.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_text)
    assert result.stdout == expected
