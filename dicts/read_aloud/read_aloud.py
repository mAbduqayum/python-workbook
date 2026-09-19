ONES = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
}

TEENS = {
    10: "TEN",
    11: "ELEVEN",
    12: "TWELVE",
    13: "THIRTEEN",
    14: "FOURTEEN",
    15: "FIFTEEN",
    16: "SIXTEEN",
    17: "SEVENTEEN",
    18: "EIGHTEEN",
    19: "NINETEEN",
}

TENS = {
    20: "TWENTY",
    30: "THIRTY",
    40: "FORTY",
    50: "FIFTY",
    60: "SIXTY",
    70: "SEVENTY",
    80: "EIGHTY",
    90: "NINETY",
}


def read_below_hundred(num: int) -> str:
    if num < 10:
        return ONES[num]
    if num < 20:
        return TEENS[num]

    tens_digit = num // 10 * 10
    ones_digit = num % 10
    if ones_digit == 0:
        return TENS[tens_digit]
    return TENS[tens_digit] + " " + ONES[ones_digit]


def read_aloud(number: str) -> str:
    if not number:
        return ""

    num = int(number)

    if num == 0:
        return "ZERO"
    if num < 100:
        return read_below_hundred(num)
    if num < 1000:
        hundreds = ONES[num // 100] + " HUNDRED"
        remainder = num % 100
        if remainder == 0:
            return hundreds
        return hundreds + " " + read_below_hundred(remainder)

    return ""


if __name__ == "__main__":
    print(read_aloud("7"))  # "SEVEN"
    print(read_aloud("15"))  # "FIFTEEN"
    print(read_aloud("42"))  # "FORTY TWO"
    print(read_aloud("90"))  # "NINETY"
    print(read_aloud("100"))  # "ONE HUNDRED"
    print(read_aloud("105"))  # "ONE HUNDRED FIVE"
    print(read_aloud("333"))  # "THREE HUNDRED THIRTY THREE"
    print(read_aloud("0"))  # "ZERO"
    print(read_aloud(""))  # ""
