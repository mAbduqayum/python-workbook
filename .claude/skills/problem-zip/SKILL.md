---
name: problem-zip
description: Create QDUOJ import ZIP files from problem folders. Use when user wants to export, package, or create ZIP for OJ problem import.
---

# QDUOJ Import ZIP Creator

Create a QDUOJ import ZIP file from problem folder(s) in `QDUOJ_import/`.

## Instructions

1. Ask which problem folder(s) to include (e.g., `4/` or multiple like `1/ 2/ 3/`)

2. Create the ZIP with proper structure - folders must be renumbered to start from `1/`:
   - Single folder: `4/` becomes `1/` in the ZIP
   - Multiple folders: `3/ 5/ 7/` become `1/ 2/ 3/` in the ZIP

3. Use this Python script pattern:
   ```python
   import os
   import zipfile
   from pathlib import Path

   def create_qduoj_zip(source_folders: list[str], output_filename: str):
       """Create QDUOJ import ZIP with proper sequential numbering."""
       with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
           for idx, source_dir in enumerate(source_folders, start=1):
               source_path = Path(source_dir)
               for root, dirs, files in os.walk(source_path):
                   for file in files:
                       file_path = os.path.join(root, file)
                       rel_path = os.path.relpath(file_path, source_path)
                       # Renumber to sequential starting from 1
                       arcname = os.path.join(str(idx), rel_path)
                       zipf.write(file_path, arcname)
       print(f"Created {output_filename}")

   # Example: single folder
   create_qduoj_zip(["QDUOJ_import/4"], "problem_name_import.zip")

   # Example: multiple folders
   create_qduoj_zip(["QDUOJ_import/1", "QDUOJ_import/2"], "batch_import.zip")
   ```

4. Save the ZIP in `QDUOJ_import/` with a descriptive name like `{problem_name}_import.zip`

## Critical Rules

- **Sequential numbering in ZIP**: The ZIP MUST contain folders `1/`, `2/`, `3/`, etc.
- The QDUOJ importer iterates `for i in range(1, count+1)` - gaps will cause import failure
- Output ZIP should be placed in `QDUOJ_import/` directory

## Import Steps (for reference)

1. Go to QDUOJ Admin -> Problem -> Import QDUOJ Problems (beta)
2. Upload the ZIP file
3. Problems will be created as hidden by default
4. Edit each problem to make it visible and restrict languages
