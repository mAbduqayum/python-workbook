ELEMENTS = {
    "H",
    "He",
    "Li",
    "Be",
    "B",
    "C",
    "N",
    "O",
    "F",
    "Ne",
    "Na",
    "Mg",
    "Al",
    "Si",
    "P",
    "S",
    "Cl",
    "Ar",
    "K",
    "Ca",
    "Sc",
    "Ti",
    "V",
    "Cr",
    "Mn",
    "Fe",
    "Co",
    "Ni",
    "Cu",
    "Zn",
    "Ga",
    "Ge",
    "As",
    "Se",
    "Br",
    "Kr",
    "Rb",
    "Sr",
    "Y",
    "Zr",
    "Nb",
    "Mo",
    "Tc",
    "Ru",
    "Rh",
    "Pd",
    "Ag",
    "Cd",
    "In",
    "Sn",
    "Sb",
    "Te",
    "I",
    "Xe",
    "Cs",
    "Ba",
    "La",
    "Ce",
    "Pr",
    "Nd",
    "Pm",
    "Sm",
    "Eu",
    "Gd",
    "Tb",
    "Dy",
    "Ho",
    "Er",
    "Tm",
    "Yb",
    "Lu",
    "Hf",
    "Ta",
    "W",
    "Re",
    "Os",
    "Ir",
    "Pt",
    "Au",
    "Hg",
    "Tl",
    "Pb",
    "Bi",
    "Po",
    "At",
    "Rn",
    "Fr",
    "Ra",
    "Ac",
    "Th",
    "Pa",
    "U",
    "Np",
    "Pu",
    "Am",
    "Cm",
    "Bk",
    "Cf",
    "Es",
    "Fm",
    "Md",
    "No",
    "Lr",
    "Rf",
    "Db",
    "Sg",
    "Bh",
    "Hs",
    "Mt",
    "Ds",
    "Rg",
    "Cn",
    "Nh",
    "Fl",
    "Mc",
    "Lv",
    "Ts",
    "Og",
}


def can_spell(word: str) -> bool:
    if len(word) == 0:
        return True

    # Try 1-letter symbol
    one = word[0].upper()
    if one in ELEMENTS and can_spell(word[1:]):
        return True

    # Try 2-letter symbol
    if len(word) >= 2:
        two = word[0].upper() + word[1].lower()
        if two in ELEMENTS and can_spell(word[2:]):
            return True

    return False


def spell_with_elements(word: str) -> list[str] | None:
    """Return a list of element symbols that spell the word, or None if impossible."""
    if len(word) == 0:
        return []

    # Try 1-letter symbol
    one = word[0].upper()
    if one in ELEMENTS:
        rest = spell_with_elements(word[1:])
        if rest is not None:
            return [one] + rest

    # Try 2-letter symbol
    if len(word) >= 2:
        two = word[0].upper() + word[1].lower()
        if two in ELEMENTS:
            rest = spell_with_elements(word[2:])
            if rest is not None:
                return [two] + rest

    return None


if __name__ == "__main__":
    print(can_spell("bacon"))  # True
    print(can_spell("beach"))  # True (Be-Ac-H)
    print(can_spell("since"))  # True
    print(spell_with_elements("bacon"))  # ['B', 'Ac', 'O', 'N']
    print(spell_with_elements("beach"))  # ['Be', 'Ac', 'H']
