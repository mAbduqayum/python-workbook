from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_string, is_palindrome",
    [
        ("go dog", True),
        ("flee to me remote elf", True),
        ("some men interpret nine memos", True),
        ("hello world", False),
        ("race car", True),
        ("not a palindrome", False),
    ],
)
def test_multiword_palindrome(script_runner, input_string, is_palindrome):
    script_path = Path(__file__).parent / "multiword_palindrome.py"

    if not script_path.exists():
        pytest.skip("Solution file multiword_palindrome.py not found")

    runner = script_runner(script_path)
    result = runner.run(input_text=f"{input_string}\n")

    if is_palindrome:
        assert (
            "is a palindrome" in result.stdout.lower()
            or "palindrome" in result.stdout.lower()
        )
    else:
        assert "not" in result.stdout.lower() or "isn't" in result.stdout.lower()
