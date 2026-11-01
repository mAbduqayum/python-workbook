# A professor's review of the workbook

Review note, 2026-11-01. It follows `curriculum-research.md` (2026-07-29) and
doesn't repeat that note's comparison of curricula. "Mistakes to fix first" and
"Teaching changes" have been acted on; the decisions are recorded at the end of
each section.

**Headline: the book is accurate, and its topic order is sound. What's missing
is teaching students to read code and to debug it, and some early exercises rely
on skills the notes haven't taught yet.**

## What was measured

| Check | Result |
|---|---|
| Tests against the reference solutions | 1,809 passed |
| Python listings in the notes, preface and appendix | 251: 195 ran clean, 4 are deliberate syntax skeletons, 2 run very long on purpose, and the rest stop on `input()` or missing files, or are fragments, or fail on purpose |
| `print(x)  # expected` comments | 131 compared; no wrong output. 11 differ only because the comment describes rather than states the output |
| Exercises that ask a student to read, trace or fix code | 0 of 222 |
| "traceback", "debugger" or "breakpoint" in the notes and book walkthrough | 0 |
| Reference solutions that use `try` | 0 of 222 |
| Files exercises that mention errors | 0 of 20 |
| Difficulty signal in the printed book | None. Four tables of contents group exercises by level, and `book/manifest.py` drops the groups |
| Later versions of a repeated exercise that mention the earlier one | 0 of 20 |

Order against solution length (Spearman, without `*2` variants or the main guard):

| Chapter | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| rho | 0.56 | 0.35 | 0.68 | 0.78 | 0.75 | **-0.09** | **0.03** | 0.90 | 0.77 |

Length is a rough stand-in for difficulty: `month_from_int` is long but easy.

Words of notes per exercise: Files 49, Repetitions 50, Conditionals 71,
Introduction 88, Recursion 110, Functions 116, Dictionaries 157, Lists 161,
Sets 240. Error Handling has 624 words and no exercises.

## Mistakes to fix first

1. **13 exercises print a prompt in the Input column**, for example `Enter
   pressure (Pascals): 20000000` in 1.34. The preface says that column is what
   you type, and the tests feed bare values. Affected: 1.3, 1.4, 1.15, 1.16,
   1.21, 1.22, 1.23, 1.26, 1.30, 1.33, 1.34, 1.35, 3.32.
2. **7.2 `most_frequent_char` requires `raise`**, which no note shows before
   Chapter 8. It's the only exercise in Chapters 1-7 that does. Change it to
   return `""` for an empty string and update its test.
3. **Two chapters open too hard.** 6.1 `set_operations` is the longest solution
   in Sets (32 lines, median 9), with five functions and rules about banned
   syntax. 7.4 `read_aloud` is the longest in Dictionaries (28 lines, median 12).
   Move both to the end of their chapters.
4. **Chapter 3 relies on things its notes never show.** `//` and `%` are taught,
   but no note in Chapters 1-3 shows the loop that strips digits with them (3.10,
   3.11). Nor do they show `str()` (3.23), indexing a string (the reference
   solutions of 3.24 and 3.25), or `.isupper()` (3.27, 3.28). Add a short Strings
   note and a digit-stripping pattern to Chapter 3.
5. **Reference solutions that run ahead of the notes.** Students are told they
   can read these. 4.23 uses lists and `random.shuffle` before Lists. 5.27, 5.29
   and 5.30 use sets before Sets. 9.18 uses `re`, which no note teaches. Rewrite
   them with what has been taught.

Decisions, 2026-11-01:

- Item 1 declined: the prompts stay, and only the wordiest (1.35, 3.32) were
  shortened. The preface's description of the Input column is still inexact for
  these 13 exercises.
- Item 2 done.
- Item 3 declined: 6.1 and 7.4 stay where they are.
- Item 4 done: `repetitions/_docs/string_loops.md` and Pattern 4 in
  `loop_patterns.md`.
- Item 5 done: 4.23 `password` moved to Lists as 5.22 and keeps its list-based
  solution, which renumbers the later exercises of Chapters 4 and 5. 9.18 no longer
  uses `re`, and 5.27, 5.29 and 5.30 (numbered as in this review) use lists. A syntax
  scan then found the same problem in 3.31, 4.18 and 4.19 (lists), and in 3.28 and
  4.16 (an inline `if`/`else`, which no note shows). Those were rewritten too.
  `random.shuffle` is now taught in `list_operations.md`, which `deck_operations`
  also needed.

