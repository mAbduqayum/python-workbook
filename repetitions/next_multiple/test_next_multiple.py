import pytest


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (23, 5, "25"),
        (25, 5, "25"),
        (1, 7, "7"),
        (7, 1, "7"),
        (3, 8, "8"),
        (100, 10, "100"),
        (101, 10, "110"),
        (999, 1000, "1000"),
    ],
)
def test_next_multiple(solution, n, k, expected):
    result = solution.run(input_text=f"{n}\n{k}\n")
    assert result.stdout == expected
