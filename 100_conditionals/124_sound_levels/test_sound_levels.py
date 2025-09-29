from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "decibel_level, expected_output",
    [
        (0, "Quieter than Quiet Room"),
        (25, "Quieter than Quiet Room"),
        (35, "Quieter than Quiet Room"),
        (40, "Quiet Room"),
        (50, "Between Quiet Room and Alarm Clock"),
        (55, "Between Quiet Room and Alarm Clock"),
        (70, "Alarm Clock"),
        (80, "Between Alarm Clock and Gas Lawnmower"),
        (90, "Between Alarm Clock and Gas Lawnmower"),
        (106, "Gas Lawnmower"),
        (115, "Between Gas Lawnmower and Jackhammer"),
        (120, "Between Gas Lawnmower and Jackhammer"),
        (130, "Jackhammer"),
        (140, "Louder than Jackhammer"),
        (145, "Louder than Jackhammer"),
        (200, "Louder than Jackhammer"),
    ],
)
def test_sound_levels(script_runner, decibel_level, expected_output):
    script_path = Path(__file__).parent / "sound_levels.py"

    if not script_path.exists():
        pytest.skip("Solution file sound_levels.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{decibel_level}\n", expected_output=expected_output
    )
