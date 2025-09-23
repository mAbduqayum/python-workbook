from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("2\n3\n45\n30\n", "Total seconds: 186330"),
        ("1\n0\n30\n0\n", "Total seconds: 88200"),
        ("0\n2\n15\n45\n", "Total seconds: 8145"),
    ],
)
def test_time_units(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "time_units.py"

    if not script_path.exists():
        pytest.skip("Solution file time_units.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
