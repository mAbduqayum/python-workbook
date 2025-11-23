def has_two_sum(numbers: list, target: int) -> bool:
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    print(has_two_sum([1, 2, 3, 4], 5))  # True (1+4 or 2+3)
    print(has_two_sum([1, 2, 3, 4], 10))  # False
    print(has_two_sum([3, 3], 6))  # True (3+3)
    print(has_two_sum([3], 6))  # False (can't use same element twice)
    print(has_two_sum([], 5))  # False
    print(has_two_sum([5, 0], 5))  # True (5+0)
