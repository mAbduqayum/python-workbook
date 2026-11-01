import pytest


@pytest.mark.parametrize(
    "initial_phase, final_phase, expected_output",
    [
        ("gas", "gas", "No transition"),
        ("gas", "liquid", "condensation"),
        ("gas", "solid", "deposition"),
        ("GAS", "solid", "deposition"),
        ("liquid", "gas", "vaporization"),
        ("liquid", "liquid", "No transition"),
        ("liquid", "solid", "freezing"),
        ("Liquid", "Gas", "vaporization"),
        ("solid", "gas", "sublimation"),
        ("solid", "liquid", "melting"),
        ("solid", "solid", "No transition"),
        ("SOLID", "LIQUID", "melting"),
    ],
)
def test_chemical_phase_transition(
    solution, initial_phase, final_phase, expected_output
):
    solution.check_output(
        input_text=f"{initial_phase}\n{final_phase}\n", expected_output=expected_output
    )
