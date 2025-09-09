# Exercise: Free Fall

Write a program that calculates how fast an object is traveling when it hits the ground after being dropped.

## Task
- Read the height from which the object is dropped in meters (as `float`)
- Calculate the final velocity when it hits the ground
- Display the result

## Examples
**Example 1:**
```
Enter height (meters): 10
Final velocity: 14.00 m/s
```

**Example 2:**
```
Enter height (meters): 50
Final velocity: 31.30 m/s
```

**Example 3:**
```
Enter height (meters): 100
Final velocity: 44.27 m/s
```

## Formula
`vf = √(vi² + 2ad)` where:
- `vi = 0` (initial velocity, dropped)
- `a = 9.8 m/s²` (acceleration due to gravity)  
- `d = height` (distance fallen)

## Note
- Use `.2f` formatting to display 2 decimal places
- Use `math.sqrt()` for square root calculation
- Gravity acceleration: `9.8 m/s²`