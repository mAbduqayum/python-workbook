# Lists in Python - Joining Iterables to Strings

## Joining Iterables to Strings

Convert a list of strings into a single string using the `join()` method:

```python
# Basic join
words = ["Hello", "world"]
sentence = " ".join(words)  # "Hello world"

# Join with different separators
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))  # "apple, banana, cherry"
print("-".join(fruits))   # "apple-banana-cherry"
print("".join(fruits))    # "applebananacherry"

# Join with newlines
lines = ["Line 1", "Line 2", "Line 3"]
text = "\n".join(lines)
# Line 1
# Line 2
# Line 3

# Convert numbers to string first
numbers = [1, 2, 3, 4, 5]
result = ", ".join(str(n) for n in numbers)  # "1, 2, 3, 4, 5"
# Or using map:
result = ", ".join(map(str, numbers))  # "1, 2, 3, 4, 5"

# Common pattern: CSV format
data = ["Alice", "25", "Engineer"]
csv_line = ",".join(data)  # "Alice,25,Engineer"
```

> **Note: join() is a string method, not a list method**
>
> Notice that `join()` is called on the separator string, not on the list: `separator.join(list)`. This might seem
> backwards at first, but it makes sense because:
> - The separator is a string, and `join()` is a string method
> - It returns a string (not a list)
> - It pairs with `split()`: `"a,b,c".split(",")` creates a list, `",".join(["a","b","c"])` creates a string
>
> **Common mistake**: `my_list.join(",")` will cause an AttributeError! Use `",".join(my_list)` instead.
