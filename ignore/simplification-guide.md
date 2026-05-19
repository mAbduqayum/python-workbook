# Exercise Simplification Guide

How to simplify exercise docs/solutions in a chapter the same way the `intro`
chapter was done. The goal: beginners write the *concept being taught*, not
boilerplate, and docs say *what* to produce — never *how* to solve it.

## How the test harness works (read this first)

`conftest.py` `_clean_output()` runs
`re.sub(r"Enter [^:]+:\s*", "", stdout.strip())` before comparing output.

- `run_and_check_output_only` (used by ~all exercises): bare `input()` **and**
  `input("Enter X: ")` both pass — the `Enter …:` prompt is stripped.
- `run_and_check` (strict, only `hello_world`): takes no input, unaffected.
- Any prompt wording *other than* `Enter <label>:` is **not** stripped and
  will fail the output comparison.

Implication: removing `Enter …:` prompts from docs/solutions is safe. Tests
assert program output, not doc text — **doc-only edits never need test
changes**. Still run the suite to confirm nothing else regressed.

## Step 1 — Drop `Enter …:` input prompt boilerplate

In each exercise `.md`, every `**Example N:**` has an input fenced block then
an output fenced block. Strip the `Enter <label>: ` prefix from each **input**
line, leaving the bare value. Leave the output block untouched. Mirror the
change in the solution `.py`: `input("Enter foo: ")` → `input()`.

**KEEP the `Enter …:` prompt when** the exercise reads **multiple inputs of
different kinds**, where the prompt is the only thing telling the reader which
value goes on which line (e.g. deposit / rate / years). Without it the input
block is ambiguous.

**DROP the prompt when** input is:
- a single value, or
- multiple values of the **same category** (e.g. three numbers to average,
  three sides of a triangle, a list to sort) — order/meaning is obvious.

Also soften `## Task` wording: "Ask/prompt the user for X" → "Read X".

The first one or two exercises in a chapter that *introduce* `input()` as the
concept may keep an explicit prompt on purpose — prompting is taught once
before being dropped.

## Step 2 — Drop how-to-solve notes; keep output/spec notes

A `## Note` (or inline hint) is **redundant and should be removed** when it:
- restates formatting already visible in the examples
  (`Use .2f formatting`, leading zeros — the example output shows it), or
- prescribes *which function/builtin* to use
  (`Use math.sqrt()`, `Use min()/max()`, `Use // and %`,
  `Convert with math.radians()`) — that is the puzzle, not the spec.

**KEEP a note (or the specific bullet) only when it states a fact the reader
cannot derive and that determines the expected output:**
- given physical constants not in the formula
  (water specific heat `4.186`, `1 kWh = 3,600,000 J`),
- required unit conversions that are part of the spec
  (`K = °C + 273.15`, second/hour/day conversion factors),
- output grammar/format conventions the examples don't fully pin
  (e.g. `year(s)` / `second(s)` pluralization),
- `math.pi` *only* when it's needed to reproduce the rounded output and the
  formula references π.

When a Note mixes both, delete only the how-to bullets and keep the spec ones.
Preserve any non-Note section even if it sits right after (e.g.
`## Operations Explained` defines the task — keep it).

Dedicated separate `*_hint.md` files are deliberate opt-in scaffolding — leave
them alone; this guide only targets inline giveaways in the exercise `.md`.

## Step 3 — General beginner-friction cleanup

Apply opportunistically while in a chapter:
- Fix broken/placeholder commands and paths in `_docs/` (use real project
  paths, `uv run`, correct menu names).
- Make constants explicit and idiomatic in solutions (`import math; math.pi`
  instead of a hardcoded `pi = 3.14159`) **only if** the rounded example
  output is unchanged — verify before/after.
- Grammar/formatting polish: `second(s)`/`year(s)`, leading zeros — update the
  solution, its test's expected strings, **and** all example outputs in the
  `.md` together so they stay in sync.

## Step 4 — Verify

1. `uv run pytest <chapter> -n auto -q` — expect 100%. (Sandbox note: the `uv`
   cache lives outside the sandbox; run with sandbox disabled if you hit a
   read-only-filesystem lock error.)
2. Spot-check 2–3 rewritten docs: bare input values, untouched output blocks,
   kept spec notes intact, no orphaned headings or missing blank lines.
3. Confirm the chapter's input-introducing exercise(s) still show prompts.

## Checklist per chapter

- [ ] Classify each input exercise: single / same-category → drop prompt;
      mixed-kind → keep prompt.
- [ ] Strip `Enter …:` from docs **and** solution `.py` for the drop set.
- [ ] Soften `## Task` "ask/prompt" → "read".
- [ ] Remove redundant/how-to notes; keep non-derivable output-spec notes.
- [ ] Sync any grammar/format fix across solution + test + doc examples.
- [ ] `pytest <chapter>` green; spot-check docs render cleanly.
