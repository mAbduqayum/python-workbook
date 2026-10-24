# Turning the workbook into a book — practice, pedagogy, and Typst

Research note, 2026-10-24. Covers how well-regarded exercise books are
organized, what the learning research says about hints and solutions, book
typography, keeping a book in sync with a living repo, and the state of Typst
(0.15.1) for building one. Sources inline; anything marked **[unverified]**
came from secondary sources or memory and was not confirmed against a primary.

**Headline: every respected exercise book keeps answers away from problems,
numbers exercises per chapter, and repeats one chapter rhythm (concept →
example → graded exercises). Typst 0.15 can build such a book straight from
the repo's markdown — cmarker renders the `.md` files at compile time and mmdr
renders the mermaid mindmaps natively — but Typst cannot list directories, so
a small script must write a manifest for it.**

---

## 1. How exercise books are organized

- **Numbering.** SICP numbers by chapter (**Exercise 1.7**) and places
  exercises inline after the material they test
  ([SICP 1.1](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/full-text/book/book-Z-H-10.html)).
  HtDP numbers 1…N globally at subsection ends, no difficulty marks, uses
  "Hint" notes ([HtDP Part I](https://htdp.org/2023-8-14/Book/part_one.html)).
  K&R uses "Exercise 1-1". Global numbering shifts every later number when an
  exercise is inserted early — a poor fit for a book that rebuilds on every
  content change.
- **Per-exercise template.** *Python Workout* repeats the same headings for
  every exercise: Exercise N → Working it out → Solution → Beyond the exercise
  ([livebook ch. 1](https://livebook.manning.com/book/python-workout/chapter-1)).
  *Exercises for Programmers* gives constraints and challenges, ramps from
  simple I/O to larger programs, and ships **no solutions**
  ([PragProg](https://pragprog.com/titles/bhwb/exercises-for-programmers/)).
- **Where answers live.**
  - *Automate the Boring Stuff* 2e: end-of-chapter questions, answers in
    Appendix C; projects get no answers because "there is no one correct
    program" ([Appendix C](https://automatetheboringstuff.com/2e/appendixc/)).
  - *Python Crash Course*: selected solutions online, with the warning "Be
    careful about looking at the solutions too quickly"
    ([solutions](https://ehmatthes.github.io/pcc_3e/solutions/)).
  - K&R: a separate volume, *The C Answer Book*.
  - TAOCP rates exercises 00–50, answers at the back
    ([answers](https://www.oreilly.com/library/view/the-art-of/9780321635792/ans.xhtml)).
  - EPI reportedly rates difficulty and gives hints **[unverified]**.
- **Nobody prints full solutions beside the problems.**

## 2. What the learning research says

- **Worked examples, then fading.** Novices learn more from studying solved
  problems than from solving unaided; the benefit reverses with expertise, so
  steps should be withdrawn gradually
  ([MIT Open Learning on Sweller, Renkl, Kalyuga](https://openlearning.mit.edu/mit-faculty/research-based-learning-findings/worked-and-faded-examples)).
  Subgoal labels help in programming specifically
  ([Margulieux, Morrison & Decker 2020](https://doaj.org/article/9a2c85d66fd54ec9ab019e9a510bbf17)).
- **Retrieval and spacing are the high-utility techniques**; interleaving and
  self-explanation moderate; rereading and highlighting low (Dunlosky et al.
  2013, DOI 10.1177/1529100612453266;
  [APS](https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html)).
  Testing beats restudying on delayed tests
  ([Roediger & Karpicke 2006](https://psychology.ecu.edu/wp-content/pv-uploads/sites/216/2019/03/Roediger-Karpicke-2006.pdf)).
- **Interleaved review beat blocked practice** 61% vs 38% a month later
  (d = 0.83) in one randomized math study
  ([IES](https://ies.ed.gov/use-work/awards/efficacy-study-interleaved-mathematics-practice)).
- **Desirable difficulties only work when the learner can succeed**
  ([Bjork & Bjork 2011](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)) —
  the case for graded hints.
- **Why answers should be hard to reach.** A failed attempt followed by the
  answer beats reading the answer
  ([Kornell, Hays & Bjork 2009](https://pubmed.ncbi.nlm.nih.gov/19586265/));
  copying homework went with falling exam scores at MIT, correlationally
  ([Palazzo et al. 2010](https://dspace.mit.edu/handle/1721.1/58844)); tutoring
  systems saw hint abuse on 36% of actions, often clicking straight through to
  the answer ([LearnLab](https://learnlab.org/research/wiki/index.php/Help_abuse)).
- **Parsons problems** give similar gains to writing code in less time
  ([Ericson, GT](https://hg.gatech.edu/node/603172)).

## 3. Book design and typography

- Body text 10–12 pt; 45–90 characters per line
  ([Butterick: point size](https://practicaltypography.com/point-size.html),
  [line length](https://practicaltypography.com/line-length.html)).
- Inside (binding) margin grows with page count: 0.5 in at 151–300 pages,
  0.625 in at 301–500 ([KDP](https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6)).
  Publisher trim sizes (7×9.19, 7×9.25) **[unverified]**.
- Code lines ≤ ~80 characters, narrower for print.
- Syntax colour gave novices no measurable comprehension benefit
  (Hannebauer et al. 2018, abstract only), and black-and-white code was not
  significantly harder to read
  ([Beelders & du Plessis](https://bop.unibe.ch/JEMR/article/view/2429)) —
  colour is fine on screen as long as it survives grayscale printing.
- Code font must separate 0/O/o and 1/l/I
  ([Google Fonts](https://fonts.google.com/knowledge/glossary/legibility)).
- Accessibility: left-aligned ragged-right text, generous spacing
  ([Dyslexia Scotland](https://dyslexiascotland.org.uk/dyslexia-friendly-typed-formats)).
  Typst ≥ 0.14 writes tagged PDF by default and can target PDF/UA-1.

## 4. Keeping a book in sync with its repo

- **Pro Git** builds on every push to main, bumps the patch version, and
  attaches PDF/EPUB/HTML to a GitHub Release
  ([workflow](https://raw.githubusercontent.com/progit/progit2/main/.github/workflows/release-on-merge.yml)).
- **Quarto** books can render through Typst, number cross-references per
  chapter, and switch content per build with profiles
  ([Typst output](https://quarto.org/docs/output-formats/typst.html),
  [profiles](https://quarto.org/docs/projects/profiles.html)).
- Stamp the build into the book: Typst `--input` / `sys.inputs` carry the
  commit hash and date
  ([forum](https://forum.typst.app/t/can-i-configure-my-document-e-g-draft-release-version-color-theme-when-creating-a-pdf-without-modifying-the-typst-file-directly/160)).

## 5. Typst state (0.15.1, 2026-07-17)

Sources: [releases](https://github.com/typst/typst/releases),
[changelog](https://typst.app/docs/changelog/).

- **0.13** (2025-02): experimental HTML export; `json`/`yaml`/`toml` take a
  path or bytes; plugins became modules; outline reworked (`fill` moved to
  `outline.entry`).
- **0.14** (2025-10): tagged PDF by default, PDF/UA-1 opt-in, `figure.alt`,
  `par.justification-limits`, `--deps`, `typst info`.
- **0.15** (2026-06): `path` type; backslashes in paths are errors;
  experimental bundle export (several outputs from one project, needs
  `--features bundle`); HTML still "do not use for production"; multiple
  bibliographies; `divider`; `typst eval` supersedes `typst query`; scoped
  decoders such as `json.decode` removed.
- **Directory listing does not exist** ([#2123](https://github.com/typst/typst/issues/2123)),
  and there is no file-exists test. The recommended pattern is a script that
  writes a file list, which Typst `json()`s and loops over
  ([forum](https://forum.typst.app/t/is-it-possible-to-automate-import-of-typ-files-import-folder-typ/2353)).
  Computed paths in `read` / `include` work.
- **Path gotcha:** a plain string passed to a helper in another file resolves
  relative to *that* file; `"/…"` resolves from `--root`. Helpers should take
  root-absolute strings or `path` values.
- **`watch` only tracks files that were read**, so new exercise folders need
  the manifest regenerated.

### Packages (versions from the Universe index)

| Package | Version | Verdict |
|---|---|---|
| cmarker | 0.1.10 | Markdown → Typst at compile time; CommonMark + tables, footnotes, highlighted fences, some HTML; `h1-level`, `label-prefix`, `scope` overrides (incl. `link`). Author: "not for one-time conversions" — use Pandoc for that. |
| mmdr | 0.2.2 | Native mermaid via mermaid-rs-renderer (23 diagram types incl. mindmap); rendered all 12 repo diagrams. |
| merman | 0.5.0 | Failed on the conditionals mindmap (`max_layout_work_units` exceeded). Avoid for now. |
| codly | 2.0.0 | Code block styling; new API (`show raw…: codly.new`). Must be declared before the mermaid rule. |
| zebraw | 0.6.3 | codly alternative with experimental HTML support. |
| hydra | 0.6.3 | Standard running headers. |
| bookly | 5.2.0 | Full book template with themes and front/back matter. |
| ilm | 2.1.1 | Minimal non-fiction template. |
| orange-book | 0.7.1 | LaTeX-style; Quarto's default. |
| shiroa | 0.4.0 | mdBook-like, HTML-first; overkill for a PDF. |
| exercise-bank | 0.8.0 | Collects solutions at chapter end or a chosen spot. |
| gentle-clues | 1.3.1 | Ready-made callouts. |
| Pandoc | 3.12.1 | Maintained Typst writer, for one-off conversions. |

### Project and CI practice

- `template.typ` with a `#show: conf.with(...)` function + `main.typ`
  ([tutorial](https://typst.app/docs/tutorial/making-a-template/),
  [forum](https://forum.typst.app/t/best-practices-for-working-with-longer-documents/1228)).
  `typst.toml` is for packages only.
- Print layout: `page(margin: (inside:, outside:))`,
  `pagebreak(to: "odd", weak: true)`; switch variants with `--input`.
- Reproducible output: Typst embeds Libertinus Serif, New Computer Modern and
  DejaVu Sans Mono; use `--ignore-system-fonts`, and
  `SOURCE_DATE_EPOCH` / `--creation-timestamp`.
- CI: `typst-community/setup-typst@v5` with package caching.
- Formatting and editor: typstyle 0.15.2, tinymist 0.15.10.

## Sources not otherwise linked

- Dunlosky et al. (2013), *Improving Students' Learning With Effective
  Learning Techniques*, Psychological Science in the Public Interest.
- Hannebauer et al. (2018), *Does syntax highlighting help programming
  novices?*, Empirical Software Engineering.
