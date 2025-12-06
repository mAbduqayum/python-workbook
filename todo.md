## repetitions

- n numbers
- n even numbers
- n odd numbers
- n numbers divisible by 10
- explain about Σ and Π (Pi) using loops
- read input from the user until the user enters
  skip (continue) or quit (break)
- table of numbers:

```table
 1  2   3   4   5   6   7   8   9   10
11 12  13                           20
.
.
.
91 ...                             100
```

### Todos

-[ ] collatz question: output in multiple lines to make it easier

## functions

- time_it (which prints how much time the function took?)

## lists

- `List Revers`
  Write function reverse(values) that returns the elements of the original list in reverse
  order—of course without calling the reverse() function of the list.
- `List Revers (b)`: List Reverse Inplace
  What is different if you want to implement reversing the order inplace to be
  memory-optimal for a very large datasets? What should be given then?
- `Well-Formed Braces`
- `Maximum Profit`
  Imagine that you have a sequence of prices ordered in time and that you want to
  calculate the maximum profit. The challenge is to determine at which time (or value, in
  this case) it would be ideal to buy and to sell. Write function max_revenue(prices) for
  this purpose, where the temporal order is expressed by the index in the list.
- `Joiner` - custom join function
- `Compare` Versions: Write function compare_versions(version1, version2) that permits you to compare
  version numbers in the format MAJOR.MINOR.PATCH with each other, thereby the
  specification of PATCH is optional. In particular, the return value should be represented
  in the form of the characters <, =, and >.
- [ ] `Longest Sequence`
  Suppose you are modeling stock prices or altitudes of a track by a list of numbers. Find
  the longest sequence of numbers whose values ascend or at least stay the same. Write
  the function find_longest_growing_sequence (values).
  Note: make questions more interesting
- [ ] `Addition of Digits`
- [ ] Excel Magic Select

| Initial value | Count | Result                                                                   |
|---------------|-------|--------------------------------------------------------------------------|
| 1             | 7     | [1, 2, 3, 4, 5, 6, 7]                                                    |
| 5             | 4     | [5, 6, 7, 8]                                                             |
| FRIDAY        | 8     | [FRIDAY, SATURDAY, SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY] |

- [ ] rotative-in:
  Consider two strings, str1 and str2, where the first string is supposed to be longer than
  the second. Figure out if the first one contains the other one. In doing so, the characters
  within the first string may also be rotated. Characters can be moved from the beginning
  or the end to the opposite position (even repeatedly). To do this, create a function contains_rotation   (str1, str2),
  which is case-insensitive during the check.

### sets

- [x] `uniques` from list
- [x] `list_union`
- [x] `list_intersection`
- [x] Subset Checker - Determine if one set is a subset of another. Good for understanding containment relationships.
- [x] Symmetric Difference - Find elements that are in either of two sets but not in both. Teaches XOR-like set
  operations.
- [x] remove duplicate letters from string.
  tell to use list instead of modifying mutable string to prevent string
  recreation each time to prevent slowdown)
- [x] Find Missing Numbers - Given a range (1 to n) and an array with some missing numbers, find which numbers are
  missing using set difference.
- [x] Pangram Checker
- [x] The First Recurring Character
  Problem: Given a string, return the first character that appears a second time.
  Input: `ABCA`
  Output: `A`
  Problem: Given an array of integers nums and an integer target, return true if two numbers in the array add up to
  target.
- [ ] convert all function argument types from list to set.

### sets advanced

- [x] Longest Consecutive Sequence

### dicts

#### Fundamentals (Warm-up)

- [ ] `chars_count`: Count frequency of each character in a string. Return a dictionary.
- [ ] `most_frequent_char`: Return the character that appears most often.
- [ ] `first_unique_char`: Return the first character that appears only once.

#### Encoding & Decoding

- [ ] `read_aloud`: Convert digits to words.
- [ ] `morse_encode`: Text → Morse code.
  *Historical note: Morse code was developed in the 1830s for telegraph communication.*
- [ ] `morse_decode`: Morse code → Text.
  *Note: Encoding transforms data into another format using a known scheme (reversible). Different from encryption (
  secret) and hashing (one-way).*
- [ ] `roman_to_int`: Convert Roman numeral string to integer. `"XIV"` → `14`
- [ ] `text_messaging`: Convert message → old cellphone key presses (T9 style).

| Key | Symbols | Key | Symbols |
|-----|---------|-----|---------|
| 1   | .,?!:   | 6   | MNO     |
| 2   | ABC     | 7   | PQRS    |
| 3   | DEF     | 8   | TUV     |
| 4   | GHI     | 9   | WXYZ    |
| 5   | JKL     | 0   | space   |

#### Mid

- [ ] `anagram` function name: is_anagram
- [ ] `phrase_anagram` function name: is_phrase_anagram
- [ ] `group_anagrams`: Group words that are anagrams of each other
- [ ] Two Sum (The "Complement" Search)
- [ ] Isomorphic Strings

#### Hard

- [ ] Longest Substring Without Repeating Characters

### General

- [ ] Create a table to compare code complexity of common methods in a list, set, dict
- [ ] more complete version of previous task: list, set, dict, tuple, string, queue[list], stack[list], linked list
- [ ] Create a table to explain the difference between hashing, encryption, encoding