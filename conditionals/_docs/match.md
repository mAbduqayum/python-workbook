# Match Statement

## Python Match Statement

The `match` statement provides pattern matching similar to switch statements in other languages, but more powerful. It's
particularly useful when you have multiple discrete values to check against.

## Basic Match Syntax

```python
match expression:
    case pattern1:
        # code for pattern1
    case pattern2:
        # code for pattern2
    case _:
        # default case (optional)
```

## Examples

### Example 1: Month Days

**Problem**: Display the number of days in a month based on the month name.

**Using match statement:**
```python
# Read the month name
month = input().lower()

# Determine the number of days
match month:
    case "february":
        print("28 or 29")
    case "january" | "march" | "may" | "july" | "august" | "october" | "december":
        print("31")
    case "april" | "june" | "september" | "november":
        print("30")
    case _:
        print("Invalid month")
```

**Using if-elif for comparison:**
```python
# Read the month name
month = input().lower()

# Determine the number of days
if month == "february":
    print("28 or 29")
elif month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
    print("31")
elif month == "april" or month == "june" or month == "september" or month == "november":
    print("30")
else:
    print("Invalid month")
```

### Example 2: Faces on Money

**Problem**: Identify which individual appears on Tajikistan banknotes based on denomination.

```python
# Read the denomination
denomination = int(input())

# Determine the individual on the banknote
match denomination:
    case 1:
        print("Mirzo Tursunzoda")
    case 3:
        print("Shirinsho Shotemur")
    case 5:
        print("Sadriddin Ayni")
    case 10:
        print("Mir Said Ali Hamadoni")
    case 20:
        print("Abuali ibni Sino")
    case 50:
        print("Bobojon Gafurov")
    case 100:
        print("Ismoili Somoni")
    case 200:
        print("Nusratullo Makhsum")
    case 500:
        print("Abuabdullo Rudaki")
    case _:
        print("Invalid denomination")
```

### Example 3: Vowel or Consonant

**Problem**: Determine if a letter is a vowel, consonant, or the special case of 'y'.

```python
# Read a letter from the user
letter = input().lower()

# Determine vowel, consonant, or special case
match letter:
    case 'y':
        print("sometimes vowel, sometimes consonant")
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("vowel")
    case _:
        print("consonant")
```

### Example 4: Temperature Classification

**Problem**: Classify temperature ranges using guard conditions.

```python
# Read temperature
temperature = int(input())

# Classify temperature with guard conditions
match temperature:
    case temp if temp < 0:
        print("freezing")
    case temp if temp < 20:
        print("cold")
    case temp if temp < 30:
        print("warm")
    case _:
        print("hot")
```

Cases are checked from top to bottom, so `cold` doesn't need `0 <= temp`:
any temperature below 0 already matched `freezing`.

Guards work, but when every case is a guard, as here, an `if-elif` chain
says the same thing more simply:

```python
if temperature < 0:
    print("freezing")
elif temperature < 20:
    print("cold")
elif temperature < 30:
    print("warm")
else:
    print("hot")
```

## Common Match Patterns

- Multiple values with OR (`|`)
- Guard conditions with `if`
- Wildcard pattern (`_`)

## When to Use Match vs If-Elif

- Use `match` when checking a single variable against multiple discrete values
- Use `if-elif` when you need complex boolean conditions or range checking
- `match` is cleaner for value-based branching, `if-elif` is better for condition-based logic
- Guards are for the occasional condition inside a `match`; if every case needs one, switch to `if-elif`
