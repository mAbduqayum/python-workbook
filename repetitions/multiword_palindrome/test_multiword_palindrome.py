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
def test_multiword_palindrome(solution, input_string, is_palindrome):
    result = solution.run(input_text=f"{input_string}\n")

    expected = "Palindrome" if is_palindrome else "Not a palindrome"
    assert result.stdout == expected
