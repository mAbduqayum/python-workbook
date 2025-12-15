# Element Sequences

Some people like to play a game that constructs a sequence of chemical elements where each element in the sequence begins with the last letter of its predecessor.

For example, if a sequence begins with Hydrogen, then the next element must be an element that begins with N, such as Nickel. The element following Nickel must begin with L, such as Lithium. The element sequence that is constructed cannot contain any duplicates.

Create a recursive function that finds the longest sequence of elements starting from a given element.

**Note:** It may take your program up to two minutes to find the longest sequence for some elements. Molybdenum and Magnesium are good test cases as they find sequences quickly.

## Template

```python
ELEMENTS = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon",
    "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium",
    "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon",
    "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium",
    "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium",
    "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium",
    "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
    "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
    "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum",
    "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium",
    "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium",
    "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium",
    "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead",
    "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium",
    "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium",
    "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium",
    "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium",
    "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium",
    "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"
]


def longest_element_sequence(start: str, used: set[str] | None = None) -> list[str]:
    pass


if __name__ == "__main__":
    print(longest_element_sequence("Molybdenum"))
    # ['Molybdenum', 'Magnesium', 'Manganese', 'Europium', 'Mercury', ...]
    print(longest_element_sequence("Nickel"))
    # ['Nickel', 'Lithium', 'Magnesium', ...]
    print(longest_element_sequence("InvalidElement"))
    # []
```

<details>
<summary>Hint</summary>

- Validate the starting element against the ELEMENTS list (case-insensitive)
- Get the last letter of the current element
- Find all elements that start with that letter and haven't been used
- Recursively find the longest sequence starting from each candidate
- Keep track of used elements to avoid duplicates
- Return the longest sequence found

</details>
