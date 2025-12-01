def first_unique_char(text: str) -> str | None:
    freq = {}
    for char in text:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1

    for char in text:
        if freq[char] == 1:
            return char

    return None


def first_unique_char2(text: str) -> str | None:
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    for char in text:
        if freq[char] == 1:
            return char

    return None


if __name__ == "__main__":
    print(first_unique_char("leetcode"))  # 'l'
    print(first_unique_char("loveleetcode"))  # 'v'
    print(first_unique_char("aabbcc"))  # None
    print(first_unique_char("abcab"))  # 'c'
    print(first_unique_char("a"))  # 'a'
    print(first_unique_char(""))  # None
