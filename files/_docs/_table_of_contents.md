# Table of Contents

```mermaid
mindmap
    root((Files))
        Reading
            open with r
            read
            readline
            readlines
        Writing
            open with w
            write
            writelines
        Appending
            open with a
        Context Manager
            with statement
            automatic close
        Processing
            line by line
            word counting
            searching
            filtering
        Encoding
            UTF-8
            encoding argument
            str vs bytes
```

## Recommended Reading Order

1. [`file_basics.md`](file_basics.md) - Opening, reading, writing, and context managers
2. [`utf8_encoding.md`](utf8_encoding.md)

## Practice Questions

### Beginner (Reading & Writing)

1. [`read_file_content`](../read_file_content/read_file_content.md) - Read entire file as string
2. [`count_lines`](../count_lines/count_lines.md) - Count number of lines
3. [`write_lines`](../write_lines/write_lines.md) - Write list of lines to file
4. [`append_line`](../append_line/append_line.md) - Append single line to file
5. [`head`](../head/head.md) - Return first n lines
6. [`tail`](../tail/tail.md) - Return last n lines

### Intermediate (Text Processing)

1. [`count_words`](../count_words/count_words.md) - Count total words in file
2. [`find_longest_word`](../find_longest_word/find_longest_word.md) - Find longest word
3. [`word_frequency`](../word_frequency/word_frequency.md) - Count word occurrences
4. [`search_lines`](../search_lines/search_lines.md) - Find lines containing search term
5. [`remove_blank_lines`](../remove_blank_lines/remove_blank_lines.md) - Copy file without blank lines
6. [`merge_files`](../merge_files/merge_files.md) - Merge multiple files into one
7. [`letter_frequency`](../letter_frequency/letter_frequency.md) - Count letter occurrences
8. [`remove_comments`](../remove_comments/remove_comments.md) - Strip Python comment lines
9. [`find_repeated_words`](../find_repeated_words/find_repeated_words.md) - Detect consecutive duplicates
10. [`six_vowel_words`](../six_vowel_words/six_vowel_words.md) - Find words with AEIOUY in order

### Advanced (Multi-file & Analysis)

1. [`spell_checker`](../spell_checker/spell_checker.md) - Check spelling against dictionary
2. [`redact_text`](../redact_text/redact_text.md) - Replace sensitive words with asterisks
3. [`find_missing_comments`](../find_missing_comments/find_missing_comments.md) - Find uncommented functions
4. [`element_lookup`](../element_lookup/element_lookup.md) - Look up chemical elements from data file