## Teaching changes, in priority order

1. **Add reading practice.** Give each chapter 5-8 "Check Yourself" items at its
   start: predict the output, explain in one sentence what this does, put these
   lines in order. Answers go at the back, beside the hints. Aim the items at
   known misconceptions, such as `=` versus `==`, or aliasing a list. Have a test
   run each snippet so a printed answer can't go wrong. Evidence: Xie 2019 orders
   the skills as tracing, then syntax, then templates; PRIMM 2019 beat its control
   group; Lopez 2008 links tracing and explaining to writing, though a 2022
   replication didn't confirm its strict hierarchy; faded Parsons problems taught
   writing about as well as writing exercises did.
2. **Teach debugging as a skill.** Add a Chapter 1 note on reading a traceback
   and a Chapter 3 note on stepping through a loop in PyCharm's debugger. Add
   2-3 "fix this program" exercises per chapter from Chapter 2. The walkthrough
   already includes a mistake, which is the right model. Evidence: Michaeli &
   Romeike 2019 improved debugging performance and confidence by teaching a
   systematic process. Think Python 3e's first chapter has its own Debugging
   section.
3. **Build the Error Handling chapter.** `try` is taught but never practiced:
   none of the 222 reference solutions uses it, and no Files exercise mentions
   errors. The chapter is a reference sheet, and its `with` section runs ahead of
   Files. Rewrite it to teach, move `with` to Files, and add about 8 exercises:
   read this traceback, retry until the input is valid, raise for bad input. Then
   make 2-3 Files exercises handle a missing file, which gives Chapter 8 a reason
   to come right before Chapter 9.
4. **Strengthen Chapter 3.** `nested_loops.md` is 74 words with one example, and
   `loop_patterns.md` is 143 words for 35 exercises. Name the patterns: counter,
   accumulator, best so far, sentinel, flag, digit stripping. Evidence: roles of
   variables (Sajaniemi & Kuittinen 2005, a Pascal study) and Xie's templates.
5. **Add one worked example per chapter with labeled steps**: understand, plan,
   write, test. Evidence: Margulieux 2020, 265 students: better quizzes and fewer
   students dropping or failing, but exam averages no better. This carries the
   load without adding hints, in line with the choice to keep hints rare.
6. **Make students understand the problem before coding.** Add one line to the
   walkthrough and preface: work one example by hand first. Evidence: Prather 2019
   (a controlled experiment), Wrenn & Krishnamurthi 2019, and the design recipe in
   How to Design Programs. Later, in Functions, have students write tests for
   their own code, as CS50P does.

Decisions, 2026-11-01:

- Item 1 declined: no reading practice.
- Item 2 changed: `appendix/debugging.md` replaces the Chapter 1 and 3 notes, and
  there are no "fix this program" exercises.
- Item 3 done, with 4 examples followed directly by their solutions
  (`errors/_docs/error_examples.md`) instead of about 8 exercises. The chapter is
  rewritten as `error_basics.md` and `raising_errors.md`, and `with` moved to
  `file_basics.md`. Missing-file handling in 9.1 `read_file_content`, 9.5 `head`
  and 9.12 `merge_files`, with a "Missing Files" note, was written and then
  removed to keep the Files chapter simple for now.
- Item 4 done: six named patterns in `loop_patterns.md`, a longer
  `nested_loops.md`, and `break` in nested loops in `loop_control.md`.
- Item 5 dropped: written for all 10 chapters, then removed as too bloated.
- Item 6 partly done: the by-hand advice is in the preface and both walkthroughs.
  Whether students write their own tests is still open.

## Making it usable for a course

7. **Print a difficulty mark and a core path.** At about 16 exercises a week over
   14 weeks, nobody assigns all 222. Mark each one core, practice or challenge,
   with about a third core. Have the manifest read the table-of-contents groups,
   and add groups to the five chapters without them. Knuth's 0-50 scale is the
   precedent; three levels are enough here.
8. **Turn the repeats into deliberate spacing.** Add one line to the 20 later
   versions: "You wrote this as a program in Exercise 3.10; now make it a
   function." End each chapter with 3-5 mixed exercises that use earlier skills.
   Evidence: Dunlosky 2013 rates practice testing and spaced practice highest,
   and Rohrer & Taylor (see `curriculum-research.md`) found the same for
   interleaving. Both are general or math evidence, not programming.
