from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "denomination, expected_output",
    [
        (1, "Mirzo Tursunzoda"),
        (3, "Shirinsho Shotemur"),
        (5, "Sadriddin Ayni"),
        (10, "Mir Said Ali Hamadoni"),
        (20, "Abuali ibni Sino"),
        (50, "Bobojon Gafurov"),
        (100, "Ismoili Somoni"),
        (200, "Nusratullo Makhsum"),
        (500, "Abuabdullo Rudaki"),
        (1000, "Invalid denomination"),
        (0, "Invalid denomination"),
        (25, "Invalid denomination"),
        (250, "Invalid denomination"),
    ],
)
def test_faces_money(script_runner, denomination, expected_output):
    script_path = Path(__file__).parent / "faces_money.py"

    if not script_path.exists():
        pytest.skip("Solution file faces_money.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{denomination}\n", expected_output=expected_output
    )