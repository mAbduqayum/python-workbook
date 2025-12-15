def run_length_encode(text: str) -> str:
    if len(text) == 0:
        return ""

    # Count consecutive occurrences of first character
    char = text[0]
    count = 1
    while count < len(text) and text[count] == char:
        count += 1

    return str(count) + char + run_length_encode(text[count:])


if __name__ == "__main__":
    print(run_length_encode("AAABBC"))  # "3A2B1C"
    print(run_length_encode("Hello"))  # "1H1e2l1o"
    print(run_length_encode("XXXXX"))  # "5X"
    print(run_length_encode(""))  # ""
    print(run_length_encode("AABBBCCCC"))  # "2A3B4C"
