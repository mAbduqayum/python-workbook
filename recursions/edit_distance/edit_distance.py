def edit_distance(s1: str, s2: str) -> int:
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    if s1[-1] == s2[-1]:
        return edit_distance(s1[:-1], s2[:-1])

    insert = edit_distance(s1, s2[:-1]) + 1
    delete = edit_distance(s1[:-1], s2) + 1
    replace = edit_distance(s1[:-1], s2[:-1]) + 1

    return min(insert, delete, replace)


if __name__ == "__main__":
    print(edit_distance("kitten", "sitting"))  # 3
    print(edit_distance("", "abc"))  # 3
    print(edit_distance("abc", ""))  # 3
    print(edit_distance("abc", "abc"))  # 0
    print(edit_distance("horse", "ros"))  # 3
