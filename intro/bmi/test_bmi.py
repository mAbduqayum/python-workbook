from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("1.75\n70.0\n", "Your BMI is: 22.86"),
        ("1.80\n85.0\n", "Your BMI is: 26.23"),
        ("1.65\n55.0\n", "Your BMI is: 20.20"),
    ],
)
def test_bmi(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "bmi.py"

    if not script_path.exists():
        pytest.skip("Solution file bmi.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
