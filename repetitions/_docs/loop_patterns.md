# Repetition in Python - Common Loop Patterns

Most loops follow one of a few patterns, and each pattern gives one variable a
job. Learn their names. When you read a new problem, you can then ask which
patterns it needs:

| The problem asks...                  | Pattern         |
|--------------------------------------|-----------------|
| How many?                            | Counter         |
| What is the total?                   | Accumulator     |
| Which is the largest or smallest?    | Best so far     |
| Keep reading until the user stops    | Sentinel        |
| Is there any? Are they all?          | Flag            |
| What are the digits of this number?  | Digit stripping |

They all have the same three parts: set the variable up before the loop, update
it inside the loop, and use it after the loop. A single program often combines
several patterns.

## Pattern 1: Counter

A **counter** starts at `0` and goes up by one each time something happens. Count
how many even numbers are between 1 and 10:

```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
print(f"Even numbers: {count}")  # Even numbers: 5
```

## Pattern 2: Accumulator

An **accumulator** builds up a result one step at a time. Calculate the sum of
the numbers from 1 to 10:

```python
total = 0
for i in range(1, 11):
    total += i
print(f"Sum: {total}")  # Sum: 55
```

Its starting value depends on the operation: `0` for a sum, `1` for a product,
and `""` for a string.

## Pattern 3: Best So Far

**Best so far** holds the best value seen up to now. Compare each new value with
it, and replace it when the new one is better. Find the maximum of numbers
entered by the user:

```python
max_value = float('-inf')  # Start with very small value
for i in range(5):
    num = int(input("Enter a number: "))
    if num > max_value:
        max_value = num
print(f"Maximum: {max_value}")
```

> **Note:** For minimum, use `float('inf')` instead.

## Pattern 4: Sentinel

A **sentinel** is a special value that means "stop." It isn't part of the data,
so the loop must not process it. Read once before the loop, and read again as
the last step inside it. This example adds up numbers until the user enters a
blank line, so it uses an accumulator too:

```python
total = 0
line = input("Enter a number (blank to stop): ")
while line != "":
    total += int(line)
    line = input("Enter a number (blank to stop): ")
print(f"Total: {total}")
```

## Pattern 5: Flag

A **flag** is a boolean that remembers whether something happened. It starts with
the answer you would give if nothing turned up, and it changes when something
does. Check whether a word contains a digit:

```python
has_digit = False
for char in "pass1word":
    if char.isdigit():
        has_digit = True
print(has_digit)  # True
```

Don't set the flag back to `False` in an `else`: the next letter would erase what
you found at `1`.

## Pattern 6: Digit Stripping

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
