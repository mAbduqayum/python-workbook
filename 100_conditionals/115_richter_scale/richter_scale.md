# Exercise: Richter Scale

Write a program that reads an earthquake magnitude and displays the appropriate descriptor according to the Richter scale.

## Task
- Read an earthquake magnitude from the user
- Display the corresponding earthquake descriptor
- Handle all magnitude ranges appropriately

## Richter Scale Classifications
| Magnitude | Descriptor |
|-----------|------------|
| Less than 2.0 | Micro |
| 2.0 to less than 3.0 | Very Minor |
| 3.0 to less than 4.0 | Minor |
| 4.0 to less than 5.0 | Light |
| 5.0 to less than 6.0 | Moderate |
| 6.0 to less than 7.0 | Strong |
| 7.0 to less than 8.0 | Major |
| 8.0 to less than 10.0 | Great |
| 10.0 or more | Meteoric |

## Examples
**Example 1:**
```
1.5
```
```
Micro
```

**Example 2:**
```
2.5
```
```
Very Minor
```

**Example 3:**
```
5.5
```
```
Moderate
```

**Example 4:**
```
7.2
```
```
Major
```

**Example 5:**
```
8.9
```
```
Great
```

**Example 6:**
```
10.5
```
```
Meteoric
```

