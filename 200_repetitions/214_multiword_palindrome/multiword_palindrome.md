# Multiple Word Palindromes

Determine if a phrase is a palindrome when spacing (and optionally punctuation) is ignored.

## Task
- Read a string from the user
- Check if it's a palindrome ignoring spaces
- **Optional Challenge:** Also ignore punctuation and treat uppercase/lowercase as equivalent
- Display whether it is or isn't a palindrome

## Examples of Multi-word Palindromes
- "go dog"
- "flee to me remote elf"
- "some men interpret nine memos"
- "A man a plan a canal Panama" (with case/punctuation ignored)

## Examples
**Example 1:**
```
Enter a string: go dog
```
```
go dog is a palindrome
```

**Example 2:**
```
Enter a string: flee to me remote elf
```
```
flee to me remote elf is a palindrome
```

**Example 3:**
```
Enter a string: hello world
```
```
hello world is not a palindrome
```

## Logic
- Remove spaces from the string
- Convert to same case (for advanced version)
- Remove punctuation (for advanced version)
- Check if modified string is a palindrome

## Hints
- Use string.replace(" ", "") to remove spaces
- Use string.lower() to convert to lowercase
- Use string.isalnum() to check if character is alphanumeric
- Build a new string with only letters/numbers for comparison
