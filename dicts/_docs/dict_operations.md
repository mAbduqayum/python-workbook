# Dictionary Operations

## Common Dictionary Methods

### Viewing Dictionary Data

```python
d = {"name": "Alice", "age": 30, "city": "NYC"}

# Get all keys
keys = d.keys()  # dict_keys(['name', 'age', 'city'])
list(keys)  # ['name', 'age', 'city']

# Get all values
values = d.values()  # dict_values(['Alice', 30, 'NYC'])
list(values)  # ['Alice', 30, 'NYC']

# Get all key-value pairs
items = d.items()  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'NYC')])
list(items)  # [('name', 'Alice'), ('age', 30), ('city', 'NYC')]
```

### `setdefault()` - Add Key Only if Missing

```python
d = {"name": "Alice"}

# Add key with default value if it doesn't exist
d.setdefault("age", 0)  # Returns 0, d = {"name": "Alice", "age": 0}

# If key exists, return its value without changing it
d.setdefault("name", "Bob")  # Returns "Alice", d unchanged

# Useful for initializing nested structures
words = ["apple", "banana", "apple", "cherry"]
by_first_letter = {}
for word in words:
    by_first_letter.setdefault(word[0], []).append(word)
# {'a': ['apple', 'apple'], 'b': ['banana'], 'c': ['cherry']}
```

### `pop()` and `popitem()` - Remove and Return

```python
d = {"name": "Alice", "age": 30, "city": "NYC"}

# pop(key) - remove and return value for key
age = d.pop("age")  # Returns 30, d = {"name": "Alice", "city": "NYC"}

# pop with default - no error if key doesn't exist
email = d.pop("email", "no-email")  # Returns "no-email", d unchanged

# popitem() - remove and return the last inserted key-value pair
item = d.popitem()  # Returns ("city", "NYC"), d = {"name": "Alice"}
```

## Iteration Patterns

### Iterating Over Keys (Default)

```python
d = {"a": 1, "b": 2, "c": 3}

# These are equivalent:
for key in d:
    print(key, d[key])

for key in d.keys():
    print(key, d[key])
```

### Iterating Over Values

```python
d = {"a": 1, "b": 2, "c": 3}

for value in d.values():
    print(value)  # 1, 2, 3
```

### Iterating Over Key-Value Pairs (Most Common)

```python
d = {"name": "Alice", "age": 30, "city": "NYC"}

for key, value in d.items():
    print(f"{key}: {value}")
# name: Alice
# age: 30
# city: NYC
```

## Dictionary Comprehensions

```python
# Create dict from expression
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filter with condition
evens = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Transform existing dict
prices = {"apple": 0.5, "banana": 0.3, "cherry": 0.8}
doubled = {item: price * 2 for item, price in prices.items()}
# {'apple': 1.0, 'banana': 0.6, 'cherry': 1.6}

# Swap keys and values
inverted = {value: key for key, value in d.items()}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}
```

## Merging Dictionaries

### `update()` - Merge Into an Existing Dict

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)  # d1 is modified: {"a": 1, "b": 3, "c": 4} (d2's values win)
```

### `|` - Merge Into a New Dict

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2  # New dict: {"a": 1, "b": 3, "c": 4}
# d1 and d2 are unchanged

d1 |= d2  # In-place, same as d1.update(d2)
```

## Collections Module: `defaultdict` and `Counter`

### defaultdict - Never Get KeyError

```python
from collections import defaultdict

# Regular dict - KeyError on missing key
d = {}
# d["missing"] += 1  # KeyError!

# defaultdict with default value
dd = defaultdict(int)  # int() returns 0
dd["missing"] += 1  # Works! dd = {"missing": 1}

# defaultdict with list (for grouping)
dd = defaultdict(list)
for item in ["apple", "banana", "apricot"]:
    dd[item[0]].append(item)
# {'a': ['apple', 'apricot'], 'b': ['banana']}
```

### Counter - Counting Made Easy

```python
from collections import Counter

# Count items in iterable
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Works with strings too
letter_counts = Counter("hello world")
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Get most common items
counts.most_common(2)  # [('apple', 3), ('banana', 2)]

# Counter supports addition and subtraction
c1 = Counter("hello")
c2 = Counter("world")
c1 + c2  # Counter({'l': 4, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
```

## Dictionary View Objects

```python
d = {"a": 1, "b": 2, "c": 3}

keys = d.keys()  # dict_keys(['a', 'b', 'c'])
values = d.values()  # dict_values([1, 2, 3])
items = d.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Views are dynamic - they reflect changes to the dict
d["d"] = 4
list(keys)  # ['a', 'b', 'c', 'd'] - automatically updated!

# Views support set operations (for keys and items)
d1_keys = {"a": 1, "b": 2}.keys()
d2_keys = {"b": 3, "c": 4}.keys()

d1_keys & d2_keys  # {'b'} - intersection
d1_keys | d2_keys  # {'a', 'b', 'c'} - union
d1_keys - d2_keys  # {'a'} - difference
```
