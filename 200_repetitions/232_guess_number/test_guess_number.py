from pathlib import Path

import pytest


def test_guess_number(script_runner):
    # Note: This test is skipped because the random number makes testing challenging
    # To properly test this, we would need to mock random.randint
    script_path = Path(__file__).parent / "guess_number.py"

    if not script_path.exists():
        pytest.skip("Solution file guess_number.py not found")

    # Basic smoke test - just verify it runs without crashing
    runner = script_runner(script_path)
    result = runner.run(input_text="50\n")
    assert "Too" in result.stdout or "Correct" in result.stdout
