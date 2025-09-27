from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "number, expected_output",
    [
        (5, "positive"),
        (-3, "negative"),
        (0, "zero"),
        (100, "positive"),
        (-100, "negative"),
        (1, "positive"),
        (-1, "negative"),
    ],
)
def test_number_sign(script_runner, number, expected_output):
    script_path = Path(__file__).parent / "number_sign.py"

    if not script_path.exists():
        pytest.skip("Solution file number_sign.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{number}\n", expected_output=expected_output
    )