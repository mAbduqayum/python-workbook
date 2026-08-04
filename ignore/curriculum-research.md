# How other Python courses are structured — and where this one stands

Research note, 2026-07-29. Compares this workbook against eight established
Python curricula and against the published research on exercise design.
Sources at the bottom; every claim below cites one.

**Headline: the topic *order* is mainstream and needs no defence. The gaps are
in what surrounds each exercise, not in the sequence of chapters.** Every one of
the 222 exercises is a blank-page write-from-scratch problem, and three
independent research traditions say the first item in a topic should not be.

---

## 1. Topic order — already in line with the field

Our order: intro → conditionals → repetitions → functions → lists → sets →
dicts → errors → files → recursions.

| Decision | Field | Us |
|---|---|---|
| Functions **after** loops | 5 of 8 (MIT ×2, MOOC.fi, Automate 3e, Python Tutorial); 3 before (CS50P, Think Python, Real Python) | after — majority side |
| Functions **before** lists | **8 of 8. No exception.** | before ✓ |
| Files **after** data structures | 7 of 8 (only py4e inverts, deliberately) | after ✓ |
| Recursion **late or absent** | absent in py4e, Automate, Python Tutorial; "leftovers" week in CS50P; part 11/14 in MOOC.fi | last — and 16 exercises is generous by field standards |

No source in the study argues its functions placement explicitly; the split is
real and unresolved, so ours is not a weak spot. Leave the sequence alone.

**One genuine oddity: sets get position 6, ahead of dicts.** Sets are the
weakest "core" data structure in the field — a named topic only in the Python
Tutorial (5.4), Think Python's Ch18 *Extras*, and CS50P's Week 9 *Et Cetera*,
two of which are explicitly labelled leftover chapters. Absent from py4e,
Automate, Real Python Basics, and MOOC.fi's section titles. We promote sets to a
full numbered chapter *and* give it the fewest exercises of any topic (6). The
promotion and the thinness point in opposite directions.

## 2. Missing topics, ranked by how strongly the field agrees

1. **OOP — 7 of 8 teach it.** The only omitter is Automate the Boring Stuff,
   which excludes it on record because its readers write throwaway scripts, not
   software. That rationale doesn't apply to a sophomore workbook.
   `oop-syllabus.md` exists at the repo root, is untracked, and references
   directories (`00_class_basics/01_person/`) that were never built.
2. **Errors — 6 of 8 teach it, and we already advertise it.** README step 8 of
   10 links a chapter with one doc page and **zero exercises**. Field range is
   wide (CS50P makes it Week 3; Think Python and py4e skip it entirely) — so
   either building it or dropping it from the reading order is defensible. What
   isn't defensible is promising it and delivering nothing.
3. **Modules/packages — 5–6 of 8.** We have the prose
   (`functions/_docs/import.md`, `modules.md`) and no exercises.
4. **Strings as a named topic — unanimous core.** Ours are scattered across
   `intro/_docs/string_formatting*.md` and `conditionals/_docs/string_utils.md`.
   Covered, but not a chapter.
5. **Testing — CS50P gives it a full week.** Its PS5 is the pattern worth
   stealing: every problem is "reimplement an earlier program, then write tests
   for your own code." We are already pytest-native, so this is unusually cheap.
   Students currently consume 222 test files and write none.
6. **Debugging — not a topic anywhere in the repo.** MOOC.fi treats it as a
   week-one skill (Part 1 has four "Fix the code:" exercises) and scaffolds it
   in three stages: print debugging → variable visualiser → VS Code debugger.
   Automate 3e independently promoted Debugging from Ch11 to Ch5 between
   editions. Two sources converged on this from different directions.
7. **Tuples — 7 of 8.** Three passing mentions here.

