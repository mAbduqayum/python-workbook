import pytest


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("2\n3\n5\n", "2.0\n6.0\n18.0\n54.0\n162.0"),
        ("100\n0.5\n5\n", "100.0\n50.0\n25.0\n12.5\n6.25"),
        (
            "100\n0.5\n10\n",
            "100.0\n50.0\n25.0\n12.5\n6.25\n3.125\n1.5625\n0.78125\n0.390625\n0.1953125",
        ),
        ("5\n2\n1\n", "5.0"),
    ],
)
def test_geometric_sequence(solution, input_text, expected):
    result = solution.run(input_text=input_text)
    assert result.stdout == expected
