from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "age, expected_output",
    [
        (0, "cannot vote"),
        (17, "cannot vote"),
        (18, "can vote"),
        (25, "can vote"),
        (65, "can vote"),
    ],
)
def test_can_vote(script_runner, age, expected_output):
    script_path = Path(__file__).parent / "can_vote.py"

    if not script_path.exists():
        pytest.skip("Solution file can_vote.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{age}\n", expected_output=expected_output
    )
