from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "letter, expected_output",
    [
        ("a", "vowel"),
        ("b", "consonant"),
        ("y", "sometimes vowel, sometimes consonant"),
        ("A", "vowel"),
        ("e", "vowel"),
        ("i", "vowel"),
        ("o", "vowel"),
        ("u", "vowel"),
        ("E", "vowel"),
        ("I", "vowel"),
        ("O", "vowel"),
        ("U", "vowel"),
        ("Y", "sometimes vowel, sometimes consonant"),
        ("z", "consonant"),
        ("Z", "consonant"),
        ("m", "consonant"),
    ],
)
def test_vowel_consonant(script_runner, letter, expected_output):
    script_path = Path(__file__).parent / "vowel_consonant.py"

    if not script_path.exists():
        pytest.skip("Solution file vowel_consonant.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{letter}\n", expected_output=expected_output
    )