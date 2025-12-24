---
name: problem
description: Create QDUOJ online judge problems with proper format. Use when user mentions creating OJ problems, coding challenges, test cases, or QDUOJ import.
---

# QDUOJ Problem Creator

Create a new QDUOJ problem in the `QDUOJ_import/` directory following the official import format.

## Instructions

1. Find the next available sequential folder number in `QDUOJ_import/` (e.g., if `1/`, `2/`, `3/` exist, create `4/`)

2. Create the folder structure:
   ```
   QDUOJ_import/N/
   ├── problem.json
   └── testcase/
       ├── 1.in
       ├── 1.out
       ├── 2.in
       ├── 2.out
       └── ...
   ```

3. Create `problem.json` with this structure:
   ```json
   {
       "display_id": "UniqueID001",
       "title": "Problem Title",
       "description": {"format": "html", "value": "<p>Description</p>"},
       "input_description": {"format": "html", "value": "<p>Input format</p>"},
       "output_description": {"format": "html", "value": "<p>Output format</p>"},
       "hint": {"format": "html", "value": "<p>Hints</p>"},
       "samples": [{"input": "sample input", "output": "sample output"}],
       "test_case_score": [
           {"input_name": "1.in", "output_name": "1.out", "score": 10}
       ],
       "time_limit": 1000,
       "memory_limit": 128,
       "difficulty": "Low",
       "template": {},
       "spj": null,
       "rule_type": "ACM",
       "source": "",
       "answers": [],
       "tags": ["beginner"]
   }
   ```

4. Create test cases in `testcase/` directory (scores should sum to 100)

## Critical Rules

- **Sequential numbering**: Folders MUST be numbered `1/`, `2/`, `3/`, etc. - no gaps!
- **Template fields**: If using templates, `prepend` and `append` CANNOT be empty strings - use `"# Prepend"` and `"# Append"` as placeholders
- **Format objects**: Description fields must use `{"format": "html", "value": "..."}`
- **Difficulty**: Use "Low", "Mid", or "High"
- **Rule type**: Use "ACM" (pass/fail) or "OI" (partial scoring)

## Template Example (Optional)

```json
"template": {
    "Python3": {
        "prepend": "# Prepend",
        "template": "def solve():\n    # Your code here\n    pass\n\nsolve()",
        "append": "# Append"
    }
}
```

Ask the user for problem details before creating.
