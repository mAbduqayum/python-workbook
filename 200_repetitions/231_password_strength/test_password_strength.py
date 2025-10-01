import pytest
from tests.grading import test_input_output


@pytest.mark.parametrize("inputs, expected", [
    (["Hello123"], "Strong"),
    (["hello123"], "Moderate"),
    (["HELLO123"], "Moderate"),
    (["HelloWorld"], "Moderate"),
    (["hello"], "Weak"),
    (["12345"], "Weak"),
    ([""], "Weak"),
])
def test_password_strength(inputs, expected):
    test_input_output("200_repetitions/231_password_strength/password_strength.py", inputs, expected)
