import pytest

try:
    from mark_unary import mark_unary
except ImportError:
    mark_unary = None


@pytest.mark.skipif(mark_unary is None, reason="mark_unary function not implemented")
@pytest.mark.parametrize(
    "tokens, expected",
    [
        (['-', '5', '+', '3'], ['~', '5', '+', '3']),
        (['(', '-', '5', ')', '*', '2'], ['(', '~', '5', ')', '*', '2']),
        (['3', '-', '5'], ['3', '-', '5']),
        (['-', '10'], ['~', '10']),
        (['5', '+', '-', '3'], ['5', '+', '~', '3']),
        (['(', '3', '+', '5', ')'], ['(', '3', '+', '5', ')']),
    ],
)
def test_mark_unary(tokens, expected):
    assert mark_unary(tokens) == expected