**Contested, so not a gap:** comprehensions. The Python Tutorial teaches them
early and mainstream (5.1.3); Think Python quarantines them in Ch18 *Extras*
and argues against them ("harder to debug because you can't put a print
statement inside the loop"); Automate omits them deliberately. Our single
mention is a legitimate position, not an oversight.

**Safe to keep skipping:** regex, generators, decorators, Big-O/sorting.
Decorators appear in exactly one intro curriculum (CS50P Week 8) and only as
OOP furniture. Complexity analysis is MIT-only — it's what makes MIT a CS course
rather than a Python course.

## 3. Exercise volume — the count is fine, the *blocking* is not

Per-topic counts here: conditionals 39, repetitions 35, intro 35, lists 30,
functions 27, files 20, recursions 16, dicts 14, sets 6.

Field comparison:

| Source | Per unit |
|---|---|
| CS50P | 3–6 per week (42 total) |
| Think Python 3e | 5–7 per chapter |
| Real Python | 1 exercise set per lesson, uniformly |
| Exercism authoring guidance | **"Try and choose 3 – 8 Exercises that practice each Concept"** |
| Exercism live Python track | most-practised concept (`strings`) = 12 exercises, across a 143-exercise track built over a decade |
| MOOC.fi | 12–38 per part (283 total) — the dense outlier |

MOOC.fi proves high volume can work, so 39 is not automatically wrong. But two
things differ. Its counts *ramp* (31→22→34→38→27→19→18→16→15→12), thinning as
tasks get larger; ours don't. And a MOOC.fi "part" spans several concepts —
Part 4 covers VS Code, functions, lists, iteration, formatting and strings —
whereas our 39 conditionals exercises are 39 conditionals exercises.

**The research is pointed here.** Rohrer & Taylor (2006, 216 students) compared
3 vs 9 practice problems in one session: *no* difference at one week or four
weeks. Their reading is diminishing returns — "after the initial exposure to a
concept, the first one or two practice problems might yield a large increase in
a subsequent test score. Yet each additional practice problem provides an ever
smaller gain." They audited four maths textbooks, found 75–92% of each
assignment's problems related to the immediately preceding lesson, and concluded
that structure "minimizes long-term retention." **Our topic folders are 100%
blocked — more extreme than the textbooks they criticised.**

Their fix is redistribution, not deletion: "each lesson is followed by the usual
number of practice problems, but only a few of these problems relate to the
immediately preceding lesson. Additional problems of the same type then appear
perhaps once or twice in each of the next dozen or so assignments." Their 2007
follow-up shows interleaved practice beats blocked practice on delayed retention
*even though* blocked practice feels more effective while you're doing it.

They also guard against over-reading it: the result "does not support the
extreme view that students should be assigned only one problem of each type."
And their test used problems structurally identical to the practice problems, so
transfer to novel tasks is untested.

**So: don't delete exercises. Make later topics revisit earlier ones.**

## 4. Scaffolding — the widest gap, and the best-corroborated

Measured in this repo: **0 of 222 exercises use a predict / trace / modify /
debug framing. All 86 templates are bare `pass` stubs.** Every exercise is a
blank page.

Three independent lines of evidence say the *first* item in a topic shouldn't be:

- **Faded worked examples** (Renkl & Atkinson 2003): worked example → completion
  problem → full problem beats alternating example-problem pairs, and the effect
  is strongest early in skill acquisition.
- **PRIMM** (Sentance, Waite & Kallia 2019 — 493 students, 13 schools, 8–12
  weeks, statistically significant in favour of the experimental group): Predict
  → Run → Investigate → Modify → Make, designed explicitly to counter "the known
  problem of novices writing programs before they are yet able to read them."
  Non-randomised quasi-experimental design; the authors note some teachers
  didn't fully engage with the materials.
- **Parsons problems** (Ericson et al., CHI 2021): same learning as writing the
  equivalent code, at higher efficiency; ITiCSE 2023 found them effective as
  scaffolding with equal posttest scores.

Lister's tracing work adds the sharp version: novices need high code-*reading*
accuracy before they can independently write code. The prerequisite for an
exercise is often a reading skill, not another solved exercise.

Cheapest concrete moves, in order: make the first 2–3 exercises of each topic
"predict the output" or "fix the code"; give some stubs a partially-filled body
instead of `pass`.

## 5. Internal inconsistencies worth fixing regardless

- **Two incompatible exercise formats, splitting cleanly at a topic boundary.**
  intro/conditionals/repetitions/functions (136 exercises) use `## Examples` and
  give **no template**. lists/sets/dicts/files/recursions (86) give a
  `## Template` and have **no examples**. Not one exercise has both. Exercism
  requires both — a worked example per task *and* a stub, because "the stub's
  job is to let a student know where to add code."
- **`## Task` is a coin flip**, not a convention: universal in
  repetitions/functions/dicts, but 2/35 in intro, 4/39 in conditionals, 0/20 in
  files, 0/16 in recursions.
- **166 of 222 exercises carry no difficulty signal** — and they're the ones a
  beginner meets first. Only sets/dicts/files/recursions group their lists.
  Exercism uses an explicit 1–10 integer on every practice exercise (their live
  Python distribution is heavily bottom-weighted: 121 of 143 sit at 1–4).
- **Examples duplicate the tests.** In 109 of the 135 exercises that have both
  (80%), more than half the numeric values in the `## Examples` block reappear
  in the test file. Exercism's rule is the opposite: "The tests should not use
  the examples from the `instructions.md` file" — worked example and test corpus
  deliberately disjoint, so the example teaches and the test verifies.
- ~~**`todo.md` ships to students.**~~ Fixed — moved to `ignore/todo.md`.
  `sync-main` strips only `<topic>/<exercise>/<exercise>.py` and `ignore/`, so
  the 224-line backlog — unwritten exercise drafts, notes like "make questions
  more interesting" — used to mirror to `main` verbatim. (`oop-syllabus.md`/
  `.pdf` are untracked, so they never leaked.)

