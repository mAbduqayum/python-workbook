from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "angle, expected_output",
    [
        (-180, "On axis"),
        (-135, "Quadrant III"),
        (-90, "On axis"),
        (-45, "Quadrant IV"),
        (-30, "Quadrant IV"),
        (0, "On axis"),
        (1, "Quadrant I"),
        (90, "On axis"),
        (120, "Quadrant II"),
        (180, "On axis"),
        (225, "Quadrant III"),
        (270, "On axis"),
        (315, "Quadrant IV"),
        (359, "Quadrant IV"),
        (360, "On axis"),
        (405, "Quadrant I"),
        (45, "Quadrant I"),
        (450, "On axis"),
        (720, "On axis"),
        (810, "On axis"),
    ],
)
def test_angle_quadrants(script_runner, angle, expected_output):
    script_path = Path(__file__).parent / "angle_quadrants.py"

    if not script_path.exists():
        pytest.skip("Solution file angle_quadrants.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{angle}\n", expected_output=expected_output
    )
