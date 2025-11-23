def longest_consecutive(numbers: list) -> int:
    if not numbers:
        return 0

    num_set = set(numbers)
    longest = 0

    for num in num_set:
        # Only start counting if this is the start of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4 (sequence: 1,2,3,4)
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9 (sequence: 0-8)
    print(longest_consecutive([1, 2, 0, 1]))  # 3 (sequence: 0,1,2)
    print(longest_consecutive([]))  # 0
    print(longest_consecutive([5]))  # 1
    print(longest_consecutive([1, 3, 5, 7]))  # 1 (no consecutive numbers)
