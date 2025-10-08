from pathlib import Path

import pytest


def test_temperature_table(script_runner):
    script_path = Path(__file__).parent / "temperature_table.py"

    if not script_path.exists():
        pytest.skip("Solution file temperature_table.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text="")

    # Check for Celsius values
    assert "0" in result.stdout
    assert "10" in result.stdout
    assert "100" in result.stdout

    # Check for Fahrenheit conversions
    assert "32" in result.stdout  # 0°C = 32°F
    assert "212" in result.stdout  # 100°C = 212°F

    # Check for some intermediate values
    output_lines = result.stdout.lower()
    assert "celsius" in output_lines or "fahrenheit" in output_lines
