def coin_sum(amount: int, coins: list[int]) -> int:
    if amount == 0:
        return 1
    if amount < 0 or len(coins) == 0:
        return 0

    # Include first coin (can use it again) + exclude first coin
    return coin_sum(amount - coins[0], coins) + coin_sum(amount, coins[1:])


if __name__ == "__main__":
    print(coin_sum(5, [1, 2, 5]))  # 4
    print(coin_sum(3, [2]))  # 0
    print(coin_sum(0, [1, 2]))  # 1
    print(coin_sum(10, [1, 5, 10]))  # 4
