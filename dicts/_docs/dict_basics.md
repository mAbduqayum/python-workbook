# Dictionary Basics

A **dictionary** is a collection of key-value pairs. Dictionaries are one of Python's most powerful built-in data types
and are extremely useful when you need to:

- Map relationships between data (e.g., names to phone numbers)
- Look up values quickly by a unique key (O(1) average time)
- Count or track frequency of items
- Cache results or memoize function calls

## Creating Dictionaries

```python
# Empty dictionary (note: {} creates an empty dict)
empty_dict = {}
empty_dict = dict()

# Dictionary from literal
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Dictionary from list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)  # {'a': 1, 'b': 2, 'c': 3}

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Using dict() constructor with keyword arguments
config = dict(host="localhost", port=8080, debug=True)
```

## Key Characteristics

| Feature       | Description                                                       |
|---------------|-------------------------------------------------------------------|
| Ordered       | Maintains insertion order                                         |
| Mutable       | Can add, update, or remove key-value pairs                        |
| Unique keys   | Each key can appear only once; new values overwrite existing ones |
| Hashable keys | Keys must be immutable types (str, int, tuple, etc., not lists)   |
| Fast lookup   | O(1) average time complexity for access, insert, and delete       |

## Basic Operations

### Accessing Values

```python
d = {"name": "Alice", "age": 30}

# Direct access (raises KeyError if key doesn't exist)
print(d["name"])  # "Alice"

# Safe access with get() (returns None or default if key doesn't exist)
print(d.get("name"))  # "Alice"
print(d.get("email"))  # None
print(d.get("email", "not@found.com"))  # "not@found.com"
```

Use `d[key]` when the key must exist (a missing key is a bug you want to see), and `d.get(key, default)` when a
missing key is normal.

### Adding and Updating

```python
d = {"name": "Alice"}

d["age"] = 30  # Add new key-value pair: {"name": "Alice", "age": 30}
d["name"] = "Bob"  # Update existing value: {"name": "Bob", "age": 30}

# setdefault: add key only if it doesn't exist
d.setdefault("city", "NYC")  # {"name": "Bob", "age": 30, "city": "NYC"}
d.setdefault("age", 25)  # {"name": "Bob", "age": 30, "city": "NYC"} (no change)
```

### Removing Elements

```python
d = {"name": "Alice", "age": 30, "city": "NYC"}

del d["age"]  # {"name": "Alice", "city": "NYC"} - raises KeyError if not found

value = d.pop("city")  # Returns "NYC", d = {"name": "Alice"}
value = d.pop("missing", "default")  # Returns "default", no error

d.clear()  # {} - removes all items
```

### Membership Testing

```python
d = {"name": "Alice", "age": 30}

"name" in d  # True (checks keys, not values!)
"Alice" in d  # False (values are not checked by 'in')
"email" not in d  # True
```

## When to Use Dictionaries

| Use Case                    | Why Dictionaries?                              |
|-----------------------------|------------------------------------------------|
| Fast lookups by key         | O(1) average vs O(n) for list search           |
| Counting/frequency tracking | Perfect for tallying occurrences               |
| Caching/memoization         | Store computed results for quick retrieval     |
| Mapping relationships       | Associate related data (ID → user, word → def) |
| Grouping data               | Collect items by category or property          |
| Configuration settings      | Store named parameters and options             |

## Important Notes on Keys

### Keys Must Be Hashable (Immutable)

```python
# Valid keys (immutable types)
d = {
    "string": 1,  # str - OK
    42: 2,  # int - OK
    3.14: 3,  # float - OK
    (1, 2): 4,  # tuple - OK (if it contains only immutable items)
    True: 5,  # bool - OK
}

# Invalid keys (mutable types)
# d = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
# d = {{}: "value"}  # TypeError: unhashable type: 'dict'
# d = {{1, 2}: "value"}  # TypeError: unhashable type: 'set'
```

### Key Uniqueness

```python
# Later assignments overwrite earlier ones
d = {"a": 1, "b": 2, "a": 3}
print(d)  # {"a": 3, "b": 2} - second "a" overwrites first
```
