from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("1000.00\n4.5\n3\n", "Balance after 3 years: 1141.17"),
        ("2500.00\n3.25\n5\n", "Balance after 5 years: 2933.53"),
        ("500.00\n2.8\n1\n", "Balance after 1 years: 514.00"),
    ],
)
def test_bank_annual(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "bank_annual.py"

    if not script_path.exists():
        pytest.skip("Solution file bank_annual.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
