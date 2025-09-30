from pathlib import Path

import pytest


def test_coin_flip(script_runner):
    script_path = Path(__file__).parent / "coin_flip.py"

    if not script_path.exists():
        pytest.skip("Solution file coin_flip.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text="")
    
    # Check for key elements in output
    assert "flip" in result.stdout.lower()
    assert "average" in result.stdout.lower()
    
    # Should have H and T characters
    assert "H" in result.stdout or "T" in result.stdout
    
    # Check that there are 10 simulation lines
    lines = result.stdout.strip().split('\n')
    flip_lines = [line for line in lines if 'H' in line or 'T' in line]
    
    # Should have at least 10 simulation results
    assert len(flip_lines) >= 10
