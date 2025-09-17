# Exercise 106: Sound Levels

Write a program that reads a sound level in decibels from the user and reports information about the sound based on common noise levels.

## Task
- Read a sound level in decibels from the user
- Display the corresponding noise if it matches exactly
- If the level is between noises, indicate which noises it falls between
- Handle values outside the range appropriately

## Sound Level Reference Table
| Noise         | Decibel Level |
|---------------|---------------|
| Quiet Room    | 40 dB         |
| Alarm Clock   | 70 dB         |
| Gas Lawnmower | 106 dB        |
| Jackhammer    | 130 dB        |

## Examples
**Example 1:**
```
70
Alarm Clock
```

**Example 2:**
```
55
Between Quiet Room and Alarm Clock
```

**Example 3:**
```
120
Between Gas Lawnmower and Jackhammer
```

**Example 4:**
```
25
Quieter than Quiet Room
```

**Example 5:**
```
140
Louder than Jackhammer
```

**Example 6:**
```
106
Gas Lawnmower
```

## Note
- Handle exact matches first, then ranges between sounds
- Use appropriate conditional statements to categorize the input
- Consider edge cases for values below 40 dB and above 130 dB
- Format output messages appropriately
