def run_length_decode(encoded: str) -> str:
    if len(encoded) == 0:
        return ""

    # Parse the count (may be multiple digits)
    i = 0
    while i < len(encoded) and encoded[i].isdigit():
        i += 1

    count = int(encoded[:i])
    char = encoded[i]

    return char * count + run_length_decode(encoded[i + 1 :])


if __name__ == "__main__":
    print(run_length_decode("3A2B1C"))  # "AAABBC"
    print(run_length_decode("1H1e1l1l1o"))  # "Hello"
    print(run_length_decode("5X"))  # "XXXXX"
    print(run_length_decode(""))  # ""
    print(run_length_decode("12A3B"))  # "AAAAAAAAAAAABBB"
