from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        (
            "250\n75\n",
            "Energy required: 78487.50 Joules\nCost to heat water: 0.00 euros",
        ),
        (
            "1000\n80\n",
            "Energy required: 334880.00 Joules\nCost to heat water: 0.01 euros",
        ),
        (
            "500\n95\n",
            "Energy required: 198835.00 Joules\nCost to heat water: 0.00 euros",
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
