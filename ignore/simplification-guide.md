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

**The harness is not uniform across chapters — check the test before you
reason about it.** Some chapters (e.g. `repetitions`) don't use the exact-match
`_clean_output` path at all. They use the `ScriptRunner` fixture directly with
**loose substring assertions** (`assert expected in result.stdout`), often
asserting only the *value* (`"1010"`, `"4"`), not the surrounding label. Where
that's the style: dropping a label prefix or reformatting output is safe as
long as the asserted substring still appears, and you can confirm it in seconds
by grepping the parametrize block.

Implication: removing `Enter …:` prompts from docs/solutions is safe. Tests
assert program output, not doc text — **doc-only edits never need test
changes**. Still run the suite to confirm nothing else regressed.

## Step 1 — Drop `Enter …:` input prompt boilerplate

In each exercise `.md`, every `**Example N:**` has an input fenced block then
an output fenced block. Strip the `Enter <label>: ` prefix from each **input**
line, leaving the bare value. Leave the output block untouched. Mirror the
change in the solution `.py`: `input("Enter foo: ")` → `input()`.

**DROP the prompt** for almost everything, including **fixed multi-input of
different kinds** (start / diff / count, weight / height, the coefficients
a / b / c). A `## Task` that names the inputs in the order they're read is
enough to disambiguate the example's input block — the prompt is redundant
with it. Drop it.

**KEEP the `Enter …:` prompt only when** reads are **interleaved inside a loop**
so there is no fixed order to name up front, and the prompt is the only thing
telling the reader which value is being asked for at each step — e.g. reading
alternating x / y coordinate pairs until the user enters a blank x
(`polygon_perimeter`). Here a bare input block really is ambiguous.

Also soften `## Task` wording: "Ask/prompt the user for X" → "Read X".

The first one or two exercises in a chapter that *introduce* `input()` as the
concept may keep an explicit prompt on purpose — prompting is taught once
before being dropped.

