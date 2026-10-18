import pytest


@pytest.mark.parametrize(
    "a, b, c, expected_output",
    [
        (1, -5, 6, "2.00 3.00"),  # Two roots: 2, 3
        (1, -4, 4, "2.00"),  # One root: 2
        (1, 2, 5, "No real roots"),  # No real roots
        (2, -7, 3, "0.50 3.00"),  # Two roots: 0.5, 3
        (1, 0, -4, "-2.00 2.00"),  # Two roots: -2, 2
        (1, -2, 1, "1.00"),  # One root: 1
        (1, 0, 1, "No real roots"),  # No real roots
        (1, -6, 9, "3.00"),  # One root: 3
        (1, -3, 2, "1.00 2.00"),  # Two roots: 1, 2
        (2, -4, 2, "1.00"),  # One root: 1
        (1, -1, -6, "-2.00 3.00"),  # Two roots: -2, 3
        (3, 2, 1, "No real roots"),  # No real roots
        (1, 0, 0, "0.00"),  # One root: 0
        (1, -7, 12, "3.00 4.00"),  # Two roots: 3, 4
    ],
)
def test_quadratic_roots(solution, a, b, c, expected_output):
    solution.check_output(
        input_text=f"{a}\n{b}\n{c}\n", expected_output=expected_output
    )
