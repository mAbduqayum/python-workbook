# Dictionary Best Practices

## Performance Characteristics

### Time Complexity

| Operation        | Average Case | Notes                     |
|------------------|--------------|---------------------------|
| `d[key]` (get)   | O(1)         | Get value                 |
| `d[key] = value` | O(1)         | Set/update value          |
| `del d[key]`     | O(1)         | Delete key-value pair     |
| `key in d`       | O(1)         | Membership test           |
| `d.get(key)`     | O(1)         | Safe access               |
| `d.items()`      | O(1)         | Returns view (not copy)   |
| `len(d)`         | O(1)         | Number of key-value pairs |
| Iteration        | O(n)         | Visit all items           |

## Common Patterns

### Pattern 1: Frequency Counting

```python
# Count occurrences of items
def count_frequencies(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

count_frequencies("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Or use Counter
from collections import Counter
Counter("hello")  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
```

### Pattern 2: Index Mapping

```python
# Map values to their indices
def create_index_map(items):
    return {item: i for i, item in enumerate(items)}

fruits = ["apple", "banana", "cherry"]
create_index_map(fruits)
# {'apple': 0, 'banana': 1, 'cherry': 2}
```

## Common Mistakes to Avoid

### Mistake 1: Using Mutable Objects as Keys

```python
# DON'T: Lists are mutable and unhashable
# d = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# DO: Use tuples instead
d = {(1, 2): "value"}  # OK - tuples are immutable
```

### Mistake 2: Modifying Dictionary During Iteration

```python
d = {"a": 1, "b": 2, "c": 3}

# DON'T: Modifies dict while iterating
# for key in d:
#     if d[key] == 2:
#         del d[key]  # RuntimeError: dictionary changed size during iteration

# DO: Iterate over a copy or collect keys to delete
for key in list(d.keys()):  # list() creates a copy
    if d[key] == 2:
        del d[key]
```

### Mistake 3: Assuming `in` Checks Values

```python
d = {"name": "Alice", "age": 30}

"name" in d  # True (checks keys)
"Alice" in d  # False (doesn't check values!)

# To check if value exists:
"Alice" in d.values()  # True
```

## When NOT to Use Dictionaries

### 1. Sequential Access Needed

```python
# If you need ordered sequential access by position, use a list
items = [1, 2, 3, 4, 5]
items[0]  # First item
items[-1]  # Last item

# Dicts don't support positional indexing
d = {"a": 1, "b": 2}
# d[0]  # KeyError (0 is a key, not a position)
```

### 2. Multiple Values Per Key

```python
# DON'T: Overwrite values
d = {}
d["a"] = 1
d["a"] = 2  # Overwrites previous value

# DO: Use dict of lists
d = {"a": [1, 2]}  # Multiple values as a list
```

## Quick Reference

### Creating Dictionaries

```python
{}                           # Empty dict
{"a": 1, "b": 2}             # Literal
dict(a=1, b=2)               # Constructor with kwargs
dict([("a", 1), ("b", 2)])   # Constructor with pairs
{x: x**2 for x in range(5)}  # Comprehension
```

### Accessing and Modifying

```python
d[key]                  # Get (raises KeyError if missing)
d.get(key, default)     # Get with default
d[key] = value          # Set/update
d.setdefault(key, val)  # Set only if missing
del d[key]              # Delete
d.pop(key, default)     # Remove and return
```

### Iterating

```python
for key in d: ...              # Iterate keys
for value in d.values(): ...   # Iterate values
for k, v in d.items(): ...     # Iterate pairs
```

### Checking and Combining

```python
key in d                # Membership test
len(d)                  # Number of items
d1.update(d2)           # Merge (mutates d1)
d1 | d2                 # Merge (new dict)
```

### Common Collections Helpers

```python
from collections import defaultdict, Counter

defaultdict(int)        # Dict with default values
Counter(items)          # Count items automatically
```

## Performance Tips

1. **Use `in` for membership tests** - It's O(1) for dicts vs O(n) for lists
2. **Use `get()` for optional keys** - Returns a default instead of raising KeyError
3. **Use dict comprehensions** - More readable and often faster than loops
4. **Consider `defaultdict`** - Simpler code when you need default values
5. **Use `Counter`** - Purpose-built for counting, includes helpful methods
6. **Iterate over `.items()`** - More efficient than `for k in d: value = d[k]`
