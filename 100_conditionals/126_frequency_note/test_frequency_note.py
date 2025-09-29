from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "frequency, expected_output",
    [
        (200.0, "No match"),        # Too low
        (260.63, "C4"),             # Lower boundary of C4
        (261.0, "C4"),              # Within 1 Hz of 261.63
        (262.5, "C4"),              # Within 1 Hz of 261.63
        (262.63, "C4"),             # Upper boundary of C4
        (292.66, "D4"),             # Lower boundary of D4
        (294.66, "D4"),             # Upper boundary of D4
        (300.0, "No match"),        # Between notes
        (328.63, "E4"),             # Lower boundary of E4
        (330.63, "E4"),             # Upper boundary of E4
        (348.23, "F4"),             # Lower boundary of F4
        (350.23, "F4"),             # Upper boundary of F4
        (391.0, "G4"),              # Lower boundary of G4
        (392.8, "G4"),              # Within 1 Hz of 392.00
        (393.0, "G4"),              # Upper boundary of G4
        (439.0, "A4"),              # Lower boundary of A4
        (440.0, "A4"),              # Exact match
        (441.0, "A4"),              # Upper boundary of A4
        (492.88, "B4"),             # Lower boundary of B4
        (494.88, "B4"),             # Upper boundary of B4
        (500.0, "No match"),        # No close match
        (600.0, "No match"),        # Too high
    ],
)
def test_frequency_note(script_runner, frequency, expected_output):
    script_path = Path(__file__).parent / "frequency_note.py"

    if not script_path.exists():
        pytest.skip("Solution file frequency_note.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{frequency}\n", expected_output=expected_output
    )
