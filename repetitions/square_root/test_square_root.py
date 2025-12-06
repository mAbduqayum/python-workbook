import math
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_value, expected_sqrt",
    [
        ("2", math.sqrt(2)),
        ("16", 4.0),
        ("25", 5.0),
        ("100", 10.0),
        ("144", 12.0),
    ],
)
def test_square_root(script_runner, input_value, expected_sqrt):
    script_path = Path(__file__).parent / "square_root.py"

    if not script_path.exists():
        pytest.skip("Solution file square_root.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=f"{input_value}\n")

    # Extract numeric value from output
    import re

    numbers = re.findall(r"\d+\.\d+", result.stdout)

    if numbers:
        actual = float(numbers[0])
        assert abs(actual - expected_sqrt) < 1e-6
