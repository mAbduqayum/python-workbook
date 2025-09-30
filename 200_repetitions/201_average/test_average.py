from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_values, expected_output",
    [
        ("10\n20\n30\n0\n", "20.0"),
        ("5\n15\n25\n35\n0\n", "20.0"),
        ("100\n0\n", "100.0"),
        ("1\n2\n3\n4\n5\n0\n", "3.0"),
    ],
)
def test_average(script_runner, input_values, expected_output):
    script_path = Path(__file__).parent / "average.py"

    if not script_path.exists():
        pytest.skip("Solution file average.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_values)
    assert expected_output in result.stdout


def test_average_error_first_zero(script_runner):
    script_path = Path(__file__).parent / "average.py"

    if not script_path.exists():
        pytest.skip("Solution file average.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text="0\n")
    assert "error" in result.stdout.lower() or "no" in result.stdout.lower()
