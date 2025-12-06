from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("3\n", "The volume is: 113.10"),
        ("5\n", "The volume is: 523.60"),
        ("2\n", "The volume is: 33.51"),
    ],
)
def test_sphere_volume(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "sphere_volume.py"

    if not script_path.exists():
        pytest.skip("Solution file sphere_volume.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
