from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "decimal_input, expected_binary",
    [
        ("10", "1010"),
        ("15", "1111"),
        ("42", "101010"),
        ("1", "1"),
        ("0", "0"),
        ("255", "11111111"),
        ("16", "10000"),
    ],
)
def test_decimal_to_binary(script_runner, decimal_input, expected_binary):
    script_path = Path(__file__).parent / "decimal_to_binary.py"

    if not script_path.exists():
        pytest.skip("Solution file decimal_to_binary.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=f"{decimal_input}\n")

    assert expected_binary in result.stdout
