# Tuples in Python

## Introduction

A **tuple** is an ordered collection, like a list, that can never change once it is created: it is **immutable**.
Tuples are written with parentheses instead of square brackets.

```python
point = (3, 4)
colors = ("red", "green", "blue")
```

Use a tuple for a fixed group of values that belong together: the two coordinates of a point, the day, month and year
of a date, the red, green and blue parts of a color.

## Creating Tuples

| Method               | Example                | Result             |
|----------------------|------------------------|--------------------|
| Empty tuple          | `empty = ()`           | `()`               |
| With values          | `point = (3, 4)`       | `(3, 4)`           |
| Without parentheses  | `point = 3, 4`         | `(3, 4)`           |
| One element          | `single = (5,)`        | `(5,)`             |
| From a list          | `tuple([1, 2, 3])`     | `(1, 2, 3)`        |
| From a string        | `tuple("abc")`         | `('a', 'b', 'c')`  |

> **Note: A one-element tuple needs a comma**
>
> It is the comma that makes a tuple, not the parentheses. `(5)` is just the number 5 in parentheses, as in `(5) * 2`;
> `(5,)` is a tuple:
>
> ```python
> print(type((5)))  # <class 'int'>
> print(type((5,)))  # <class 'tuple'>
> ```

## Reading a Tuple

Everything that reads a list without changing it works on a tuple too:

```python
colors = ("red", "green", "blue")

print(colors[0])  # red
print(colors[-1])  # blue
print(colors[0:2])  # ('red', 'green')
print(len(colors))  # 3
print("green" in colors)  # True

for color in colors:
    print(color)
```

Tuples have only two methods, and neither changes the tuple:

| Method          | Description                    | Example                       | Result |
|-----------------|--------------------------------|-------------------------------|--------|
| `count(x)`      | How many times `x` appears     | `(1, 2, 2, 3).count(2)`       | `2`    |
| `index(x)`      | Index of the first `x`         | `("a", "b", "c").index("b")`  | `1`    |

## Tuples Can't Change

Anything that would change a tuple is an error:

```python
point = (3, 4)
point[0] = 10  # TypeError: 'tuple' object does not support item assignment
point.append(5)  # AttributeError: 'tuple' object has no attribute 'append'
```

To get a different tuple, build a new one and point the name at it:

```python
point = (3, 4)
point = (10, point[1])
print(point)  # (10, 4)
```

> **Note: A tuple of lists**
>
> A tuple can't change which objects it holds, but an object inside it can still change if it is mutable. A list in a
> tuple can still grow:
>
> ```python
> student = ("Ali", [90, 85])
> student[1].append(100)
> print(student)  # ('Ali', [90, 85, 100])
> ```
>
> [`pointer.md`](pointer.md) explains mutable and immutable objects.

## Packing and Unpacking

Listing values with commas **packs** them into a tuple. Assigning a tuple to several names **unpacks** it, one value
per name:

```python
point = 3, 4  # packing
x, y = point  # unpacking
print(x)  # 3
print(y)  # 4
```

The number of names must match the number of values:

```python
x, y = (1, 2, 3)  # ValueError: too many values to unpack (expected 2)
```

Unpacking makes swapping two variables a single line:

```python
a = 1
b = 2
a, b = b, a
print(a, b)  # 2 1
```

### Where You Have Already Met Tuples

Several things you already use hand you tuples:

```python
# divmod() returns the quotient and the remainder as a tuple
quotient, remainder = divmod(17, 5)
print(quotient, remainder)  # 3 2

# enumerate() gives an (index, element) tuple at each step
for index, color in enumerate(["red", "green"]):
    print(index, color)  # 0 red, then 1 green

# zip() pairs elements up as tuples
for name, score in zip(["Ali", "Sara"], [90, 85]):
    print(name, score)  # Ali 90, then Sara 85


# A function that returns several values returns them as one tuple
def min_max(numbers):
    return min(numbers), max(numbers)


low, high = min_max([4, 9, 1])
print(low, high)  # 1 9
```

## Tuples or Lists?

|                    | List                                   | Tuple                                     |
|--------------------|----------------------------------------|-------------------------------------------|
| Written as         | `[1, 2, 3]`                            | `(1, 2, 3)`                               |
| Can change         | Yes                                    | No                                        |
| Methods            | `append`, `remove`, `sort` and more    | `count` and `index` only                  |
| Typical use        | Many values of one kind: scores, names | A fixed group of values: a point, a date  |
| Dictionary key     | No                                     | Yes, if everything inside is immutable    |

**Rule of thumb**: if the values will be added to, removed or reordered, use a list. If they belong together as one
fixed record, use a tuple.
