# Spelling with Element Symbols

Create a recursive function that determines whether a word can be spelled using chemical element symbols.

Element symbols are one or two letters (e.g., H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, etc.).

## Template

```python
ELEMENTS = {
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
}


def can_spell(word: str) -> bool:
    pass


def spell_with_elements(word: str) -> list[str] | None:
    """Return a list of element symbols that spell the word, or None if impossible."""
    pass


if __name__ == "__main__":
    print(can_spell("bacon"))     # True (B-Ac-O-N)
    print(can_spell("beach"))     # True (Be-Ac-H)
    print(can_spell("since"))     # True (Si-N-Ce)
    print(spell_with_elements("bacon"))  # ['B', 'Ac', 'O', 'N']
    print(spell_with_elements("beach"))  # ['Be', 'Ac', 'H']
```

<details>
<summary>Hint</summary>

- Base case: empty string returns True (or empty list)
- Try matching 1-letter element symbol at start, then recurse on rest
- Try matching 2-letter element symbol at start, then recurse on rest
- Element symbols are case-sensitive (first letter uppercase, second lowercase)
- Convert input to proper case before matching

</details>
