def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}

    for word in words:
        key = "".join(sorted(word))

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    result = []
    for key in groups:
        result.append(groups[key])
    return result


def group_anagrams2(words: list[str]) -> list[list[str]]:
    groups = {}

    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)

    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    print(group_anagrams(["abc", "def"]))
    # [['abc'], ['def']]

    print(group_anagrams(["abc", "bca", "cab"]))
    # [['abc', 'bca', 'cab']]

    print(group_anagrams([]))
    # []

    print(group_anagrams(["hello"]))
    # [['hello']]
