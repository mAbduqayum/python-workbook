from pathlib import Path

import pytest


def test_sum_table(script_runner):
    script_path = Path(__file__).parent / "sum_table.py"

    if not script_path.exists():
        pytest.skip("Solution file sum_table.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text="")

    assert "18" in result.stdout  # 9 + 9
    assert "16" in result.stdout  # 8 + 8
    assert "14" in result.stdout  # 7 + 7

    lines = result.stdout.strip().split("\n")
    assert len(lines) == 10
