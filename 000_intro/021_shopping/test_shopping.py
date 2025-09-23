from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_params, expected_output",
    [
        ("12.50\n3\n", "Total cost: 37.50"),
        ("8.99\n2\n", "Total cost: 17.98"),
        ("15.00\n4\n", "Total cost: 60.00"),
    ],
)
def test_shopping(script_runner, input_params, expected_output):
    script_path = Path(__file__).parent / "shopping.py"

    if not script_path.exists():
        pytest.skip("Solution file shopping.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=input_params, expected_output=expected_output
    )
