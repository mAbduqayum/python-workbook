from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_values, expected_outputs",
    [
        ("00000000\n\n", ["0"]),
        ("11111111\n\n", ["0"]),
        ("10101010\n\n", ["0"]),
        ("10101011\n\n", ["1"]),
        ("00000001\n\n", ["1"]),
        ("11110000\n\n", ["0"]),
    ],
)
def test_parity_bits(script_runner, input_values, expected_outputs):
    script_path = Path(__file__).parent / "parity_bits.py"

    if not script_path.exists():
        pytest.skip("Solution file parity_bits.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_values)

    for expected in expected_outputs:
        assert expected in result.stdout


def test_parity_bits_error(script_runner):
    script_path = Path(__file__).parent / "parity_bits.py"

    if not script_path.exists():
        pytest.skip("Solution file parity_bits.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text="1010\n\n")

    assert "error" in result.stdout.lower()
