from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "temperature, expected_output",
    [
        (-1, "solid"),
        (-10, "solid"),
        (-273, "solid"),
        (-50, "solid"),
        (0, "solid or liquid"),
        (1, "liquid"),
        (25, "liquid"),
        (50, "liquid"),
        (99, "liquid"),
        (100, "liquid or gas"),
        (101, "gas"),
        (150, "gas"),
        (200, "gas"),
    ],
)
def test_h2o_phases(script_runner, temperature, expected_output):
    script_path = Path(__file__).parent / "h2o_phases.py"

    if not script_path.exists():
        pytest.skip("Solution file h2o_phases.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{temperature}\n", expected_output=expected_output
    )
