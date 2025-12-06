from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "position, expected_output",
    [
        ("a1", "black"),
        ("a2", "white"),
        ("a7", "black"),
        ("a8", "white"),
        ("b1", "white"),
        ("b2", "black"),
        ("b7", "white"),
        ("c1", "black"),
        ("c2", "white"),
        ("c3", "black"),
        ("c7", "black"),
        ("d1", "white"),
        ("d2", "black"),
        ("d5", "white"),
        ("d7", "white"),
        ("e1", "black"),
        ("e2", "white"),
        ("e4", "white"),
        ("e7", "black"),
        ("f1", "white"),
        ("f2", "black"),
        ("f7", "white"),
        ("g1", "black"),
        ("g2", "white"),
        ("g7", "black"),
        ("h1", "white"),
        ("h2", "black"),
        ("h7", "white"),
        ("h8", "black"),
    ],
)
def test_chess_square_color(script_runner, position, expected_output):
    script_path = Path(__file__).parent / "chess_square_color.py"

    if not script_path.exists():
        pytest.skip("Solution file chess_square_color.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{position}\n", expected_output=expected_output
    )
