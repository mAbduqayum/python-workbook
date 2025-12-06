from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("45.50\n18\n", "Tip amount: 8.19\nTotal amount: 53.69"),
        ("30.00\n20\n", "Tip amount: 6.00\nTotal amount: 36.00"),
        ("85.75\n15\n", "Tip amount: 12.86\nTotal amount: 98.61"),
    ],
)
def test_tip_calculator(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "tip_calculator.py"

    if not script_path.exists():
        pytest.skip("Solution file tip_calculator.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
