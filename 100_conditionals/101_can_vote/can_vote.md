# Can Vote

Write a program that determines if a person can vote based on their age.

## Task
- Read a person's age from the user
- Determine if they are eligible to vote
- Display "can vote" or "cannot vote"

## Examples
**Example 1:**
```
18
```
```
can vote
```

**Example 2:**
```
17
```
```
cannot vote
```

**Example 3:**
```
25
```
```
can vote
```

**Example 4:**
```
16
```
```
cannot vote
```

**Example 5:**
```
65
```
```
can vote
```

## Logic
- If age >= 18: can vote
- If age < 18: cannot vote

## Note
- Voting age is 18 in most countries
- Use the simple comparison operator
- Handle integer ages
