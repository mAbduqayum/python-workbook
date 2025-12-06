from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("1000.00\n4.0\n3\n", "Balance after 3 years: 1127.27"),
        ("5000.00\n3.5\n2\n", "Balance after 2 years: 5361.99"),
        ("2500.00\n2.25\n1\n", "Balance after 1 years: 2556.83"),
    ],
)
def test_bank_monthly(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "bank_monthly.py"

    if not script_path.exists():
        pytest.skip("Solution file bank_monthly.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
