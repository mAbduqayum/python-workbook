# Mixed practice at chapter ends - research and plan

Research note, 2026-11-08. For the todo "end each chapter with 3-5 mixed
exercises" (`professor-review.md` item 8, grounded in `curriculum-research.md`
§3). Four passes: learning science, how other books do it, computing-education
research, and an audit of this repo. Sources at the bottom; every claim cites
one, and claims I only saw second-hand say so.

**Headline: "mixed" has to mean *choosing*, not just *combining*.** A problem
that stacks loops, lists and dicts trains plan composition, a real skill but a
different one. The interleaving benefit comes from problems whose tool the
reader must pick, so the set needs look-alike problems that need different
tools, no topic labels, and older skills returning in more than one later
chapter. Bigger "uses everything" problems still have a place, as an optional
challenge broken into named steps.

---

## 1. What the evidence says

### 1.1 Mixed means choosing

- Rohrer's definition of interleaved practice: "no 2 consecutive problems
  require the same strategy," which "forces students to choose an appropriate
  strategy for each problem on the basis of the problem itself"
  ([Rohrer et al. 2020](https://gwern.net/doc/psychology/spaced-repetition/2019-rohrer.pdf)).
- Textbook "chapter reviews, mixed reviews, or spiral reviews... often consist
  of several small blocks," which let students infer the strategy before
  reading the problem ([Rohrer & Hartwig 2023](https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-spaced-and-interleaved-mathematics-practice-rohrer-hartwig.pdf)).
  The learning-science and textbook passes found this independently.
- Rohrer & Hartwig recommend placing problems that look alike but need
  different methods side by side (their example: Law of Sines next to Law of
  Cosines). Same source.
- Novices also struggle to choose strategies on their own; they default to
  trial and error ([Ko et al. 2019](https://doi.org/10.1145/3287324.3287371)).

### 1.2 Contrast and retention need different placements

- Contrast needs adjacency. In the meta-analysis, interleaving worked for items
  in immediate succession (g = 0.73) but not for temporally spaced items
  (g = 0.22, CI crossing zero, k = 17)
  ([Brunmair & Richter 2019](https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf)).
- Retention needs gaps. Best gap ≈ 10-20% of the retention interval
  ([Dunlosky et al. 2013](https://www.whz.de/fileadmin/lehre/hochschuldidaktik/docs/dunloskiimprovingstudentlearning.pdf);
  [Cepeda et al. 2008](https://www.evullab.org/pdf/CepedaVulRohrerWixtedPashler-PS-2008.pdf),
  trivia facts, so an extrapolation for programming).
- So one end-of-chapter set gives the contrast once. Spacing needs each older
  skill to come back in several later sets - Rohrer & Taylor's "once or twice
  in each of the next dozen or so assignments" (`curriculum-research.md` §3).

### 1.3 Dose

- "At least a third of practice problems should be interleaved"
  ([Hartwig & Rohrer 2021](https://zenodo.org/record/4676278/files/HartwigRohrerB.pdf?download=1));
  the best groups had "at least two-thirds... spaced or interleaved," though
  "there is no magic proportion" (Rohrer & Hartwig 2023).
- Nine sets of 4-5 come to about 40 items, roughly 15% of the book. Rohrer's
  own intervention *rearranges* existing problems rather than adding new ones,
  so moving exercises (§3.2) is the cheaper route to a higher share.

### 1.4 Size and limits

- Meta-analysis: g = 0.42 overall, g = 0.34 for math, g = −0.39 for words,
  I² = 77% (Brunmair & Richter 2019). Corroborated in direction by
  [Firth et al. 2021](https://strathprints.strath.ac.uk/75711) (g up to 0.65).
- Classroom headline: 54 classes, a month later, 61% (interleaved) vs 38%
  (blocked), d = 0.83 (Rohrer et al. 2020). The large effects all come from one
  lab.
- Independent full-year trial in Nigeria: +0.29 SD on short-term tests, 0.04 SD
  (not significant) on the end-of-year test, and top students did worse
  ([van der Haar et al. 2023](https://edworkingpapers.com/sites/default/files/ai23-876.pdf)).
- Blocked practice comes first in nearly all of Rohrer's studies, and feedback
  "might be a necessary ingredient" (Rohrer et al. 2020). The chapter bodies
  already supply the blocked phase.
- Students will rate mixed sets harder and less effective: 65% preferred
  blocked, 63% called interleaved harder
  ([Hartwig & Rohrer 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12383065/)).

### 1.5 Programming evidence is thin

- No controlled study of blocked vs interleaved problem order in introductory
  programming was found (learning-science and CS-education passes both
  searched SIGCSE, ITiCSE, ICER, Koli Calling, TOCE and CSE).
- Spacing and testing have some CS support:
  [YeckehZaare & Resnick 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12141441/)
  (randomized, Python CS1, rewarding practice days: 85.3% vs 81.7% exam);
  [Smith et al. 2023](https://zilles.cs.illinois.edu/papers/frequent_testing_sigcse23.pdf)
  (non-randomized, frequent testing).
- [Lionelle et al. 2022](https://par.nsf.gov/biblio/10352318) bundled spacing
  and interleaving into a CS1 redesign; interleaving's share can't be
  separated.
- **Using interleaving here is an extrapolation from math.**

### 1.6 Composition is its own skill

- Composing plans is harder for novices than decomposing or coding familiar
  subtasks ([Spohrer, Soloway & Pope 1985](https://doi.org/10.1207/s15327051hci0102_4);
  restated by [Rivera, Krishnamurthi & Fisler 2024](https://doi.org/10.1145/3626252.3630901)).
  Merging several plans into one loop is the hardest case.
- Rainfall results depend on context: 186 of 218 HtDP students mostly correct
  ([Fisler 2014](https://doi.org/10.1145/2632320.2632346), figure via
  [Castro & Fisler 2017](https://franciscastro.github.io/pdf/prepub-icer-2017.pdf));
  "at least about half" in three CS1 courses, with missing-input handling the
  main bug ([Seppälä et al. 2015](https://doi.org/10.1145/2828959.2828963),
  abstract only).
- Compound problems hide fragile knowledge: students who know most of the
  material can still fail the whole
  ([Luxton-Reilly & Petersen 2017](https://doi.org/10.1145/3013499.3013500)).
  Small concept questions predicted the matching integrative one
  ([Zingaro et al. 2012](https://doi.org/10.1145/2157136.2157215)).
- Blank-page writing "often do[es] not expose students to the intended
  patterns"; faded Parsons problems taught patterns better and transferred to
  writing as well as writing practice did
  ([Weinman et al. 2021](https://acelab.berkeley.edu/wp-content/papercite-data/pdf/parsons-chi2021.pdf)).
- One standalone theme beats a dependent chain: many small programs cut
  anxiety and raised coding scores by 20 points in one CS1 section
  ([Allen et al. 2018](https://doi.org/10.18260/1-2--31231)); story context
  doesn't change performance
  ([Lovellette et al. 2024](https://doi.org/10.1145/3643864)). No comparative
  study of a running project was found.

---

## 2. What other books do

| Source | Format | Placement | Labeled? |
|---|---|---|---|
| Saxon Math | 25-30 Mixed Practice problems after every lesson | every lesson | lesson number under each |
| Rohrer & Hartwig | ≥ 2/3 spaced or interleaved | every assignment | no - choosing is the point |
| AoPS / Stewart | Review problems, then a harder Challenge / Problems Plus tier | chapter end | no |
| Stroustrup PPP3 | Drill (one program modified step by step), then Exercises | chapter end | no |
| CS50P | Problem Set 5 reimplements earlier problems, adding raised errors and tests | week 5 | by origin |
| MOOC.fi | Capstone as a part's last exercise; `_2` chains across parts | part end; spread | by name |
| HtDP 2e | Graphical editor revisited at 5.10, 10.4, 32.4 | spread | cross-reference |
| Python Crash Course | "Wrap your code from Exercise 10-6 in a while loop" | after sections | by number |
| Exercism | Concept exercises unlock practice exercises | unlock graph | yes (`prerequisites`) |

Sources: [Saxon scope](https://g.christianbook.com/ns/pdf/more/17001.pdf),
[Stewart 9e](https://demo.webassign.net/features/textbooks/scalc9/details.html),
[PPP3 Ch 0](https://www.stroustrup.com/PPP3_Ch0.pdf),
[CS50P PS5](https://cs50.harvard.edu/python/psets/5/),
[MOOC.fi Part 4](https://programming-25.mooc.fi/part-4/6-strings-and-lists),
[HtDP 2e](https://htdp.org/2023-8-14/Book/index.html),
[PCC 3e Ch 10](https://ehmatthes.github.io/pcc_3e/solutions/chapter_10/),
[Exercism docs](https://raw.githubusercontent.com/exercism/docs/main/building/tracks/practice-exercises/README.md).
AoPS star markings and the text of MOOC.fi's `course_grading` exercises were not
verified.

Patterns worth borrowing: short mixed items over one big problem (Saxon,
Rohrer); revisit an earlier exercise and add the new chapter's concern
(CS50P); a routine tier plus an optional challenge tier (AoPS, Stewart,
Stroustrup).

---

## 3. What the repo shows

Audit of `*/_docs`, `index.toml`, all 223 solutions, `scripts/` and pw-book.

### 3.1 Skills that vanish

Checked by grep on 2026-11-08:

- No solution after Chapter 3 uses a `:.Nf` format spec, `input()` or `try`.
  Width, thousands, percent and fill specs are never used at all.
- `match` appears in 3 solutions (`month_days`, `next_day`, `lists/precedence`).
- `random` is used only in Repetitions and Lists; `math` not after Functions;
  `divmod`, `ceil`, `floor` never; `ord`/`chr` not after Functions.
- `break` appears in Repetitions and `files/head` only; `continue` only in
  `sets/isogram`.
- Error Handling has **no exercises** (`errors/` holds only `_docs`), so
  `try`, `raise` and `assert` are never practiced. No test uses
  `pytest.raises`.
- Memoization (`recursions/_docs/memoization.md`) is never practiced;
  `fibonacci` is plain double recursion.

### 3.2 Exercises that could move (redistribution)

- Conditionals equality lookups → Lists or Dicts: `month_from_int`,
  `student_year_level`, `name_shape`, `letter_grade_points`, `faces_money`,
  `tajikistan_holidays`.
- Conditionals range ladders → Lists (a table of `(bound, label)` pairs):
  `http_errors`, `life_phases`, `richter_scale`, `visible_light`, `h2o_phases`,
  `frequency_name`, `sound_levels`, `angle_type`.
- Cost: moving anything but a chapter's last exercise renumbers the rest, and
  `pw-book/content/preface.md` hardcodes "Exercise 2.14" and "Exercise 1.3".
  Several are back-link targets (`even_odd`, `leap_year`, `valid_triangle`,
  `quadratic_roots`, `fizz_buzz`).

### 3.3 Constraints on new exercises

- Chapters 1-3 are program-style (stdin/stdout, `tests/run_script.py`);
  Chapters 4-10 are function-style with `Call | Returns` tables.
- `scripts/check_order.py` warns (doesn't fail) when a solution uses an
  `index.toml` term before its first teaching page. Blind spots: terms missing
  from the index (`any`, `startswith`, `rstrip`, the `string` module...) and
  keyword arguments like `key=`.
- `scripts/check_examples.py` runs every exercise's examples and fails on any
  mismatch; examples whose solution imports `random` go unchecked.
- In print, `###` groups under Practice Questions are flattened and their
  headings don't print (`manifest.py`). Mixed exercises go among the existing
  Practice Questions in order of difficulty, with no heading of their own
  (decided 2026-11-08).

---

## 4. The plan

### 4.1 Shape of each set

One set at the end of each chapter from Conditionals to Recursion (Introduction
has nothing earlier to mix). Four core items and one optional challenge:

1. **A look-alike pair** (2 items, adjacent). Same surface, different tool:
   one needs this chapter's new tool, the other an older one. For example, at
   the end of Dictionaries, "how many *different* words?" (set) next to "how
   many times does *each* word appear?" (dict). (§1.1, §1.2)
2. **A spaced revisit** (1 item). An older skill the schedule in §4.3 says is
   due. (§1.2)
3. **A revisit with a twist** (1 item). An earlier exercise, linked by title as
   the 27 repeats already are, plus this chapter's concern: at the end of
   Error Handling, an earlier function now raises `ValueError` on bad input;
   at the end of Files, it reads its input from a file. (CS50P, §2)
4. **Optional challenge** (1 item). A larger problem as a ladder of named
   steps, each with the data it passes on named in the statement, ending in a
   combined function. This is where problems like Electricity Bill, Card
   Number Check, Tic-Tac-Toe Winner, Word Index and Grade Book go. (§1.6)

### 4.2 Rules

- Order the set so no two adjacent items need the same main tool (§1.1).
- No skill or chapter labels on the items. A back-link names the earlier
  *exercise*, not the tool to use (§1.1; untested, inferred from the
  mechanism).
- Core items at the difficulty of the chapter's core exercises; the hard part
  is choosing the tool (§1.4).
- Each step of the challenge is self-contained with its own tests. Reusing
  the reader's own earlier code, such as copying `is_leap_year`, is welcome
  (author's call, 2026-11-08, overriding §1.6).
- Use only skills taught by the end of the chapter, checked against
  `index.toml` and by hand for its blind spots (§3.3).
- Solutions follow the existing rules: explicit loops, no hint blocks; a
  truly needed hint goes in `<name>_hint.md`.

### 4.3 Revisit schedule

Each older skill returns in at least two later sets:

| Skill (first taught) | Returns at the end of |
|---|---|
| Format specs: width, `:,`, `%` (Intro) | Conditionals, Lists, Files |
| `math.ceil`, `divmod` (Intro) | Conditionals, Functions |
| `match` (Conditionals) | Repetitions, Functions, Dicts |
| `ord`/`chr` (Conditionals) | Functions, Dicts |
| Sentinel loop and `break` (Repetitions) | Functions, Errors |
| `random` (Repetitions) | Sets, Dicts |
| Digit stripping `% 10`, `// 10` (Repetitions) | Lists, Sets, Recursion |
| Tuples (Lists) | Dicts, Files |
| Sets (Sets) | Dicts, Files, Recursion |
| Dicts (Dicts) | Errors, Files, Recursion (a memo dict) |
| `try`/`raise` (Errors) | Files, Recursion |

### 4.4 Pilot: Lists

Lists was the pilot for the chapter framing, so pilot here too. In print order:

1. **Month Name.** `month_name(n: int) -> str`. Links back to Month From
   Integer: "You wrote this as a program with one branch per month; now make
   it a function with no `if`." (Look-alike pair, first half: lookup.)
2. **Quiet Hours.** `is_quiet(hour: int) -> bool`, true from 22 through 6.
   Same "number in, answer out" surface, but it's a range test with a
   wraparound. (Second half: comparisons.)
3. **Digit Counts.** `digit_counts(n: int) -> list[int]`, how often each digit
   0-9 appears; `0` gives a 1 in the first slot. Digit stripping into a
   counter list, or `str()` and `.count()`. (Spaced revisit: Repetitions.)
4. **Receipt Lines.** `receipt_lines(items: list[tuple[str, float]]) ->
   list[str]`: each name left-aligned, each price right-aligned to two
   decimals, then a total line. (Revisit: format specs, unused since
   Chapter 3, and tuples.)
5. **Tic-Tac-Toe Winner** (optional). (a) `line_winner(cells)` for three
   cells; (b) `board_lines(board)` returns the 8 lines; (c) `winner(board)`
   combines them.

Each gets `<name>.md`, a loop-based `<name>.py` and `test_<name>.py`, listed
at the end of `lists/_docs/_table_of_contents.md`.

Superseded 2026-11-08: the author picked 13 exercises from a 55-item candidate
list instead of this pilot. Tic-Tac-Toe Winner was written, then dropped, so
Lists has none.

### 4.5 Considered and not chosen

- **One running project through every chapter** (MOOC.fi's grading thread,
  Deitel's DS Intro): no comparative evidence, and a missed step blocks the
  next (§1.6). A shared theme with standalone items keeps the benefit.
- **3-5 bigger combined problems per chapter** (the first draft): trains
  composition but not choice, and hides fragile knowledge (§1.1, §1.6). Kept
  as the optional challenge.
- **A separate planning notation**: failed with novices, who "didn't like
  having two artifacts" (Rivera et al. 2024).

---

## 5. Open decisions

1. ~~**Printed heading.**~~ Decided 2026-11-08: no heading at all, not even an
   unprinted `###` group; mixed exercises join the end of the list.
2. **Dose.** Accept about 15% now, or also move some Conditionals lookups and
   ladders into later sets to approach a third (renumbering)?
3. **Non-writing formats.** Find-the-bug items fit the existing tests (the
   buggy code is printed; the reader's fix is tested). Parsons problems could
   live in `<name>_hint.md`. Trace and explain-in-English items need an answer
   key the book doesn't have. Add any of these after the pilot?

Out of scope here, noted for later: Error Handling has no exercises of its
own; `key=` is used in `dicts/most_frequent_char` and `files/find_longest_word`
but never taught; and `scripts/check_examples.py` currently fails on three doc
examples (`dicts/_docs/dict_operations.md:182`,
`intro/_docs/math_functions.md:49`,
`intro/_docs/string_formatting_advanced.md:13`).

---

## Sources

**Learning science**
- [Brunmair & Richter, Similarity matters](https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf) — independent meta-analysis, 2019
- [Rohrer, Dedrick, Hartwig & Cheung, classroom RCT](https://gwern.net/doc/psychology/spaced-repetition/2019-rohrer.pdf) — primary, 2020
- [Rohrer & Hartwig, Spaced and Interleaved Mathematics Practice](https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-spaced-and-interleaved-mathematics-practice-rohrer-hartwig.pdf) — primary (same lab), 2023
- [Hartwig & Rohrer, Interleaved Practice Improves Mathematics Learning](https://zenodo.org/record/4676278/files/HartwigRohrerB.pdf?download=1) — primary (same lab), 2021
- [Hartwig & Rohrer, student perceptions](https://pmc.ncbi.nlm.nih.gov/articles/PMC12383065/) — primary, 2025
- [van der Haar et al., Nigeria full-year trial](https://edworkingpapers.com/sites/default/files/ai23-876.pdf) — primary, independent, 2023
- [Dunlosky et al.](https://www.whz.de/fileadmin/lehre/hochschuldidaktik/docs/dunloskiimprovingstudentlearning.pdf) — independent review, 2013
- [Cepeda et al., temporal ridgeline](https://www.evullab.org/pdf/CepedaVulRohrerWixtedPashler-PS-2008.pdf) — primary, 2008
- [Firth, Rivers & Boyle](https://strathprints.strath.ac.uk/75711) — independent systematic review, 2021

**Programming and CS education**
- [YeckehZaare & Resnick](https://pmc.ncbi.nlm.nih.gov/articles/PMC12141441/) — primary, 2025
- [Smith et al., testing frequency](https://zilles.cs.illinois.edu/papers/frequent_testing_sigcse23.pdf) — primary, 2023
- [Lionelle et al., Spiral CS1](https://par.nsf.gov/biblio/10352318) — primary, 2022, abstract only
- [Spohrer, Soloway & Pope, goal/plan analysis](https://doi.org/10.1207/s15327051hci0102_4) — primary, 1985
- [Fisler, The Recurring Rainfall Problem](https://doi.org/10.1145/2632320.2632346) — primary, 2014
- [Seppälä et al., Do we know how difficult the rainfall problem is?](https://doi.org/10.1145/2828959.2828963) — independent, 2015
- [Castro & Fisler, Sometimes, Rainfall Accumulates](https://franciscastro.github.io/pdf/prepub-icer-2017.pdf) — primary, 2017
- [Rivera, Krishnamurthi & Fisler, program planning notations](https://doi.org/10.1145/3626252.3630901) — primary, 2024
- [Weinman, Fox & Hearst, Faded Parsons Problems](https://acelab.berkeley.edu/wp-content/papercite-data/pdf/parsons-chi2021.pdf) — primary, 2021
- [Luxton-Reilly & Petersen, compound assessments](https://doi.org/10.1145/3013499.3013500) — independent, 2017
- [Zingaro, Petersen & Craig, integrative CS1 questions](https://doi.org/10.1145/2157136.2157215) — primary, 2012
- [Ko et al., explicit programming strategies](https://doi.org/10.1145/3287324.3287371) — primary, 2019
- [Allen et al., many small programs](https://doi.org/10.18260/1-2--31231) — primary, 2018
- [Lovellette, Bouvier & Matta, problem description effect](https://doi.org/10.1145/3643864) — independent, 2024

**Books and courses**
- [Saxon Math scope and sequence](https://g.christianbook.com/ns/pdf/more/17001.pdf) — primary, 2006-07
- [Stewart Calculus 9e contents](https://demo.webassign.net/features/textbooks/scalc9/details.html) — primary, current
- [Stroustrup, PPP3 Ch 0](https://www.stroustrup.com/PPP3_Ch0.pdf) — primary, 2024
- [CS50P Problem Set 5](https://cs50.harvard.edu/python/psets/5/) — primary, current
- [MOOC.fi Python 2025, Part 4](https://programming-25.mooc.fi/part-4/6-strings-and-lists) — primary, 2025
- [HtDP 2e contents](https://htdp.org/2023-8-14/Book/index.html) — primary, 2023
- [Python Crash Course 3e, Ch 10 solutions](https://ehmatthes.github.io/pcc_3e/solutions/chapter_10/) — primary (author's site), 2023
- [Exercism practice-exercise docs](https://raw.githubusercontent.com/exercism/docs/main/building/tracks/practice-exercises/README.md) — primary, current
