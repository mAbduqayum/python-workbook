from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "first_num, second_num, expected_output",
    [
        (
            15,
            4,
            "15 + 4 = 19\n15 - 4 = 11\n15 * 4 = 60\n15 / 4 = 3.75\n15 // 4 = 3\n15 % 4 = 3\n15 ** 4 = 50625",
        ),
        (
            20,
            6,
            "20 + 6 = 26\n20 - 6 = 14\n20 * 6 = 120\n20 / 6 = 3.33\n20 // 6 = 3\n20 % 6 = 2\n20 ** 6 = 64000000",
        ),
        (
            8,
            3,
            "8 + 3 = 11\n8 - 3 = 5\n8 * 3 = 24\n8 / 3 = 2.67\n8 // 3 = 2\n8 % 3 = 2\n8 ** 3 = 512",
        ),
    ],
)
def test_advanced_calculator(script_runner, first_num, second_num, expected_output):
    script_path = Path(__file__).parent / "advanced_calculator.py"

    if not script_path.exists():
        pytest.skip("Solution file advanced_calculator.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{first_num}\n{second_num}\n", expected_output=expected_output
    )
