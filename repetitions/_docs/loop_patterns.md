# Repetition in Python - Common Loop Patterns

The following are common patterns you'll use repeatedly when working with loops.

## Pattern 1: Accumulation (Sum/Total)

Calculate the sum of numbers from 1 to 10:

```python
total = 0
for i in range(1, 11):
    total += i
print(f"Sum: {total}")  # Sum: 55
```

## Pattern 2: Counting

Count how many even numbers are between 1 and 10:

```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
print(f"Even numbers: {count}")  # Even numbers: 5
```

## Pattern 3: Finding Maximum/Minimum

Find the maximum of numbers entered by the user:

```python
max_value = float('-inf')  # Start with very small value
for i in range(5):
    num = int(input("Enter a number: "))
    if num > max_value:
        max_value = num
print(f"Maximum: {max_value}")
```

> **Note:** For minimum, use `float('inf')` instead.

## Pattern 4: Digit Stripping

`n % 10` is the last digit of a number, and `n // 10` is the number without that
digit. Repeat both to visit every digit, from right to left:

```python
n = 4071
while n > 0:
    print(n % 10)
    n = n // 10
```

| `n`    | Prints `n % 10` | `n // 10` |
|--------|-----------------|-----------|
| `4071` | `1`             | `407`     |
| `407`  | `7`             | `40`      |
| `40`   | `0`             | `4`       |
| `4`    | `4`             | `0`       |

> **Note:** The loop never runs when `n` is `0` or negative. Handle `0` on its
> own if it matters, and strip the digits of `abs(n)` for a negative number.
