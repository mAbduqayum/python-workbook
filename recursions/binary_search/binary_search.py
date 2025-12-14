def binary_search(lst: list, target: int) -> int:
    def helper(low: int, high: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            return helper(low, mid - 1)
        else:
            return helper(mid + 1, high)

    return helper(0, len(lst) - 1)


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    print(binary_search(nums, 7))  # 3
    print(binary_search(nums, 1))  # 0
    print(binary_search(nums, 11))  # 5
    print(binary_search(nums, 4))  # -1