## 6. The 23 alternate solutions — the research answers this directly

Open item in `.docs/issues.md` #10: 23 `*2` functions (`chars_count2`,
`two_sum2`, …) live in graded solution files with nothing marking them as
alternatives and no test touching them.

- **The technique is sound.** Rittle-Johnson & Star (70 students, randomised):
  comparing alternative solution methods produced greater procedural flexibility
  and conceptual knowledge than studying the same methods sequentially. It fed a
  US Dept. of Education Practice Guide recommendation.
- **But the moderator decides the placement.** Students *with prior domain
  knowledge* learn more from comparison than novices do. That argues for
  revealing alternatives **after** the learner has solved it once.
- **Nobody puts them in the solution file.** Exercism's reference model is a
  separate `.approaches/` directory — `introduction.md` enumerating and
  comparing them, one subdirectory per approach, snippets capped at 8 lines,
  revealed only after submission. Their `acronym` exercise documents eight
  approaches and closes with a "Which approach to use?" section comparing
  idiomaticity, complexity, measured speed and readability. Codewars and
  LeetCode both gate community solutions behind submission too.

**Recommendation: move the 23 into a per-exercise `approaches.md` (or a section
at the foot of the exercise `.md`), not the `.py`.** That resolves the item
without losing the teaching material, and matches every system surveyed.

## 7. Things we're doing right — don't "fix" these

- **Shipping tests to students is well-precedented.** MOOC.fi does exactly this
  (tests run locally via the TMC plugin and on the server), and Exercism shows
  the full test file for *practice* exercises. The field splits — CS50P inverts
  it and makes students write their own — but our side is the mainstream one.
  No controlled study comparing visible vs hidden tests on learning outcomes was
  found.
- **Withholding nothing else.** Every system withholds the reference solution;
  our `sync-main` strip does precisely that and nothing more.
- **The `infix_to_postfix` → `precedence` chain** matches Python Koans, which
  enforces prerequisites through a shared code artifact rather than metadata
  (`about_triangle_project` → `about_exceptions` → `about_triangle_project2`).
  Exercism's alternative is to declare dependencies on *concepts* and derive the
  graph, which scales better but needs a concept registry we don't have. Fine as
  is; just don't build many more of these by hand.

## 8. Suggested order of work

1. ~~`todo.md` → `ignore/todo.md`~~ — done.
2. Decide `errors/`: build exercises, or drop step 8 from the README order.
3. Move the 23 alternates out of the solution files into `approaches.md`.
4. Add difficulty groupings to the five unlabelled topics.
5. Add 2–3 predict/fix-the-code exercises at the head of each topic.
6. Start interleaving: have later topics revisit earlier concepts.
7. OOP, if the course is going there.

Declined for now (2026-08-04): converging the two exercise formats onto a single
`## Task` + `## Examples` + `## Template` shape, and de-duplicating the worked
examples from the test cases. Both are recorded in §5 above if that changes.

