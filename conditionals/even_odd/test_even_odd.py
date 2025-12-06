from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "number, expected_output",
    [
        (7, "odd"),
        (4, "even"),
        (0, "even"),
        (-3, "odd"),
        (-2, "even"),
        (100, "even"),
        (101, "odd"),
    ],
)
def test_even_odd(script_runner, number, expected_output):
    script_path = Path(__file__).parent / "even_odd.py"

    if not script_path.exists():
        pytest.skip("Solution file even_odd.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{number}\n", expected_output=expected_output
    )
