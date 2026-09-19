def load_elements(file_path: str) -> dict:
    by_number = {}
    by_symbol = {}
    by_name = {}

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                number, symbol, name = parts
                by_number[number] = name
                by_symbol[symbol.lower()] = name
                by_name[name.lower()] = name

    return {"by_number": by_number, "by_symbol": by_symbol, "by_name": by_name}


def lookup_element(elements: dict, query: str) -> str | None:
    query_lower = query.lower()

    if query in elements["by_number"]:
        return elements["by_number"][query]

    if query_lower in elements["by_symbol"]:
        return elements["by_symbol"][query_lower]

    if query_lower in elements["by_name"]:
        return elements["by_name"][query_lower]

    return None


if __name__ == "__main__":
    with open("elements.txt", "w") as f:
        f.write("1 H Hydrogen\n")
        f.write("2 He Helium\n")
        f.write("6 C Carbon\n")
        f.write("8 O Oxygen\n")

    elements = load_elements("elements.txt")
    print(lookup_element(elements, "1"))  # Hydrogen
    print(lookup_element(elements, "He"))  # Helium
    print(lookup_element(elements, "Carbon"))  # Carbon
    print(lookup_element(elements, "99"))  # None
