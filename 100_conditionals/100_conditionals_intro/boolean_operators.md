# Booleans and Boolean Operators

## Boolean Type
The boolean type (`bool`) has only two values: `True` and `False`. These are used in conditional statements to make decisions.

## Boolean Operators
Boolean operators `and`, `or`, `not` allow you to combine and manipulate boolean values `True`, `False` to create more complex conditions.

### 1. `and` Operator

Returns `True` only when both conditions are true.

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

### 2. `or` Operator

Returns `True` when at least one condition is true.

| A     | B     | A or B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

### 3. `not` Operator

Reverses the boolean value.

| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

## Combining Multiple Operators

You can combine multiple boolean operators in a single expression:

## Operator Precedence

When combining operators, Python follows this order:

1. `not` (highest precedence)
2. `and`
3. `or` (lowest precedence)

```python
result = not True or False and True
print(result)
# Is evaluated as: (not True) or (False and True)
# Result: False or False -> False
```
