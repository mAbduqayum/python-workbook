# Is a String a Palindrome?

Determine whether a string is a palindrome (identical forward and backward).

## Task
- Read a string from the user
- Use a loop to check if it's a palindrome
- Display whether it is or isn't a palindrome

## Examples of Palindromes
- "anna"
- "civic"
- "level"
- "hannah"
- "racecar"

## Examples
**Example 1:**
```
Enter a string: anna
```
```
anna is a palindrome
```

**Example 2:**
```
Enter a string: hello
```
```
hello is not a palindrome
```

**Example 3:**
```
Enter a string: racecar
```
```
racecar is a palindrome
```

## Logic
- Compare characters from start and end moving inward
- Use a loop to check if string[i] == string[-(i+1)]
- Or reverse the string and compare with original

## Hints
- Method 1: Use loop to compare first/last, second/second-last, etc.
- Method 2: Reverse string and compare: string == string[::-1]
- For loop approach, check up to len(string) // 2
- If any pair doesn't match, it's not a palindrome

## Fun Facts
- Aibohphobia: fear of palindromes (itself a palindrome!)
- Ailihphilia: love of palindromes
