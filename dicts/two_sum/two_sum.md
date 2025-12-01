# Two Sum

Find two numbers that add up to a target value.

## Task

Write a function `two_sum(nums, target)` that finds two numbers in the array that add up to the target value.

- Return the indices of the two numbers as a list `[index1, index2]`
- Return `None` if no two numbers add up to the target
- You cannot use the same element twice
- There may be multiple valid answers; return any one of them
- The array may contain negative numbers and zeros

## Template

```python
def two_sum(nums: list[int], target: int) -> list[int] | None:
    pass


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))  # [1, 2]
    print(two_sum([3, 3], 6))  # [0, 1]
    print(two_sum([1, 2, 3], 10))  # None
    print(two_sum([-1, -2, -3, -4], -5))  # [0, 3] or [1, 2]
    print(two_sum([0, 1, 0], 0))  # [0, 2]
```

## Hint

<details>
<summary>Click to reveal hint</summary>

Use the **complement pattern**: For each number, calculate what value would sum to the target (the complement). Store numbers you've seen in a dictionary with their indices.

```python
seen = {}

for i in range(len(nums)):
    num = nums[i]
    complement = target - num  # What number do we need?

    if complement in seen:  # Have we seen it before?
        return [seen[complement], i]

    seen[num] = i  # Remember this number and its index

return None
```

Example with `nums = [2, 7, 11]`, `target = 9`:
1. `num = 2`, `complement = 7`, not seen yet, store `{2: 0}`
2. `num = 7`, `complement = 2`, **found!** Return `[0, 1]`

</details>

## Note

<details>
<summary>Click to reveal note</summary>

**The Complement Search Pattern:**

This is one of the most important patterns in coding interviews and real-world programming:

**Problem**: Find two items that satisfy a relationship (e.g., sum to target)

**Naive Solution** (O(n²)):
```python
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

**Optimized with Dictionary** (O(n)):
```python
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

**Why This Works:**

Instead of checking all pairs, we:
1. For each number, calculate its complement (what it needs to pair with)
2. Check if we've seen the complement before (O(1) dictionary lookup)
3. Store each number as we go

**Time Complexity**: O(n) - single pass through array
**Space Complexity**: O(n) - dictionary stores up to n elements

This pattern applies to many similar problems: finding pairs with a specific difference, product, etc.

</details>
