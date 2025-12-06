def is_phrase_anagram(phrase1: str, phrase2: str) -> bool:
    clean1 = phrase1.lower().replace(" ", "")
    clean2 = phrase2.lower().replace(" ", "")

    freq1 = {}
    for char in clean1:
        if char in freq1:
            freq1[char] = freq1[char] + 1
        else:
            freq1[char] = 1

    freq2 = {}
    for char in clean2:
        if char in freq2:
            freq2[char] = freq2[char] + 1
        else:
            freq2[char] = 1

    return freq1 == freq2


def is_phrase_anagram2(phrase1: str, phrase2: str) -> bool:
    clean1 = phrase1.lower().replace(" ", "")
    clean2 = phrase2.lower().replace(" ", "")

    freq1 = {}
    for char in clean1:
        freq1[char] = freq1.get(char, 0) + 1

    freq2 = {}
    for char in clean2:
        freq2[char] = freq2.get(char, 0) + 1

    return freq1 == freq2


if __name__ == "__main__":
    print(is_phrase_anagram("listen", "silent"))  # True
    print(is_phrase_anagram("conversation", "voices rant on"))  # True
    print(is_phrase_anagram("The Eyes", "They See"))  # True
    print(is_phrase_anagram("hello world", "world peace"))  # False
    print(is_phrase_anagram("abc", "a b c"))  # True
    print(is_phrase_anagram("", ""))  # True
