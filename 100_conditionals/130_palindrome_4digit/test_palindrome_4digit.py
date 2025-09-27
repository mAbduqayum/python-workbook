from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "number, expected_output",
    [
        (1221, "palindrome"),
        (9009, "palindrome"),
        (7337, "palindrome"),
        (1111, "palindrome"),
        (1001, "palindrome"),
        (2002, "palindrome"),
        (3003, "palindrome"),
        (4004, "palindrome"),
        (5005, "palindrome"),
        (6006, "palindrome"),
        (7007, "palindrome"),
        (8008, "palindrome"),
        (1991, "palindrome"),
        (1881, "palindrome"),
        (1771, "palindrome"),
        (1661, "palindrome"),
        (1551, "palindrome"),
        (1441, "palindrome"),
        (1331, "palindrome"),
        (9999, "palindrome"),
        (1000, "not palindrome"),
        (2000, "not palindrome"),
        (3000, "not palindrome"),
        (4567, "not palindrome"),
        (8765, "not palindrome"),
        (1234, "not palindrome"),
        (5678, "not palindrome"),
        (1234, "not palindrome"),
    ],
)
def test_palindrome_4digit(script_runner, number, expected_output):
    script_path = Path(__file__).parent / "palindrome_4digit.py"

    if not script_path.exists():
        pytest.skip("Solution file palindrome_4digit.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{number}\n", expected_output=expected_output
    )
