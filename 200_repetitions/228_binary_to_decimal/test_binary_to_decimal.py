from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "binary_input, expected_decimal",
    [
        ("1010", "10"),
        ("1111", "15"),
        ("10000", "16"),
        ("1", "1"),
        ("0", "0"),
        ("11111111", "255"),
        ("101010", "42"),
    ],
)
def test_binary_to_decimal(script_runner, binary_input, expected_decimal):
    script_path = Path(__file__).parent / "binary_to_decimal.py"

    if not script_path.exists():
        pytest.skip("Solution file binary_to_decimal.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=f"{binary_input}\n")

    assert expected_decimal in result.stdout
