from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "a, b, c, expected_output",
    [
        (5, 7, 10, "between"),
        (10, 7, 5, "between"),
        (5, 12, 10, "not between"),
        (5, 5, 10, "between"),
        (10, 5, 5, "between"),
        (5, 10, 10, "between"),
        (10, 10, 5, "between"),
        (1, 3, 5, "between"),
        (5, 3, 1, "between"),
        (1, 6, 5, "not between"),
        (5, 6, 1, "not between"),
        (0, 0, 0, "between"),
        (-5, -3, -1, "between"),
        (-1, -3, -5, "between"),
        (-5, 0, -1, "not between"),
        (100, 50, 200, "not between"),
        (200, 50, 100, "not between"),
    ],
)
def test_between_values(script_runner, a, b, c, expected_output):
    script_path = Path(__file__).parent / "between_values.py"

    if not script_path.exists():
        pytest.skip("Solution file between_values.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{a}\n{b}\n{c}\n", expected_output=expected_output
    )
