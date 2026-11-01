# Error Handling Examples

Try each question yourself before you read its solution.

## Example 1: Ask Until Valid

**Question:** Ask for a rating from 1 to 5. If the answer isn't a whole number, or
is out of range, say so and ask again. Once it's valid, print it.

**Thinking:**

- `abc` makes `int()` raise a `ValueError`, so that needs a `try`.
- `7` converts without a problem and only fails our own check, so that needs an
  `if`.
- We can't know how many tries the user will need, so this calls for a `while`
  loop.

**Solution:**

```python
while True:
    text = input("Rating (1-5): ")
    try:
        rating = int(text)
    except ValueError:
        print("Not a whole number.")
        continue
    if rating < 1 or rating > 5:
        print("Out of range.")
        continue
    break

print(f"Rating: {rating}")
```

Typing `abc`, then `7`, then `4` prints:

```
Not a whole number.
Out of range.
Rating: 4
```

---

## Example 2: Read This Traceback

**Question:** This program crashes. Which line failed, why, and how would you fix
it?

```python
prices = {"tea": 3, "coffee": 5}


def total_price(items):
    total = 0
    for item in items:
        total += prices[item]
    return total


print(total_price(["tea", "coffee"]))
print(total_price(["tea", "juice"]))
```

```
8
Traceback (most recent call last):
  File "/home/farid/order.py", line 12, in <module>
    print(total_price(["tea", "juice"]))
          ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/home/farid/order.py", line 7, in total_price
    total += prices[item]
             ~~~~~~^^^^^^
KeyError: 'juice'
```

**Thinking:**

- The bottom line says what went wrong: `prices` has no key `'juice'`.
- The lines above it say where: line 7, inside `total_price`.
- Above them is the call that got there: line 12, with `["tea", "juice"]`.
- The first call printed `8`, so the function works when every item has a price.
  The problem is an item it wasn't prepared for.

**Solution:** A simple check prevents the error, so check first:

```python
prices = {"tea": 3, "coffee": 5}


def total_price(items):
    total = 0
    for item in items:
        if item in prices:
            total += prices[item]
        else:
            print(f"No price for {item}")
    return total


print(total_price(["tea", "coffee"]))  # 8
print(total_price(["tea", "juice"]))  # Prints the message, then 3
```

---

## Example 3: Raise for Bad Input

**Question:** Write `parse_time(text)`, which turns a time such as `"14:30"` into
minutes since midnight. Raise a `ValueError` if the text isn't a real time.

**Thinking:**

- `"14:30"` is 14 × 60 + 30 = 870 minutes.
- `"25:00"` looks fine, but no hour 25 exists, so that check is ours to write.
- `"noon"` has no `:`, and `"14:xx"` has no number after it. Unpacking and `int()`
  already raise a `ValueError` for those, so we can let them through.

**Solution:**

```python
def parse_time(text: str) -> int:
    hours, minutes = text.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        raise ValueError(f"No such time: {text}")
    return hours * 60 + minutes


for text in ["14:30", "25:00", "noon", "14:xx"]:
    try:
        print(parse_time(text))
    except ValueError as e:
        print(f"Bad time: {e}")
```

```
870
Bad time: No such time: 25:00
Bad time: not enough values to unpack (expected 2, got 1)
Bad time: invalid literal for int() with base 10: 'xx'
```

Three different mistakes reach the same `except`, because all of them are
`ValueError`s.

---

## Example 4: Skip the Bad Entries

**Question:** Write `sum_valid(entries)`, which adds up the strings in a list that
are whole numbers. It returns the total and how many entries it skipped.

**Thinking:**

- For `["4", "x", "7", "", "9"]`, the valid entries add up to 20, and two are
  skipped.
- Where the `try` goes decides what a failure does. Around the whole loop, the
  first bad entry would end the loop. Inside the loop, it only ends that one
  entry's turn, and the loop moves on to the next.

**Solution:**

```python
def sum_valid(entries: list[str]) -> tuple[int, int]:
    total = 0
    skipped = 0
    for entry in entries:
        try:
            total += int(entry)
        except ValueError:
            skipped += 1
    return total, skipped


print(sum_valid(["4", "x", "7", "", "9"]))  # (20, 2)
print(sum_valid([]))  # (0, 0)
```
