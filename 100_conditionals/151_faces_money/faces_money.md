# Exercise 110: Faces on Money

It is common for images of a country's previous leaders, or other individuals of historical significance, to appear on its money. Write a program that identifies which individual appears on US banknotes.

## Task
- Read the denomination of a US banknote from the user
- Display the name of the individual that appears on that banknote
- Display an appropriate error message if no such note exists

## US Banknote Reference Table
| Amount | Individual         |
|--------|--------------------|
| $1     | George Washington  |
| $2     | Thomas Jefferson   |
| $5     | Abraham Lincoln    |
| $10    | Alexander Hamilton |
| $20    | Andrew Jackson     |
| $50    | Ulysses S. Grant   |
| $100   | Benjamin Franklin  |

## Examples
**Example 1:**
```
1
George Washington
```

**Example 2:**
```
20
Andrew Jackson
```

**Example 3:**
```
100
Benjamin Franklin
```

**Example 4:**
```
2
Thomas Jefferson
```

**Example 5:**
```
25
Invalid denomination
```

**Example 6:**
```
500
Invalid denomination
```

## Note
- Accept input as integer values (1, 2, 5, 10, 20, 50, 100)
- While $2 bills are rarely seen, they are legal tender
- High denomination bills ($500, $1000, etc.) were discontinued in 1969
- Display appropriate error messages for invalid denominations
