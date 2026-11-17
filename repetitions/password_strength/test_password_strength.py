import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Hello123!@#\n", "very strong"),
        ("Hello123\n", "strong"),
        ("hello123\n", "medium"),
        ("HELLO123\n", "medium"),
        ("HelloWorld\n", "medium"),
        ("Hel!23\n", "strong"),
        ("hello\n", "very weak"),
        ("12345\n", "very weak"),
    ],
)
def test_password_strength(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
