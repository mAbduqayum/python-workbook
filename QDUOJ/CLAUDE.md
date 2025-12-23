# QDUOJ Problem Creation Guide

## Overview
Create programming problems for a self-hosted QDUOJ (QingDao University Online Judge) platform.

## Test Case Format

### File Structure
- **Naming**: `1.in`, `1.out`, `2.in`, `2.out`, etc.
- **ZIP Structure**: Flat (files directly in zip root, NO subdirectories)
- **Line Endings**: Unix (LF)

### Creating ZIP
```bash
cd /path/to/testcases
zip ../testcases.zip *.in *.out
```

**IMPORTANT**: Do NOT include subdirectories in zip. First attempt with `1/` folder failed. Flat structure works.

## Default Settings

| Setting | Value |
|---------|-------|
| Time Limit | 1000 ms |
| Memory Limit | 256 MB |
| Languages | Python only |
| IO Mode | Standard IO |
| Special Judge | No |

## Problem Template

### Required Fields
- **Display ID**: Short identifier (e.g., `BloodType001`)
- **Title**: Problem name
- **Description**: Problem statement
- **Input Description**: Input format explanation
- **Output Description**: Output format explanation
- **Sample Input/Output**: At least 2 sample

## Input/Output Format
- Multiple lines per test case
- Example:
  ```
  # Input (1.in)
  1
  2
  
  # Output (1.out)
  3
  ```

## Workflow

1. Create test case files (`N.in`, `N.out`)
2. Verify files are not empty
3. Create flat ZIP from test case directory
4. Provide problem description with all form fields
5. User uploads ZIP and fills form manually

## Example Problem Structure

```
problem/
├── 1.in
├── 1.out
├── 2.in
├── 2.out
├── ...
└── testcases.zip (flat, contains *.in and *.out only)
```
