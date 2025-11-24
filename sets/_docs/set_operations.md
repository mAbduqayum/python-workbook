# Set Operations

Python sets support all standard mathematical set operations. These operations are powerful tools for comparing and
combining collections.

## Visual Overview

```
A = {1, 2, 3}
B = {2, 3, 4}

Union (A | B):          {1, 2, 3, 4}  - all elements from both
Intersection (A & B):   {2, 3}        - elements in both
Difference (A - B):     {1}           - elements in A but not B
Symmetric Diff (A ^ B): {1, 4}        - elements in either, but not both
```

## Union

Elements that are in **either** set (or both).

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Method 1: operator
a | b                # {1, 2, 3, 4, 5}

# Method 2: method (can take any iterable)
a.union(b)           # {1, 2, 3, 4, 5}
a.union([3, 4, 5])   # {1, 2, 3, 4, 5}

# Multiple sets
a | b | {6, 7}       # {1, 2, 3, 4, 5, 6, 7}
```

## Intersection

Elements that are in **both** sets.

```python
a = {1, 2, 3}
b = {2, 3, 4}

# Method 1: operator
a & b                # {2, 3}

# Method 2: method
a.intersection(b)    # {2, 3}

# Multiple sets
a & b & {2, 5}       # {2}
```

## Difference

Elements in the **first** set but **not** in the second.

```python
a = {1, 2, 3}
b = {2, 3, 4}

# Method 1: operator
a - b                # {1}
b - a                # {4}

# Method 2: method
a.difference(b)      # {1}
```

## Symmetric Difference

Elements in **either** set, but **not in both** (XOR operation).

```python
a = {1, 2, 3}
b = {2, 3, 4}

# Method 1: operator
a ^ b                      # {1, 4}

# Method 2: method
a.symmetric_difference(b)  # {1, 4}
```

## Subset and Superset

```python
a = {1, 2}
b = {1, 2, 3, 4}

# Subset: is every element of a in b?
a <= b               # True (a is subset of b)
a.issubset(b)        # True

a < b                # True (a is proper subset - not equal)

# Superset: does b contain all elements of a?
b >= a               # True (b is superset of a)
b.issuperset(a)      # True
```

## Disjoint Sets

Two sets are **disjoint** if they have no elements in common.

```python
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

a.isdisjoint(b)      # True - no common elements
a.isdisjoint(c)      # False - both have 3
```

## In-Place Operations

Modify the set directly instead of creating a new one:

```python
a = {1, 2, 3}

a |= {4, 5}          # a.update({4, 5})
a &= {2, 3, 4}       # a.intersection_update({2, 3, 4})
a -= {3}             # a.difference_update({3})
a ^= {1, 5}          # a.symmetric_difference_update({1, 5})
```

## Summary Table

| Operation      | Operator | Method                      | Description                  |
|----------------|----------|-----------------------------|------------------------------|
| Union          | `a \| b` | `a.union(b)`                | All elements from both sets  |
| Intersection   | `a & b`  | `a.intersection(b)`         | Elements in both sets        |
| Difference     | `a - b`  | `a.difference(b)`           | Elements in a but not b      |
| Symmetric Diff | `a ^ b`  | `a.symmetric_difference(b)` | Elements in either, not both |
| Subset         | `a <= b` | `a.issubset(b)`             | Is a contained in b?         |
| Superset       | `a >= b` | `a.issuperset(b)`           | Does a contain b?            |
| Disjoint       | -        | `a.isdisjoint(b)`           | No common elements?          |
