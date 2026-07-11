<details>
<summary><strong>Hint</strong></summary>

- Handle edge cases: empty sub is always a sublist
- Iterate through main_list with a sliding window
- For each position i, check if main_list[i:i+len(sub)] == sub
- Return True if found, False otherwise

</details>

## Note

- Empty list is considered a sublist of any list
- Elements must be consecutive
- [3, 7] is not a sublist of [2, 3, 5, 7, 11] because they're not consecutive
