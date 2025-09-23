from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("8\n3\n12\n", "Sorted order: 3, 8, 12"),
        ("15\n7\n15\n", "Sorted order: 7, 15, 15"),
        ("-5\n10\n0\n", "Sorted order: -5, 0, 10"),
    ],
)
def test_sort_integers(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "sort_integers.py"

    if not script_path.exists():
        pytest.skip("Solution file sort_integers.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
