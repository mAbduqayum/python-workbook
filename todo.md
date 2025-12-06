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

- [x] `chars_count`: Count frequency of each character in a string. Return a dictionary.
- [x] `most_frequent_char`: Return the character that appears most often.
- [x] `first_unique_char`: Return the first character that appears only once.

#### Encoding & Decoding

- [x] `read_aloud`: Convert digits to words.
- [x] `morse_encode`: Text → Morse code.
  *Historical note: Morse code was developed in the 1830s for telegraph communication.*
- [x] `morse_decode`: Morse code → Text.
  *Note: Encoding transforms data into another format using a known scheme (reversible). Different from encryption (
  secret) and hashing (one-way).*
- [x] `roman_to_int`: Convert Roman numeral string to integer. `"XIV"` → `14`
- [x] `text_messaging`: Convert message → old cellphone key presses (T9 style).

| Key | Symbols | Key | Symbols |
|-----|---------|-----|---------|
| 1   | .,?!:   | 6   | MNO     |
| 2   | ABC     | 7   | PQRS    |
| 3   | DEF     | 8   | TUV     |
| 4   | GHI     | 9   | WXYZ    |
| 5   | JKL     | 0   | space   |

#### Mid

- [x] `anagram` function name: is_anagram
- [x] `phrase_anagram` function name: is_phrase_anagram
- [x] `group_anagrams`: Group words that are anagrams of each other
- [x] Two Sum (The "Complement" Search)
- [x] Isomorphic Strings

#### Hard

- [x] Longest Substring Without Repeating Characters


### Files

- [ ] head
- [ ] tail
- [ ] cat
- [ ] lines count
- [ ] words count
- [ ] longest word
- [ ] letter frequency
- [ ] word frequency
- [ ] remove comments
- [ ] What’s that Element Again?
  Write a program that reads a file containing information about chemical elements
  and stores it in one or more appropriate data structures. Then your program should
  read and process input from the user. If the user enters an integer then your program
  should display the symbol and name of the element with the number of protons
  entered. If the user enters a non-integer value then your program should display the
  number of protons for the element with that name or symbol. Your program should
  display an appropriate error message if no element exists for the name, symbol or
  number of protons entered. Continue to read input from the user until a blank line is
  entered.
- [ ] Spell Checker
  A spell checker can be a helpful tool for people who struggle to spell words correctly.
  In this exercise, you will write a program that reads a file and displays all of the words
  in it that are misspelled. Misspelled words will be identified by checking each word
  in the file against a list of known words. Any words in the user’s file that do not
  appear in the list of known words will be reported as spelling mistakes.
  The user will provide the name of the file to check for spelling mistakes as a
  command line argument. Your program should display an appropriate error message
  if the command line argument is missing. An error message should also be displayed
  if your program is unable to open the user’s file. When creating your solution to this exercise so that words followed by a comma, period or other punctuation mark are not reported as spelling mistakes. Ignore the capitalization of the words when checking their spelling.
- [ ] Repeated Words
  Spelling mistakes are only one of many different kinds of errors that might appear in
  a written work. Another error that is common for some writers is a repeated word. For
  example, an author might inadvertently duplicate a word, as shown in the following
  sentence:
  At least one value must be entered
  entered in order to compute the average.
  Some word processors will detect this error and identify it when a spelling or grammar
  check is performed.
  In this exercise you will write a program that detects repeated words in a text file.
  When a repeated word is found your program should display a message that contains
  the line number and the repeated word. Ensure that your program correctly handles
  the case where the same word appears at the end of one line and the beginning of the
  following line, as shown in the previous example. The name of the file to examine will
  be provided as the program’s only command line argument. Display an appropriate
  error message if the user fails to provide a command line argument, or if an error
  occurs while processing the file.
- [ ] Redacting Text in a File
  Sensitive information is often removed, or redacted, from documents before they
  are released to the public. When the documents are released it is common for the
  redacted text to be replaced with black bars.
  In this exercise you will write a program that redacts all occurrences of sensitive
  words in a text file by replacing them with asterisks. Your program should redact
  sensitive words wherever they occur, even if they occur in the middle of another
  word. The list of sensitive words will be provided in a separate text file. Save the
  redacted version of the original text in a new file. The names of the original text file,
  sensitive words file, and redacted file will all be provided by the user.
  You may find the replace method for strings helpful when completing this
  exercise. Information about the replace method can be found on the Internet.
  For an added challenge, extend your program so that it redacts words in a case
  insensitive manner. For example, if exam appears in the list of sensitive words then
  redact exam, Exam, ExaM and EXAM, among other possible capitalizations.
- [ ] Missing Comments
  When one writes a function, it is generally a good idea to include a comment that
  outlines the function’s purpose, its parameters and its return value. However, some-
  times comments are forgotten, or left out by well-intentioned programmers that plan
  to write them later but then never get around to it.
  Create a Python program that reads one or more Python source files and identifies
  functions that are not immediately preceded by a comment. For the purposes of this
  exercise, assume that any line that begins with def, followed by a space, is the
  beginning of a function definition. Assume that the comment character, #, will be
  the first character on the previous line when the function has a comment. Display the
  names of all of the functions that are missing comments, along with the file name
  and line number where the function definition is located.
  The user will provide the names of one or more Python files as command line
  arguments, all of which should be analyzed by your program. An appropriate error
  message should be displayed for any files that do not exist or cannot be opened. Then
  your program should process the remaining files.
- [ ] Words with Six Vowels in Order
  There is at least one word in the English language that contains each of the vowels
  A, E, I, O, U and Y exactly once and in order. Write a program that searches a file
  containing a list of words and displays all of the words that meet this constraint. The
  user will provide the name of the file that will be searched. Display an appropriate
  error message and exit the program if the user provides an invalid file name, or
  if something else goes wrong while your program is searching for words with six
  vowels in order.

### General

- [ ] Create a table to compare code complexity of common methods in a list, set, dict
- [ ] more complete version of previous task: list, set, dict, tuple, string, queue[list], stack[list], linked list
- [ ] Create a table to explain the difference between hashing, encryption, encoding