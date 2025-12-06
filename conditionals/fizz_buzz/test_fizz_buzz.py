from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "number, expected_output",
    [
        (15, "FizzBuzz"),
        (9, "Fizz"),
        (10, "Buzz"),
        (7, "7"),
        (30, "FizzBuzz"),
        (1, "1"),
        (3, "Fizz"),
        (5, "Buzz"),
        (6, "Fizz"),
        (12, "Fizz"),
        (20, "Buzz"),
        (45, "FizzBuzz"),
        (2, "2"),
        (4, "4"),
        (8, "8"),
        (0, "FizzBuzz"),  # 0 is divisible by both 3 and 5
        (-15, "FizzBuzz"),  # Test negative numbers
        (-3, "Fizz"),
        (-5, "Buzz"),
    ],
)
def test_fizz_buzz(script_runner, number, expected_output):
    script_path = Path(__file__).parent / "fizz_buzz.py"

    if not script_path.exists():
        pytest.skip("Solution file fizz_buzz.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{number}\n", expected_output=expected_output
    )
