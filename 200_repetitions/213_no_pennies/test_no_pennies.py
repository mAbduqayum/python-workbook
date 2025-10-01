from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_values, expected_total, expected_cash",
    [
        ("10.25\n5.78\n3.12\n\n", "19.15", "19.15"),
        ("4.99\n2.48\n1.22\n\n", "8.69", "8.70"),
        ("7.53\n3.21\n\n", "10.74", "10.75"),
        ("1.01\n\n", "1.01", "1.00"),
        ("1.03\n\n", "1.03", "1.05"),
    ],
)
def test_no_pennies(script_runner, input_values, expected_total, expected_cash):
    script_path = Path(__file__).parent / "no_pennies.py"

    if not script_path.exists():
        pytest.skip("Solution file no_pennies.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=input_values)
    
    assert expected_total in result.stdout
    assert expected_cash in result.stdout
