def clamp(value: int, low: int, high: int) -> int:
    if value < low:
        return low
    if value > high:
        return high
    return value


def clamp2(value: int, low: int, high: int) -> int:
    return max(low, min(value, high))


if __name__ == "__main__":
    print(clamp(13, 1, 12))  # 12
    print(clamp(0, 1, 12))  # 1
    print(clamp(7, 1, 12))  # 7
    print(clamp(-5, -3, 3))  # -3
