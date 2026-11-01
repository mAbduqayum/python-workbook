import pytest

try:
    from evaluate_expression import evaluate_expression
except ImportError as missing:
    # This exercise imports the functions of four earlier ones, so the import
    # can fail for several reasons. Name the one that actually failed instead
    # of always blaming evaluate_expression.
    unresolved = missing.name
else:
    unresolved = None

pytestmark = pytest.mark.skipif(
    unresolved is not None, reason=f"{unresolved} not implemented"
)


@pytest.mark.parametrize(
    "expr, expected",
    [
        ("5", 5.0),
        ("3 + 5", 8.0),
        ("15 - 7 + 2", 10.0),
        ("3 + 5 * 2", 13.0),
        ("(10 + 20) * 3", 90.0),
        ("10 / 4", 2.5),
        ("2 ^ 3 + 1", 9.0),
        ("-5 + 3 * 2", 1.0),
        ("2 * -3", -6.0),
        ("-(2 + 3)", -5.0),
        ("(-2 + 5) * 3", 9.0),
        ("10 - -3", 13.0),
    ],
)
def test_evaluate_expression(expr, expected):
    assert evaluate_expression(expr) == pytest.approx(expected)
