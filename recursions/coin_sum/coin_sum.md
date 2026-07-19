# Coin Sum

Create a recursive function that counts the number of ways to make change for a given amount using a set of coin denominations.

## Template

```python
def coin_sum(amount: int, coins: list[int]) -> int:
    pass


if __name__ == "__main__":
    print(coin_sum(5, [1, 2, 5]))    # 4 (ways: 5, 2+2+1, 2+1+1+1, 1+1+1+1+1)
    print(coin_sum(3, [2]))          # 0 (no way to make 3 with only 2s)
    print(coin_sum(0, [1, 2]))       # 1 (one way: use no coins)
    print(coin_sum(10, [1, 5, 10]))  # 4
```
