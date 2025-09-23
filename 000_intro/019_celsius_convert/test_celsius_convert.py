from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("25\n", "Temperature in Fahrenheit: 77.00\nTemperature in Kelvin: 298.15"),
        ("0\n", "Temperature in Fahrenheit: 32.00\nTemperature in Kelvin: 273.15"),
        ("100\n", "Temperature in Fahrenheit: 212.00\nTemperature in Kelvin: 373.15"),
    ],
)
def test_celsius_convert(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "celsius_convert.py"

    if not script_path.exists():
        pytest.skip("Solution file celsius_convert.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
