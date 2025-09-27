from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "a, b, c, expected_output",
    [
        (5, 5, 3, "yes"),
        (1, 2, 3, "no"),
        (7, 3, 7, "yes"),
        (4, 4, 4, "yes"),
        (9, 2, 9, "yes"),
        (1, 1, 2, "yes"),
        (10, 20, 30, "no"),
        (0, 0, 1, "yes"),
        (-1, -1, 5, "yes"),
        (-2, 3, -2, "yes"),
    ],
)
def test_two_equal(script_runner, a, b, c, expected_output):
    script_path = Path(__file__).parent / "two_equal.py"

    if not script_path.exists():
        pytest.skip("Solution file two_equal.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{a}\n{b}\n{c}\n", expected_output=expected_output
    )