from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        (
            "2\n90\n",
            "Energy required: 0.21 kWh\nCost to heat water: $0.01",
        ),
        (
            "5\n80\n",
            "Energy required: 0.47 kWh\nCost to heat water: $0.02",
        ),
        (
            "10\n75\n",
            "Energy required: 0.87 kWh\nCost to heat water: $0.03",
        ),
    ],
)
def test_heat_capacity(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "heat_capacity.py"

    if not script_path.exists():
        pytest.skip("Solution file heat_capacity.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