---

## Sources

**Curricula**
- [CS50P — Syllabus, weekly topic pages, problem sets, honesty policy](https://cs50.harvard.edu/python/) — primary, 2026 edition
- [Python Programming MOOC 2025 (Helsinki) — parts 1–14, grading](https://programming-25.mooc.fi/) — primary, 2025; exercise counts from [rage/programming-25](https://github.com/rage/programming-25)
- [MIT 6.100L — syllabus and 26-lecture calendar](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/pages/calendar/) — primary, Fall 2022 (OCW publishes 6.100L and 6.0001, not 6.100A)
- [MIT 6.0001 — syllabus](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/syllabus/) — primary, Fall 2016
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) — primary, current
- [Think Python 3e](https://allendowney.github.io/ThinkPython/) — primary, Downey
- [Automate the Boring Stuff 2e](https://automatetheboringstuff.com/2e/chapter0/) and [3e TOC](https://nostarch.com/automate-boring-stuff-python-3rd-edition) — primary
- [Real Python — learning paths](https://realpython.com/learning-paths/) — primary
- [Python for Everybody — lessons](https://www.py4e.com/lessons) — primary

**Exercise design**
- [Exercism docs — concept exercises](https://github.com/exercism/docs/blob/main/building/tracks/concept-exercises.md), [practice exercises](https://github.com/exercism/docs/blob/main/building/tracks/practice-exercises/README.md), [syllabus](https://exercism.org/docs/building/tracks/syllabus), [config.json](https://exercism.org/docs/building/tracks/config-json), [approaches](https://exercism.org/docs/building/tracks/approaches), [unlocking](https://github.com/exercism/docs/blob/main/building/product/unlocking-exercises.md) — primary
- [exercism/python — live track config and `acronym/.approaches/`](https://github.com/exercism/python) — primary
- [Rationale for v3](https://github.com/exercism/v3/blob/main/docs/rationale-for-v3.md) — primary, platform opinion
- [gregmalcolm/python_koans](https://github.com/gregmalcolm/python_koans) — primary
- [Codewars authoring docs — sample tests, description, ranks](https://docs.codewars.com/authoring/guidelines/sample-tests) — primary
- [HackerRank — test cases in coding questions](https://support.hackerrank.com/articles/3245197419-test-cases-in-coding-questions) — primary

**Research**
- [Rohrer & Taylor (2006), *Applied Cognitive Psychology* 20:1209–1224](https://files.eric.ed.gov/fulltext/ED505642.pdf) — overlearning and distributed practice
- [Rohrer & Taylor (2007), *Instructional Science* 35:481–498](http://uweb.cas.usf.edu/~drohrer/pdfs/Rohrer&Taylor2007IS.pdf) — interleaving beats blocking
- [Sentance, Waite & Kallia (2019), *Computer Science Education* 29(2–3):136–176](https://suesentance.net/wp-content/uploads/2020/02/teaching_computer_programming_with_primm__a_sociocultural_perspective_author_copy.pdf) — PRIMM
- [Lee et al. (2011), *ACM Inroads* 2(1):32–37](https://www.semanticscholar.org/paper/3a84e3e77e76795c7e93c98f28f2b9118d1b10fc) — Use-Modify-Create
- [Renkl & Atkinson (2003)](https://mrbartonmaths.com/resourcesnew/8.%20Research/Making%20the%20most%20of%20examples/Fading%20out%20and%20Prompts.pdf) — faded worked examples
- [Ericson et al. (2021), CHI '21](https://dl.acm.org/doi/fullHtml/10.1145/3411764.3445292) and [ITiCSE 2023](https://dl.acm.org/doi/10.1145/3587103.3594182) — Parsons problems
- [Rittle-Johnson & Star (2007)](https://www.semanticscholar.org/paper/1591c94ea47a603ca35cae9e01e656305931cb88) — comparing solution methods
- [Janzen & Saiedian (2006), SIGCSE '06](https://digitalcommons.calpoly.edu/csse_fac/40/) — test-driven learning

**Not found:** any controlled experiment comparing visible vs hidden tests on
learning outcomes; how LeetCode assigns difficulty; how a Codewars kyu rank is
set.
