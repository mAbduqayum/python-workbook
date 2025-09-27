from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "initial_phase, final_phase, expected_output",
    [
        ("gas", "gas", "No transition"),
        ("gas", "liquid", "condensation"),
        ("gas", "plasma", "ionization"),
        ("gas", "solid", "deposition"),
        ("GAS", "solid", "deposition"),
        ("liquid", "gas", "vaporization"),
        ("liquid", "liquid", "No transition"),
        ("liquid", "plasma", "Cannot transition directly"),
        ("liquid", "solid", "freezing"),
        ("Liquid", "Gas", "vaporization"),
        ("solid", "gas", "sublimation"),
        ("solid", "liquid", "melting"),
        ("solid", "plasma", "Cannot transition directly"),
        ("solid", "solid", "No transition"),
        ("SOLID", "LIQUID", "melting"),
        ("plasma", "gas", "recombination"),
        ("plasma", "liquid", "Cannot transition directly"),
        ("plasma", "plasma", "No transition"),
        ("plasma", "solid", "Cannot transition directly"),
        ("Plasma", "GAS", "recombination"),
    ],
)
def test_chemical_phase_transition(script_runner, initial_phase, final_phase, expected_output):
    script_path = Path(__file__).parent / "chemical_phase_transition.py"

    if not script_path.exists():
        pytest.skip("Solution file chemical_phase_transition.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{initial_phase}\n{final_phase}\n", expected_output=expected_output
    )
