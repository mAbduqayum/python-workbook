def get_page(items: list, page_num: int, page_size: int) -> list:
    start = (page_num - 1) * page_size
    return items[start : start + page_size]


if __name__ == "__main__":
    # Test your function
    print(get_page(["a", "b", "c", "d", "e"], 1, 2))  # ['a', 'b']
    print(get_page(["a", "b", "c", "d", "e"], 2, 2))  # ['c', 'd']
    print(get_page(["a", "b", "c", "d", "e"], 3, 2))  # ['e']
