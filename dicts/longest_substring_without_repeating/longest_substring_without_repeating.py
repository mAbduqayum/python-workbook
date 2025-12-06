def longest_substring_without_repeating(s: str) -> int:
    char_index = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        char = s[right]

        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        if right - left + 1 > max_length:
            max_length = right - left + 1

    return max_length


def longest_substring_without_repeating2(s: str) -> int:
    char_index = {}
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print(longest_substring_without_repeating("abcabcbb"))  # 3 ("abc")
    print(longest_substring_without_repeating("bbbbb"))  # 1 ("b")
    print(longest_substring_without_repeating("pwwkew"))  # 3 ("wke")
    print(longest_substring_without_repeating(""))  # 0
    print(longest_substring_without_repeating("a"))  # 1
    print(longest_substring_without_repeating("abcdef"))  # 6
    print(longest_substring_without_repeating("dvdf"))  # 3 ("vdf")
