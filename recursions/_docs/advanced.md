# Advanced Recursion

## Binary Search

Search in sorted list by dividing in half:

```python
def binary_search(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, low, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, high)

nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(nums, 7))   # 3
print(binary_search(nums, 4))   # -1
```

## Flatten Nested List

```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, [4]]]]))  # [1, 2, 3, 4]
print(flatten([[1, 2], [3, [4, 5]]]))  # [1, 2, 3, 4, 5]
```

## Sum Nested List

```python
def nested_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total

print(nested_sum([1, [2, [3, 4]], 5]))  # 15
```

## Permutations

Generate all arrangements:

```python
def permutations(lst):
    if len(lst) <= 1:
        return [lst]

    result = []
    for i, item in enumerate(lst):
        rest = lst[:i] + lst[i+1:]
        for perm in permutations(rest):
            result.append([item] + perm)
    return result

print(permutations([1, 2, 3]))
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

## Subsets

Generate all subsets:

```python
def subsets(lst):
    if not lst:
        return [[]]

    rest = subsets(lst[1:])
    return rest + [[lst[0]] + s for s in rest]

print(subsets([1, 2, 3]))
# [[], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]]
```

## Directory Tree (Conceptual)

```python
import os

def list_files(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            list_files(full_path)  # recurse into subdirectory
        else:
            print(full_path)
```

## Tail Recursion

When recursive call is the last operation:

```python
# Not tail recursive (multiplication after call)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Tail recursive (nothing after call)
def factorial_tail(n, acc=1):
    if n <= 1:
        return acc
    return factorial_tail(n - 1, n * acc)
```

Note: Python doesn't optimize tail recursion, but it's a useful pattern for converting to loops.
