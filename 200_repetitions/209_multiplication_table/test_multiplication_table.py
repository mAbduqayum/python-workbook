from pathlib import Path

import pytest


def test_multiplication_table(script_runner):
    script_path = Path(__file__).parent / "multiplication_table.py"

    if not script_path.exists():
        pytest.skip("Solution file multiplication_table.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text="")

    # Check for presence of key products
    assert "100" in result.stdout  # 10 × 10
    assert "81" in result.stdout  # 9 × 9
    assert "64" in result.stdout  # 8 × 8
    assert "49" in result.stdout  # 7 × 7

    # Check that output contains multiple lines (should be at least 11: header + 10 rows)
    lines = result.stdout.strip().split("\n")
    assert len(lines) >= 10
