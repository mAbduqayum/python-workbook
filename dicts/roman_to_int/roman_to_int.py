ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(roman: str) -> int:
    total = 0
    for i in range(len(roman)):
        current = ROMAN[roman[i]]
        if i + 1 < len(roman) and current < ROMAN[roman[i + 1]]:
            total -= current
        else:
            total += current
    return total


if __name__ == "__main__":
    print(roman_to_int("III"))  # 3
    print(roman_to_int("IV"))  # 4
    print(roman_to_int("IX"))  # 9
    print(roman_to_int("LVIII"))  # 58
    print(roman_to_int("MCMXCIV"))  # 1994
    print(roman_to_int("I"))  # 1
    print(roman_to_int("XIV"))  # 14
