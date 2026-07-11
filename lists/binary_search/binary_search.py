def binary_search(items: list, target) -> int:
    left, right = 0, len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    # Test your function
    items = [2, 3, 5, 7, 11]
    print(binary_search(items, 5))  # 2
    print(binary_search(items, 4))  # -1
