from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("10\n20\n30\n", "The average is: 20.00"),
        ("5\n15\n25\n", "The average is: 15.00"),
        ("8\n12\n16\n", "The average is: 12.00"),
    ],
)
def test_average(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "average.py"

    if not script_path.exists():
        pytest.skip("Solution file average.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
