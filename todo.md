## 200_repetitions

- n numbers
- n even numbers
- n odd numbers
- n numbers divisible by 10
- explain about Σ and Π (Pi) using loops
- read input from the user until user enters
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

## 300_functions

- time_it (which prints how much time the function took?)

## lists

- `List Revers`
  Write function reverse(values) that returns the elements of the original list in reverse
  order—of course without calling the reverse() function of the list.
- `List Revers (b)`: List Reverse Inplace
  What is different if you want to implement reversing the order inplace to be
  memory-optimal for very large datasets? What should be given then?
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
  function find_longest_growing_sequence(values).
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
  or the end to the opposite position (even repeatedly). To do this, create function
  contains_rotation(str1, str2), which is case-insensitive during the check.

### sets

- [ ] `common_elements` in two lists
- [ ] `duplicates_count` in list
- [ ] `remove_duplicates` in list
- [ ] `uniques` list from list
- [ ] remove duplicate letters from string.
  tell to use list instead of modifying mutable string to prevent string
  recreation each time to prevent slowdown)

### dicts

- [ ] `text_messaging`: message -> old cellphone clicks

| Key | Symbols |
|-----|---------|
| 1   | .,?!:   |
| 2   | ABC     |
| 3   | DEF     |
| 4   | GHI     |
| 5   | JKL     |
| 6   | MNO     |
| 7   | PQRS    |
| 8   | TUV     |
| 9   | WXYZ    |
| 0   | space   |

- [ ] `morse_code`
  Add historical note about morse code
- [ ] `morse_encode`
  Add note about what does encoding mean
- [ ] `read_aloud` -> 42 -> “FOUR TWO”
- [ ] `most_frequent_elements`
- [ ] `chars_map`
- [ ] `anagram` function name: is_anagram
- [ ] `phrase_anagram` function name: is_phrase_anagram

### General

- [ ] Create a table to compare code complexity of common methods in list, set, dict
- [ ] more complete version of previous task: list, set, dict, tuple, string, queue[list], stack[list], linked list
- [ ] Create a table to explain difference between hashing, encryption, encoding