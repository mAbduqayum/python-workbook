# Element Lookup

Create functions to load chemical elements from a file and look them up by various criteria.

## Template

```python
def load_elements(file_path: str) -> dict:
    pass


def lookup_element(elements: dict, query: str) -> str | None:
    pass


if __name__ == "__main__":
    # Create an elements data file
    with open("elements.txt", "w") as f:
        f.write("1 H Hydrogen\n")
        f.write("2 He Helium\n")
        f.write("6 C Carbon\n")
        f.write("8 O Oxygen\n")

    # Test your functions
    elements = load_elements("elements.txt")

    # Lookup by atomic number
    print(lookup_element(elements, "1"))  # Hydrogen

    # Lookup by symbol
    print(lookup_element(elements, "He"))  # Helium

    # Lookup by name
    print(lookup_element(elements, "Carbon"))  # Carbon

    # Not found
    print(lookup_element(elements, "99"))  # None
```

## Note

- File format: Each line contains `atomic_number symbol name` (space-separated)
- `load_elements` should return a dict with three keys:
  - "by_number": dict mapping atomic number (as string) to element name
  - "by_symbol": dict mapping symbol to element name
  - "by_name": dict mapping name to element name
- `lookup_element` should check all three mappings and return the element name
- Lookups should be case-insensitive for symbols and names
- Return `None` if the element is not found
