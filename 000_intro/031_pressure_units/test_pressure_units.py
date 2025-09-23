from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        (
            "101.325\n",
            "Pressure in pascals: 101325.00\nPressure in bars: 1.01\nPressure in atmospheres: 1.00",
        ),
        (
            "200\n",
            "Pressure in pascals: 200000.00\nPressure in bars: 2.00\nPressure in atmospheres: 1.97",
        ),
        (
            "50\n",
            "Pressure in pascals: 50000.00\nPressure in bars: 0.50\nPressure in atmospheres: 0.49",
        ),
    ],
)
def test_pressure_units(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "pressure_units.py"

    if not script_path.exists():
        pytest.skip("Solution file pressure_units.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
