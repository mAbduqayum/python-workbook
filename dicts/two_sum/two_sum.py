def two_sum(nums: list[int], target: int) -> list[int] | None:
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return None


def two_sum2(nums: list[int], target: int) -> list[int] | None:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))  # [1, 2]
    print(two_sum([3, 3], 6))  # [0, 1]
    print(two_sum([1, 2, 3], 10))  # None
    print(two_sum([-1, -2, -3, -4], -5))  # [0, 3] or [1, 2]
    print(two_sum([0, 1, 0], 0))  # [0, 2]
