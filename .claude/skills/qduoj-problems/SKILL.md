---
name: qduoj-problems
description: Create QDUOJ online judge problems (single or batch) with proper format. Use when user mentions creating QDUOJ problems, coding challenges, test cases, or OJ import.
---

# QDUOJ Problem Creator

Create QDUOJ problems in the `QDUOJ_import/` directory following the official import format.

## CRITICAL: Template Fields Cannot Be Empty

**ALL template fields (`prepend`, `template`, `append`) MUST be non-empty strings.**

Empty strings like `"prepend": ""` will cause a **server error** on import because QDUOJ's `TemplateSerializer` requires non-empty CharField values.

- Correct: `"prepend": "# No imports needed"`
- Wrong: `"prepend": ""`

## Single Problem Creation

### Instructions

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
       "hint": {"format": "html", "value": ""},
       "samples": [{"input": "sample input", "output": "sample output"}],
       "test_case_score": [
           {"input_name": "1.in", "output_name": "1.out", "score": 10}
       ],
       "time_limit": 1000,
       "memory_limit": 128,
       "difficulty": "Low",
       "template": {
           "Python3": {
               "prepend": "# No imports needed",
               "template": "# Your code here\npass",
               "append": "# End of submission"
           }
       },
       "spj": null,
       "rule_type": "ACM",
       "source": "",
       "answers": [],
       "tags": ["beginner"]
   }
   ```

4. Create test cases in `testcase/` directory (scores should sum to 100)

5. **Create the import ZIP** after all files are ready (see ZIP Creation section)

## Code Templates

Templates allow you to wrap user submissions with boilerplate code.

### When to Use Templates

If the source problem markdown has a `## Template:` section, use that template in QDUOJ with I/O handled in the `append` section.

### How Templates Work

When a submission is judged, QDUOJ combines the code like this:
```python
code = f"{template['prepend']}\n{user_code}\n{template['append']}"
```

- **prepend**: Code added BEFORE the user's submission (hidden from user)
- **template**: The starter code shown to the user in the editor
- **append**: Code added AFTER the user's submission (hidden from user)

### Template Structure

```json
"template": {
    "Python3": {
        "prepend": "# Prepend",
        "template": "def solve(n: int) -> int:\n    # Your code here\n    pass",
        "append": "# Append"
    }
}
```

**Critical**: `prepend` and `append` CANNOT be empty strings. Use `"# Prepend"` and `"# Append"` as placeholders.

### Template Example: Function Implementation

Student implements a function, template handles I/O:

```json
"template": {
    "Python3": {
        "prepend": "# Prepend",
        "template": "def is_leap_year(year: int) -> bool:\n    # Your code here\n    pass",
        "append": "if __name__ == \"__main__\":\n    year = int(input())\n    if is_leap_year(year):\n        print(\"Leap year\")\n    else:\n        print(\"Not leap year\")"
    }
}
```

In this example:
- User only sees and edits the `is_leap_year` function
- The `append` section handles reading input and printing output
- Test cases use standard I/O but user focuses on logic

### Template Example: Hidden Test Harness

```json
"template": {
    "Python3": {
        "prepend": "import sys\nfrom io import StringIO",
        "template": "def process(data: list[int]) -> int:\n    # Your code here\n    pass",
        "append": "# Test harness\nresult = process([int(x) for x in input().split()])\nprint(result)"
    }
}
```

## Batch Problem Creation

When creating multiple problems at once:

1. **Plan the problems first**: List all problems with their folder numbers before creating any files

2. **Create sequential folders**: Each problem gets its own numbered folder
   ```
   QDUOJ_import/
   ├── 1/
   │   ├── problem.json
   │   └── testcase/
   ├── 2/
   │   ├── problem.json
   │   └── testcase/
   └── 3/
       ├── problem.json
       └── testcase/
   ```

3. **Use unique display_ids**: Each problem needs a unique `display_id` (max 24 characters)
   - Pattern: `{Topic}{Number}` (e.g., `LeapYear001`, `PrintName001`)

4. **Batch ZIP creation**: Include all problems in a single ZIP for atomic import
   ```python
   import os
   import zipfile
   from pathlib import Path

   def create_batch_qduoj_zip(source_folders: list[str], output_filename: str):
       """Create QDUOJ import ZIP with sequential numbering starting from 1."""
       with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
           for idx, source_dir in enumerate(source_folders, start=1):
               source_path = Path(source_dir)
               for root, dirs, files in os.walk(source_path):
                   for file in files:
                       file_path = os.path.join(root, file)
                       rel_path = os.path.relpath(file_path, source_path)
                       arcname = os.path.join(str(idx), rel_path)
                       zipf.write(file_path, arcname)
       print(f"Created {output_filename} with {len(source_folders)} problems")

   # Example: batch import of problems 1-5
   folders = [f"QDUOJ_import/{i}" for i in range(1, 6)]
   create_batch_qduoj_zip(folders, "QDUOJ_import/batch_import.zip")
   ```

## ZIP Creation

### Single Problem ZIP
```python
import os
import zipfile
from pathlib import Path

def create_qduoj_zip(source_folder: str, output_filename: str):
    """Create QDUOJ import ZIP with folder as 1/."""
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        source_path = Path(source_folder)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, source_path)
                arcname = os.path.join("1", rel_path)
                zipf.write(file_path, arcname)
    print(f"Created {output_filename}")

# Example: create ZIP from folder N
create_qduoj_zip("QDUOJ_import/N", "QDUOJ_import/problem_name_import.zip")
```

### Expected ZIP Structure
The QDUOJ importer expects this exact structure inside the ZIP:
```
1/
├── problem.json
└── testcase/
    ├── 1.in
    ├── 1.out
    └── ...
2/
├── problem.json
└── testcase/
    └── ...
```

**Critical**: The importer iterates `for i in range(1, count+1)` - folders MUST be numbered sequentially starting from 1 with no gaps.

## Critical Rules

- **No hints by default**: Leave `hint` value empty (`""`) unless explicitly requested
- **Sequential numbering**: ZIP folders MUST be `1/`, `2/`, `3/`, etc. - no gaps, always start from 1
- **Template fields**: If using templates, `prepend` and `append` CANNOT be empty strings - use `"# Prepend"` and `"# Append"` as placeholders
- **Format objects**: Description fields must use `{"format": "html", "value": "..."}`
- **Difficulty**: Use "Low", "Mid", or "High"
- **Rule type**: Use "ACM" (pass/fail) or "OI" (partial scoring)
- **Display ID**: Max 24 characters, must be unique per problem
- **Test case scores**: Must sum to 100
- **Always create ZIP**: After creating problem folder(s), generate the import ZIP file

## Import Steps (for reference)

1. Go to QDUOJ Admin -> Problem -> Import QDUOJ Problems (beta)
2. Upload the ZIP file
3. All problems are imported atomically (within a transaction)
4. Problems are created as hidden by default
5. Edit each problem to make it visible and restrict languages

Ask the user for problem details before creating.