9. **Frame each chapter.** Put 3-5 outcomes facing the map ("you can..."), and end
   with a checklist. This pairs with the glossary todo. Retitle the notes for
   print: "Lists in Python - Basics" becomes "List Basics" inside the Lists
   chapter, and "Python Error Handling Guide" becomes "Handling Errors".
10. **Tell students why to work without AI.** Add a short preface paragraph: tools
    can hide what you haven't learned yet. Evidence is thin: The Widening Gap 2024
    is a lab study of 21 novices. Think Python 3e takes the other side and invites
    readers to ask a virtual assistant.
11. **State the book's scope.** Add a closing "Where to go next" page that names
    what the book leaves out, such as classes and regular expressions. Classes are
    still the largest missing topic (7 of 8 curricula teach them), but they come
    last, after everything above.

## Repo changes that keep this fixed

- **Check listings in the build.** Run each printed listing and fail when a
  `print(x)  # y` comment is wrong, with a way to mark descriptive comments.
- **Check prerequisites.** Report any builtin or method that a reference solution
  calls before a note has shown it. Item 4 and item 5 above came from a scan like
  this. Report only at first, since it can't see every concept.
- **Correct the README.** It still says the PDF is "rebuilt whenever the content
  changes", but the book's CI no longer runs on push.

## Leave alone

- Chapter order, visible tests and comprehensions: see `curriculum-research.md`.
- The two exercise formats, and examples that overlap the tests: declined on
  2026-08-04.
- Prompts in the Input column, and the order of 6.1 and 7.4: declined on
  2026-11-01.
- Reading practice, "fix this program" exercises, and a worked example per
  chapter: declined on 2026-11-01.
- The `*2` variants and rare hints: existing conventions.

## Limits of this review

- Most papers were read as abstracts or summaries, not in full.
- Several studies aren't about university Python: PRIMM studied ages 11-14,
  Michaeli & Romeike a K-12 setting, and Sajaniemi Pascal.
- The prerequisite scan only finds named calls, and a student may solve an
  exercise differently from the reference solution.

## Sources

- [Xie et al. 2019, A theory of instruction for introductory programming skills](https://faculty.washington.edu/ajko/papers/Xie2019IntroCSTheoryOfInstruction.pdf)
- [Sentance, Waite & Kallia 2019, Teaching computer programming with PRIMM](https://qmro.qmul.ac.uk/xmlui/handle/123456789/57800)
- [Lopez et al. 2008, Relationships between reading, tracing and writing skills](https://opus.lib.uts.edu.au/handle/10453/10806)
- [Replication record for Lopez et al.](https://forrt.org/flora-replication-atlas/doi/10.1145/1404520.1404531/)
- [Weinman et al. 2021, Faded Parsons Problems](https://acelab.berkeley.edu/wp-content/papercite-data/pdf/parsons-chi2021.pdf)
- [Qian & Lehman 2017, Students' misconceptions and other difficulties](https://www.springerprofessional.de/doi/10.1145/3077618)
- [Michaeli & Romeike 2019, Improving debugging skills in the classroom](https://computingeducation.de/pub/2019_Michaeli-Romeike_WIPSCE19.pdf)
- [Think Python 3e, chapter 1](https://allendowney.github.io/ThinkPython/chap01.html)
- [Sajaniemi & Kuittinen 2005, roles of variables](https://saja.kapsi.fi/var_roles/abstracts/cse05.html)
- [Margulieux, Morrison & Decker 2020, subgoal labeled worked examples](https://stemeducationjournal.springeropen.com/articles/10.1186/s40594-020-00222-7)
- [Prather et al. 2019, First Things First](https://www.springerprofessional.de/doi/10.1145/3287324.3287374)
- [Wrenn & Krishnamurthi 2019, Executable Examples](https://cs.brown.edu/~sk/Publications/Papers/Published/wk-examplar/)
- [How to Design Programs](https://en.wikipedia.org/wiki/How_to_Design_Programs)
- [The Art of Computer Programming, exercise ratings](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)
- [Dunlosky et al. 2013, summary from the Association for Psychological Science](https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html)
- [Prather et al. 2024, The Widening Gap](https://arxiv.org/abs/2405.17739v1)
