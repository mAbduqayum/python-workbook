# Boolean Operators in Python

Boolean operators allow you to combine and manipulate boolean values (True/False) to create more complex conditions.

## The Three Boolean Operators

### 1. `and` Operator
Returns `True` only when both conditions are true.

```python
# Both conditions must be true
age = 25
salary = 50000

if age >= 18 and salary >= 40000:
    print("Eligible for loan")
```

**Truth Table:**

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

### 2. `or` Operator
Returns `True` when at least one condition is true.

```python
# At least one condition must be true
day = "Saturday"
holiday = True

if day == "Sunday" or holiday:
    print("No work today!")
```

**Truth Table:**

| A     | B     | A or B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

### 3. `not` Operator
Reverses the boolean value.

```python
# Reverses the condition
is_raining = False

if not is_raining:
    print("Good weather for a walk")
```

**Truth Table:**

| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

## Combining Multiple Operators

You can combine multiple boolean operators in a single expression:

```python
age = 20
has_license = True
has_car = False

# Complex condition using multiple operators
if age >= 18 and has_license and not has_car:
    print("You can rent a car")
```

## Operator Precedence

When combining operators, Python follows this order:
1. `not` (highest precedence)
2. `and`
3. `or` (lowest precedence)

```python
# This expression: not True or False and True
# Is evaluated as: (not True) or (False and True)
# Result: False or False = False

result = not True or False and True
print(result)  # False
```

## Practical Examples

### Checking Valid Age Range
```python
age = int(input("Enter your age: "))

if 13 <= age <= 19:
    print("You are a teenager")
```

### Multiple Conditions with OR
```python
grade = input("Enter your grade: ")

if grade == "A" or grade == "B" or grade == "C":
    print("Passing grade")
else:
    print("Failing grade")
```
