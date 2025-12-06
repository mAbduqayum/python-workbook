from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "note, expected_output",
    [
        ("C4", "261.63"),
        ("D4", "293.66"),
        ("E4", "329.63"),
        ("F4", "349.23"),
        ("G4", "392.00"),
        ("A4", "440.00"),
        ("B4", "493.88"),
        ("X4", "Invalid note"),
        ("Z4", "Invalid note"),
        ("c4", "261.63"),  # Test case insensitivity if implemented
        ("a4", "440.00"),  # Test case insensitivity if implemented
        # Extended version tests (if implemented)
        ("C3", "130.81"),
        ("A5", "880.00"),
        ("C5", "523.26"),
        ("A3", "220.00"),
    ],
)
def test_note_frequency(script_runner, note, expected_output):
    script_path = Path(__file__).parent / "note_frequency.py"

    if not script_path.exists():
        pytest.skip("Solution file note_frequency.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{note}\n", expected_output=expected_output
    )
