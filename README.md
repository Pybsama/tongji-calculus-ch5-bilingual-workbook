# Tongji Calculus Chapter 5 — Bilingual Workbook

[简体中文说明](README.zh-CN.md)

A Goodnotes-ready bilingual practice set aligned with Chapter 5, **Definite
Integrals**, in the seventh edition of Tongji University’s *Advanced
Mathematics*. This is an independently authored project, not an official
Tongji University or Higher Education Press publication.

## Downloads

- [Chinese exercise workbook](dist/同济高数第七版_第五章_习题册_中文.pdf)
- [Chinese detailed solutions](dist/同济高数第七版_第五章_超详细解析_中文.pdf)
- [English exercise workbook](dist/Tongji_Calculus_7e_Chapter_5_Exercises_EN.pdf)
- [English detailed solutions](dist/Tongji_Calculus_7e_Chapter_5_Detailed_Solutions_EN.pdf)
- [SHA-256 checksums](SHA256SUMS)
- [Release and formula audit](reports/release_audit.md)

## Contents

- Exactly 100 questions progressing through basic, standard, advanced, hard,
  and challenge levels.
- Coverage of Riemann sums, properties and average value, the Fundamental
  Theorem of Calculus, Newton–Leibniz evaluation, substitution, integration by
  parts, improper integrals, convergence tests, and Gamma-function enrichment.
- Eight formats: single choice, multiple choice, true/false, fill-in,
  calculation, proof, synthesis, and error diagnosis.
- Every solution includes knowledge points, method analysis, at least four
  derivation steps, pitfalls, verification, a takeaway, and an extension
  prompt.
- Stable Q001–Q100 identifiers across all four PDFs.
- Spacious 4:3 layouts: one landscape writing page per exercise and portrait
  pages for detailed solutions.

## Mathematics-quality gate

All mathematics in prompts, choices, answers, and solutions is stored as
explicit standard LaTeX. The release pipeline:

1. rejects raw Unicode math shortcuts, slash-style fractions, malformed
   delimiters, and high-risk ambiguous notation;
2. strictly parses every formula occurrence with pinned KaTeX 0.17.0;
3. compiles vector mathematics through Tectonic 0.16.9/XeTeX with STIX Two
   Math;
4. checks bilingual structure, all 100 question bookmarks, fonts, page sizes,
   checksums, reproducibility, and unsafe PDF actions;
5. renders every PDF page with PDFium for clipping and sparse-page checks,
   followed by human review of representative formula-dense pages.

“KaTeX compatible” describes the source audit. The PDFs contain
XeTeX-typeset vector mathematics, not visible `$...$` source markers.
Improper integrals are split at every singular point; a Cauchy principal value
is never presented as ordinary convergence.

## Provenance and authorship boundary

Every item carries auditable `source_lineage` metadata:

- 20 open-text method adaptations;
- 50 independently rewritten classic-method variants;
- 30 original synthesis, comparison, proof, or diagnosis problems.

The open references are OpenStax Calculus and MIT OpenCourseWare. No
commercial-textbook wording or worked solution is reproduced. Tongji and
Higher Education Press pages are used only to verify the edition and chapter
scope. See [SOURCES.md](SOURCES.md) for the exact registry and attribution
rules.

## Suggested study route

1. Work through Q001–Q100 without opening the solution volume.
2. Classify errors as conceptual, endpoint orientation, algebraic,
   method-selection, parameter-domain, singularity-splitting, or convergence
   errors.
3. Verify finite integrals by differentiation, symmetry, estimates, or an
   independent substitution.
4. For improper integrals, write the defining limit before calculating and
   check every problematic endpoint separately.
5. Retry missed questions after 48 hours, then interleave topics one week
   later.

## Strengths and limitations

The set combines formula fluency with definition-level reasoning, proof,
parameter classification, error diagnosis, and independent verification.
The sequence explicitly distinguishes signed area from geometric area,
ordinary improper convergence from principal value, and sufficient estimates
from exact evaluation. Chinese and English versions have matching IDs and
structure.

One hundred questions cannot exhaust every substitution pattern or
convergence comparison, and perceived difficulty depends on prior algebra and
trigonometry. Gamma-function material is marked as enrichment. A static PDF
cannot adapt to an individual error history. A “classic-method variant”
identifies a teaching tradition, not a verbatim problem from a commercial
book.

## Build and verify locally

The verified stack uses Python 3.12+, Node.js 20+, KaTeX 0.17.0, Tectonic
0.16.9, and pinned `default_bundle_v33`. Fandol, TeX Gyre Heros, and STIX Two
Math provide the open fonts.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
npm ci
python scripts/generate_checkpoint_q001_q050.py
python scripts/generate_q051_q100.py
python scripts/merge_corpus.py
python scripts/migrate_latex.py
python scripts/validate_content.py
pytest -q
npm run validate:katex
python scripts/build_pdfs.py
python scripts/verify_reproducible.py
python scripts/update_checksums.py
python scripts/validate_pdfs.py
python scripts/render_validate.py
```

Editable source is under [`content/parts`](content/parts);
[`content/questions.json`](content/questions.json) is the canonical merged
corpus. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for typesetting
and font notices.

Original project content is licensed as described in [LICENSE](LICENSE). CC
BY-NC-SA 4.0 permits noncommercial sharing and adaptation. Because of its
NonCommercial restriction, this repository is accurately described as
publicly source-available rather than OSI-approved open-source software.
