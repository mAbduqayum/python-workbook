def isomorphic_strings(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t

        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s

    return True


def isomorphic_strings2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t, strict=False):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t

        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s

    return True


if __name__ == "__main__":
    print(isomorphic_strings("egg", "add"))  # True
    print(isomorphic_strings("foo", "bar"))  # False
    print(isomorphic_strings("paper", "title"))  # True
    print(isomorphic_strings("ab", "abc"))  # False
    print(isomorphic_strings("abc", "abc"))  # True
    print(isomorphic_strings("", ""))  # True
