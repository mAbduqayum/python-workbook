def first_item(items):
    return items[0]


def mid_item(items):
    return items[len(items) // 2]


def last_item(items):
    return items[-1]


if __name__ == "__main__":
    # Test your functions
    items = [1, 2, 3, 4, 5]
    print(first_item(items))  # 1
    print(mid_item(items))  # 3
    print(last_item(items))  # 5
