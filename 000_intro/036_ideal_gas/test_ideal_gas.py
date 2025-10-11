from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("20000000\n12\n20\n", "Amount of gas: 98.47 moles"),
        ("101325\n22.4\n0\n", "Amount of gas: 1.00 moles"),
        ("500000\n5\n25\n", "Amount of gas: 1.01 moles"),
    ],
)
def test_ideal_gas(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "ideal_gas.py"

    if not script_path.exists():
        pytest.skip("Solution file ideal_gas.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
