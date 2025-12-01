def is_anagram(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    freq1 = {}
    for char in word1:
        if char in freq1:
            freq1[char] = freq1[char] + 1
        else:
            freq1[char] = 1

    freq2 = {}
    for char in word2:
        if char in freq2:
            freq2[char] = freq2[char] + 1
        else:
            freq2[char] = 1

    return freq1 == freq2


def is_anagram2(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    freq1 = {}
    for char in word1:
        freq1[char] = freq1.get(char, 0) + 1

    freq2 = {}
    for char in word2:
        freq2[char] = freq2.get(char, 0) + 1

    return freq1 == freq2


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))  # False
    print(is_anagram("abc", "abcd"))  # False
    print(is_anagram("test", "test"))  # True
    print(is_anagram("", ""))  # True
    print(is_anagram("a", "a"))  # True
