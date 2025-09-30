from pathlib import Path

import pytest


def test_discount_table(script_runner):
    script_path = Path(__file__).parent / "discount_table.py"

    if not script_path.exists():
        pytest.skip("Solution file discount_table.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text="")
    
    # Check for all original prices
    assert "4.95" in result.stdout
    assert "9.95" in result.stdout
    assert "14.95" in result.stdout
    assert "19.95" in result.stdout
    assert "24.95" in result.stdout
    
    # Check for some calculated values (60% discount means 40% of original price)
    assert "1.98" in result.stdout  # 4.95 * 0.4
    assert "3.98" in result.stdout  # 9.95 * 0.4
    assert "5.98" in result.stdout  # 14.95 * 0.4
    assert "7.98" in result.stdout  # 19.95 * 0.4
    assert "9.98" in result.stdout  # 24.95 * 0.4