**Measurement inputs need a unit somewhere.** Once a prompt is dropped, the
example input becomes a bare number — `5.2` in `circle_area` doesn't say
"meters". Put the unit in the **intro paragraph** ("calculates the area of a
circle given its radius in meters"). This holds even when the program doesn't
print the unit in its output.

## Step 2 — Drop how-to-solve notes; keep output/spec notes

A `## Note` (or inline hint) is **redundant and should be removed** when it:
- restates formatting already visible in the examples
  (`Use .2f formatting`, leading zeros — the example output shows it), or
- prescribes *which function/builtin* to use
  (`Use math.sqrt()`, `Use min()/max()`, `Use // and %`,
  `Convert with math.radians()`) — that is the puzzle, not the spec, or
- **paraphrases another section of the same doc** — the Task, Algorithm,
  Logic, Formula, Diagram, or a thresholds Table. If the bullet just says
  in prose what an earlier section already says structurally, drop it.

**KEEP a note (or the specific bullet) only when it states a fact the reader
cannot derive and that determines the expected output:**
- given physical constants not in the formula
  (water specific heat `4.186`, `1 kWh = 3,600,000 J`),
- required unit conversions that are part of the spec
  (`K = °C + 273.15`, second/hour/day conversion factors),
- output grammar/format conventions the examples don't fully pin
  (e.g. `year(s)` / `second(s)` pluralization),
- `math.pi` *only* when it's needed to reproduce the rounded output and the
  formula references π,
- edge-case behaviour the Task and examples don't make explicit
  (case-insensitive input, boundary values, non-strict ordering).

When a Note mixes both, delete only the how-to/redundant bullets and keep
the spec ones. Preserve any non-Note structural section even if it sits
right after (e.g. `## Operations Explained` defines the task — keep it).

### Step 2b — Prefer one section over two

The default shape of a simplified exercise is **Task → Examples**, nothing
else. For trivial problems it goes one step further to just
**intro paragraph → Examples** (drop `## Task` entirely). Use that minimal
shape when the title + intro + examples already convey input, output
strings, and the rule — that is, when every `## Task` bullet would just
restate "Read X / determine Y / display Z" without adding new spec.

If a `## Note`, `## Logic`, or `## Algorithm` section survives Step 2,
ask one more question: *does this content belong in `## Task`?*

- A bullet that is genuinely-necessary spec (e.g. "voting age is 18",
  "input is case-insensitive", "0°C displays `solid or liquid`") should
  be **moved into `## Task` — or directly into the intro paragraph** if
  it's a single short fact. Then drop the now-empty Note.
- A `## Logic` / `## Algorithm` / `## Pattern` section that walks the student
  through the branches, the digit extraction, or a term-by-term derivation of
  the answer *is* the solution — drop it wholesale.
- Keep a standalone reference section only when it is genuinely
  declarative content the student looks up rather than derives — a
  thresholds table (BMI ranges, day-mapping table), a labeled formula,
  or a diagram. Tables/formulas/diagrams stay; prose how-to goes.
- **A named method the student cannot be expected to derive (Newton's method,
  a series for π) keeps its core formula, not just its tolerance.** Dropping
  the update rule (`guess = (guess + x/guess) / 2`) along with the walkthrough
  leaves the exercise unsolvable — that's too far. Keep the one labeled formula
  / series; drop the surrounding "do this, then this" steps. (Naming the method
  in the title isn't enough for a beginner.)

One scoped exception: chapters introducing a new feature (e.g.
`if_elif_else` teaching docs in `_docs/`) intentionally keep more
explanation — leave those alone.

### Step 2c — Drop label prefixes in one-line outputs

When the program's output is a **single line** of the form
`Label: <value>` (or `Label: <value> <unit>`), and the surrounding context
(intro + the value alone) already tells the reader what the value is,
**drop the label prefix** from solution, test, and doc together. Examples:

- `print(f"Sorted order: {a}, {b}, {c}")` → `print(f"{a}, {b}, {c}")`
- `print(f"The area is: {area:.2f}")` → `print(f"{area:.2f}")`
- `print(f"Total seconds: {n}")` → `print(f"{n}")`

**Keep the label** when:
- the output is **multi-line** and labels disambiguate which line is which
  (Fahrenheit / Kelvin, Energy / Cost, Tip / Total), or
- the label carries **dynamic information** that wouldn't otherwise appear
  (`Balance after {years} years: …`), or
- dropping the label would leave the value ambiguous (no unit anywhere and
  the intro doesn't pin it).

Prefer **value + unit suffix** (`{feet:.2f} feet`) over **label prefix**
(`Distance in feet: {feet:.2f}`) when a single-line output needs a unit —
the unit reads naturally with the number, and there's no leading boilerplate.

Remember: this change touches **three files** (`.py`, `test_*.py`, `.md`).
Sync them in one pass.

### Step 2d — Don't suggest formulas for grade-school math

`## Formula` is genuinely useful for physics, finance, or trigonometry the
student can't be expected to derive. It is **not** useful for unit
conversions that are elementary arithmetic — drop it for things like:

- seconds ↔ minutes/hours/days,
- millimetres ↔ metres,
- digit extraction with `//` and `%` on a two-digit number.

If a beginner has to be told `total_seconds = days×86400 + hours×3600 +
minutes×60 + seconds`, the exercise is teaching the wrong thing.

### Step 2e — Delete `<details>` Hint/Note blocks; use a `*_hint.md` if truly needed

`<details>` Hint and Note blocks inside an exercise doc paste a complete or
near-complete solution, defeating the guide's goal (*what* to produce, never
*how*). **Delete them all.** First fold any spec-critical fact they contain
into `## Task` (Step 2b) so nothing non-derivable is lost.

Only when a hint is **really necessary** — a named technique a beginner cannot
be expected to derive, and where the obvious brute-force bypasses the concept
the exercise teaches (sliding window, complement search, sorted-key grouping) —
create a **standalone `<exercise>_hint.md`** next to the exercise, modeled on
`intro/sort_integers/sort_integers_hint.md`:

- `# <Title> - Hint` heading,
- terse `## Algorithm` bullets describing the approach in words,
- an optional one-line `## Note`,
- **no full solution code**, and
- **not linked** from the exercise doc — the student opens it deliberately.

Keep the bar high: if the technique is taught in `_docs/`, or the needed
mapping/tool is already handed to the student in the template, no hint file is
warranted.

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

## Function questions

Conventions for exercises where the student writes a function (lists,
functions, … chapters), on top of the steps above. A change here touches
**three files** — `.md` template/examples, solution `.py` `__main__` block,
`test_*.py` cases — sync them in one pass.

- **Sample list values: primes, not `[1, 2, 3, 4, 5]`.** Use
  `[2, 3, 5, 7, 11]` (extend with 13, 17, …); same for string forms
  (`"1 2 3 4 5"` → `"2 3 5 7 11"`). With consecutive ints starting at 1,
  value and index+1 coincide, so an example can't show whether a result is
  an index or a value. Recompute every expected output — sums, averages,
  found-indices, matrix rows all change with the data.
- **Generic list parameter: `l`, not `lst`.** Keep semantic names
  (`items`, `numbers`, `results`) where they exist. (`E` rules are ignored
  in this repo's ruff config, so E741 won't fire on `l`.)
- **Notes state behavior, not the computation.** Step 2's how-to test applies
  to function questions too, but the giveaway looks different: instead of
  input prompts it's an index expression, formula, or builtin name hiding in
  an edge-case bullet. Say *which result* the function returns ("for
  even-length lists, return the second of the two middle items"), never the
  expression or tool that produces it (`len // 2`, "create the list from
  `range`", "slicing handles this naturally"). Assumptions ("list is not
  empty") and *constraints* ("don't use `sum`") are spec — they stay.
  Delete any `<details>` Hint/Note blocks (Step 2e); promote a truly-needed
  hint to a standalone `*_hint.md`.

## Step 4 — Verify

1. `uv run pytest <chapter> -n auto -q` — expect 100%. (Sandbox note: the `uv`
   cache lives outside the sandbox; run with sandbox disabled if you hit a
   read-only-filesystem lock error.)
2. Spot-check 2–3 rewritten docs: bare input values, untouched output blocks,
   kept spec notes intact, no orphaned headings or missing blank lines.
3. Confirm the chapter's input-introducing exercise(s) still show prompts.

## Checklist per chapter

- [ ] Drop `Enter …:` from docs **and** solution `.py` everywhere except
      interleaved-loop reads (Step 1).
- [ ] Soften `## Task` "ask/prompt" → "read".
- [ ] Remove redundant/how-to notes; keep non-derivable output-spec notes.
- [ ] Delete all `<details>` Hint/Note blocks; promote a truly-needed hint to a
      standalone `<exercise>_hint.md` (Step 2e).
- [ ] Fold any surviving spec bullets into `## Task`; drop standalone
      `## Logic` / `## Algorithm` walkthroughs; default shape is
      `Task → Examples` (plus a thresholds table / formula / diagram
      when declarative).
- [ ] Add input-unit hints to measurement-exercise intros when prompts were
      dropped (Step 1).
- [ ] Drop redundant `Label:` prefixes from single-line outputs; prefer
      `value + unit suffix` when a unit is needed.
- [ ] Drop `## Formula` for grade-school arithmetic conversions.
- [ ] Sync any grammar/format fix across solution + test + doc examples.
- [ ] Function questions: prime sample values (`[2, 3, 5, 7, 11]`), expected
      outputs recomputed; `lst` → `l`, semantic names kept; notes state
      behavior, not the computing expression/builtin.
- [ ] `pytest <chapter>` green; spot-check docs render cleanly.
