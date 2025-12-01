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


def read_aloud(number: str) -> str:
    if not number:
        return ""

    num = int(number)

    if num == 0:
        return "ZERO"
    if num < 10:
        return ONES[num]
    if num < 20:
        return TEENS[num]
    if num < 100:
        tens_digit = num // 10 * 10
        ones_digit = num % 10
        if ones_digit == 0:
            return TENS[tens_digit]
        else:
            return TENS[tens_digit] + " " + ONES[ones_digit]
    if num < 1000:
        hundreds_digit = num // 100
        remainder = num % 100
        result = ONES[hundreds_digit] + " HUNDRED"
        if remainder > 0:
            if remainder < 10:
                result = result + " " + ONES[remainder]
            elif remainder < 20:
                result = result + " " + TEENS[remainder]
            else:
                tens_digit = remainder // 10 * 10
                ones_digit = remainder % 10
                if ones_digit == 0:
                    result = result + " " + TENS[tens_digit]
                else:
                    result = result + " " + TENS[tens_digit] + " " + ONES[ones_digit]
        return result

    return ""


if __name__ == "__main__":
    print(read_aloud("42"))  # "FORTY TWO"
    print(read_aloud("7"))  # "SEVEN"
    print(read_aloud("105"))  # "ONE HUNDRED FIVE"
    print(read_aloud("333"))  # "THREE HUNDRED THIRTY THREE"
    print(read_aloud(""))  # ""
    print(read_aloud("0"))  # "ZERO"
    print(read_aloud("10"))  # "TEN"
    print(read_aloud("15"))  # "FIFTEEN"
    print(read_aloud("20"))  # "TWENTY"
    print(read_aloud("100"))  # "ONE HUNDRED"
