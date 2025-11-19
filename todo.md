## 200_repetitions

- n numbers
- n even numbers
- n odd numbers
- n numbers divisible by 10
- explain about Σ and Π (Pi) using loops
- read input from the user until user enters
  skip (continue) or quit (break)
- table of numbers:
 1  2   3   4   5   6   7   8   9   10
11 12  13                           20
.
.
.
91 ...                             100

### Todos

-[ ] collatz question: output in multiple lines to make it easier

## 300_functions

- time_it (which prints how much time the function took?)

## 400_lists

- List Revers
  Write function reverse(values) that returns the elements of the original list in reverse
  order—of course without calling the reverse() function of the list.
- List Revers (b): List Reverse Inplace
  What is different if you want to implement reversing the order inplace to be
  memory-optimal for very large datasets? What should be given then?
- Well-Formed Braces
- Maximum Profit
  Imagine that you have a sequence of prices ordered in time and that you want to
  calculate the maximum profit. The challenge is to determine at which time (or value, in
  this case) it would be ideal to buy and to sell. Write function max_revenue(prices) for
  this purpose, where the temporal order is expressed by the index in the list.
- Read aloud -> 42 -> “FOUR TWO”
- Joiner - custom join function
- Compare Versions: Write function compare_versions(version1, version2) that permits you to compare
  version numbers in the format MAJOR.MINOR.PATCH with each other, thereby the
  specification of PATCH is optional. In particular, the return value should be represented
  in the form of the characters <, =, and >.

### sets

-[ ] Common Elements
-[ ] number of duplicates in a list
-[ ] remove duplicates from list
-[ ] remove duplicate letters from string. (tell to use list instead of modifying mutable string to prevent string
  recreation each time to prevent slowdown)
-[ ] Exercise 6: Longest Sequence
  Suppose you are modeling stock prices or altitudes of a track by a list of numbers. Find
  the longest sequence of numbers whose values ascend or at least stay the same. Write
  function find_longest_growing_sequence(values).
  Note: make questions more interesting
-[ ] rotative-in:
  Consider two strings, str1 and str2, where the first string is supposed to be longer than
  the second. Figure out if the first one contains the other one. In doing so, the characters
  within the first string may also be rotated. Characters can be moved from the beginning
  or the end to the opposite position (even repeatedly). To do this, create function
  contains_rotation(str1, str2), which is case-insensitive during the check.

### dicts

-[ ] Excel Magic Select

| Initial value | Count | Result                                                                   |
|---------------|-------|--------------------------------------------------------------------------|
| 1             | 7     | [1, 2, 3, 4, 5, 6, 7]                                                    |
| 5             | 4     | [5, 6, 7, 8]                                                             |
| FRIDAY        | 8     | [FRIDAY, SATURDAY, SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY] |