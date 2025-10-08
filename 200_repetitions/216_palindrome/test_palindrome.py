from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_string, is_palindrome",
    [
        ("anna", True),
        ("civic", True),
        ("level", True),
        ("hannah", True),
        ("racecar", True),
        ("hello", False),
        ("world", False),
        ("python", False),
        ("a", True),
        ("aa", True),
        ("ab", False),
    ],
)
def test_palindrome(script_runner, input_string, is_palindrome):
    script_path = Path(__file__).parent / "palindrome.py"

    if not script_path.exists():
        pytest.skip("Solution file palindrome.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=f"{input_string}\n")

    if is_palindrome:
        assert (
            "is a palindrome" in result.stdout.lower()
            or "palindrome" in result.stdout.lower()
        )
    else:
        assert "not" in result.stdout.lower() or "isn't" in result.stdout.lower()
