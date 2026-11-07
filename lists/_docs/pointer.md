# Names and Objects

## Names Point to Objects

In some languages, a **pointer** is a variable that holds the memory address of a value. Python has no pointers you
can work with directly, but every variable behaves like one: a variable is a **name** that points to an **object**.

```python
scores = [85, 92, 78]
```

This line does two things: it creates a list object in memory, then points the name `scores` at it. The name is not
the list; it only leads to it.

## Assignment Never Copies

Assigning one variable to another makes a second name for the **same** object. Nothing is copied:

```python
a = [1, 2, 3]
b = a  # b points to the same list as a
b.append(4)
print(a)  # [1, 2, 3, 4] - a sees the change
print(b)  # [1, 2, 3, 4]
```

```
a ──┐
    ├──► [1, 2, 3, 4]
b ──┘
```

Two names for one object are called **aliases**. A change made through either name shows through both, because there
is only one list.

## `is` and `==`

| Operator | Asks                                   | Example  |
|----------|----------------------------------------|----------|
| `==`     | Do the two objects hold equal values?  | `a == c` |
| `is`     | Do the two names point to one object?  | `a is b` |

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True  - equal values
print(a is c)  # False - two different lists
print(a is b)  # True  - one list, two names
```

`id()` returns a number that identifies an object for as long as it exists. Two names point to the same object exactly
when their `id()`s are equal:

```python
print(id(a) == id(b))  # True
print(id(a) == id(c))  # False
```

> **Note: Compare values with `==`**
>
> Use `is` only to check for `None`: `if result is None:`. For numbers and strings, `is` can give `True` or `False`
> for equal values depending on how Python happened to store them, so always compare them with `==`.

## Mutable and Immutable Objects

A **mutable** object can change in place: a list can grow, shrink, or have an element replaced. An **immutable**
object can never change after it is created.

| Type    | Mutable? | Example           |
|---------|----------|-------------------|
| `list`  | Yes      | `[1, 2, 3]`       |
| `dict`  | Yes      | `{"a": 1}`        |
| `set`   | Yes      | `{1, 2, 3}`       |
| `int`   | No       | `42`              |
| `float` | No       | `3.14`            |
| `bool`  | No       | `True`            |
| `str`   | No       | `"hello"`         |
| `tuple` | No       | `(1, 2, 3)`       |

With an immutable object, aliases are harmless. "Changing" the variable creates a new object and points the name at
it; every other name still points to the old one:

```python
x = 10
y = x
x = x + 1  # x now points to a new object, 11
print(x)  # 11
print(y)  # 10 - y still points to 10

name = "ali"
other = name
name = name.upper()  # upper() returns a new string
print(name)  # ALI
print(other)  # ali
```

## Reassigning vs Changing in Place

With a list, it matters whether a line **changes** the list or **reassigns** the name to a new one:

| Code          | What it does                                      | Other names see it? |
|---------------|---------------------------------------------------|---------------------|
| `b.append(4)` | Changes the list in place                         | Yes                 |
| `b[0] = 9`    | Changes the list in place                         | Yes                 |
| `b += [4]`    | Changes the list in place, like `b.extend([4])`   | Yes                 |
| `b = b + [4]` | Builds a new list and points `b` at it            | No                  |
| `b = []`      | Points `b` at a new, empty list                   | No                  |

```python
a = [1, 2, 3]
b = a
b = b + [4]  # a new list; a is untouched
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]

a = [1, 2, 3]
b = a
b += [4]  # changes the one list both names point to
print(a)  # [1, 2, 3, 4]
```

## Functions Receive the Same Object

Calling a function points its parameter at the object you pass in. A function can therefore change a list that
belongs to its caller:

```python
def add_bonus(scores):
    for i in range(len(scores)):
        scores[i] += 5


marks = [70, 80]
add_bonus(marks)
print(marks)  # [75, 85] - the caller's list changed
```

Reassigning the parameter, though, only moves the function's own name:

```python
def clear(scores):
    scores = []  # points the local name at a new list


marks = [70, 80]
clear(marks)
print(marks)  # [70, 80] - unchanged
```

> **Note: Don't change what you were given**
>
> A function that changes its argument surprises whoever calls it. Unless changing the list is the function's job,
> build and return a new list instead, or work on a copy. The next note,
> [`list_copying.md`](list_copying.md), shows how to make one.
