def most_frequent_char(text: str) -> str:
    if not text:
        raise ValueError("Cannot find most frequent character in empty string")

    freq = {}
    for char in text:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1

    max_char = ""
    max_count = 0
    for char in freq:
        if freq[char] > max_count:
            max_count = freq[char]
            max_char = char

    return max_char


def most_frequent_char2(text: str) -> str:
    if not text:
        raise ValueError("Cannot find most frequent character in empty string")

    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    return max(freq, key=freq.get)


if __name__ == "__main__":
    print(most_frequent_char("hello"))  # 'l'
    print(most_frequent_char("aabbcc"))  # 'a' (or 'b' or 'c' - all tied)
    print(most_frequent_char("a"))  # 'a'
    print(most_frequent_char("abcabc"))  # 'a' (or 'b' or 'c' - all tied)
    print(most_frequent_char("AaAaBb"))  # 'A'
    print(most_frequent_char("hello world"))  # 'l'
