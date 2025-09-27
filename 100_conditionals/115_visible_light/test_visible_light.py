from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "wavelength, expected_output",
    [
        (300, "Outside visible spectrum"),
        (379, "Outside visible spectrum"), # Just below visible
        (380, "Violet"),  # Lower boundary of violet
        (420, "Violet"),
        (449, "Violet"),  # Just below blue
        (450, "Blue"),   # Lower boundary of blue
        (480, "Blue"),
        (494, "Blue"),   # Just below green
        (495, "Green"),  # Lower boundary of green
        (550, "Green"),
        (569, "Green"),  # Just below yellow
        (570, "Yellow"), # Lower boundary of yellow
        (580, "Yellow"),
        (589, "Yellow"), # Just below orange
        (590, "Orange"), # Lower boundary of orange
        (600, "Orange"),
        (619, "Orange"), # Just below red
        (620, "Red"),    # Lower boundary of red
        (700, "Red"),
        (750, "Red"),    # Upper boundary of red
        (751, "Outside visible spectrum"), # Just above visible
        (800, "Outside visible spectrum"),
    ],
)
def test_visible_light(script_runner, wavelength, expected_output):
    script_path = Path(__file__).parent / "visible_light.py"

    if not script_path.exists():
        pytest.skip("Solution file visible_light.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{wavelength}\n", expected_output=expected_output
    )
