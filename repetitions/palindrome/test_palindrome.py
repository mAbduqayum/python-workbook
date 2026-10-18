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
def test_palindrome(solution, input_string, is_palindrome):
    result = solution.run(input_text=f"{input_string}\n")

    expected = "Palindrome" if is_palindrome else "Not a palindrome"
    assert result.stdout == expected
