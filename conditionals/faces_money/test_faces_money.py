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
        (1000, "invalid denomination"),
        (0, "invalid denomination"),
        (25, "invalid denomination"),
        (250, "invalid denomination"),
    ],
)
def test_faces_money(solution, denomination, expected_output):
    solution.check_output(
        input_text=f"{denomination}\n", expected_output=expected_output
    )
