import pytest

try:
    from infix_to_postfix import infix_to_postfix
except ImportError:
    infix_to_postfix = None


@pytest.mark.skipif(infix_to_postfix is None, reason="infix_to_postfix function not implemented")
@pytest.mark.parametrize(
    "infix, expected",
    [
        (['3', '+', '5', '*', '2'], ['3', '5', '2', '*', '+']),
        (['(', '3', '+', '5', ')', '*', '2'], ['3', '5', '+', '2', '*']),
        (['3', '+', '5'], ['3', '5', '+']),
        (['3', '*', '5'], ['3', '5', '*']),
        (['3', '+', '5', '+', '2'], ['3', '5', '+', '2', '+']),
        (['(', '3', '+', '5', ')'], ['3', '5', '+']),
    ],
)
def test_infix_to_postfix(infix, expected):
    assert infix_to_postfix(infix) == expected
