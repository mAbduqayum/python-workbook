import pytest

try:
    from element_spelling import can_spell, spell_with_elements
except ImportError:
    can_spell = None
    spell_with_elements = None


@pytest.mark.skipif(can_spell is None, reason="can_spell not implemented")
@pytest.mark.parametrize(
    "word, expected",
    [
        ("bacon", True),
        ("beach", True),  # Be-Ac-H
        ("since", True),
        ("", True),
        ("h", True),
        ("he", True),
        ("no", True),
        ("yes", True),
        ("fun", True),
        ("xyz", False),
    ],
)
def test_can_spell(word, expected):
    assert can_spell(word) == expected


@pytest.mark.skipif(
    spell_with_elements is None, reason="spell_with_elements not implemented"
)
@pytest.mark.parametrize(
    "word, expected",
    [
        ("bacon", ["B", "Ac", "O", "N"]),
        ("beach", ["Be", "Ac", "H"]),
        ("", []),
    ],
)
def test_spell_with_elements(word, expected):
    assert spell_with_elements(word) == expected
