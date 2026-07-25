# Chapter 5 release audit

Audit date: 2026-07-25

## Release scope

- Canonical corpus: 100 questions, Q001–Q100.
- Languages: Chinese and English with matching identifiers and structure.
- Release artifacts: two exercise workbooks and two detailed-solution volumes.
- Pages: 102 + 202 Chinese pages and 102 + 202 English pages (608 total).

## Mathematics and editorial checks

- All 16 single- and multiple-choice items were reviewed option by option; their
  answer keys are pinned by regression tests.
- Parameter hypotheses and convergence ranges were explicitly checked for the
  power, exponential, Gamma, Beta-type, and comparison-test problems.
- Absolute-value branch handling, interior-singularity splitting, ordinary
  improper convergence, and Cauchy principal values were reviewed separately.
- Every solution has knowledge points, analysis, at least four derivation
  steps, pitfalls, verification, takeaway, and extension fields.
- Direct-evaluation questions are compared by normalized mathematical
  signatures rather than whole-prompt text. Regression fixtures preserve the
  former Q045/Q051 and Q047/Q059 cross-part duplicate cases; the current corpus
  contains no matching evaluation signatures in either language.
- Structural, quota, source-lineage, and bilingual validation report zero
  errors and zero unresolved heuristic differences; all 56 tests pass.

## Formula and PDF checks

- The migration audit reports that zero source files require normalization.
- KaTeX 0.17.0 parses 3,247 formula occurrences (1,003 unique) with
  `throwOnError=true` and `strict=error`; parse errors: zero.
- Tectonic 0.16.9/XeTeX builds vector mathematics with STIX Two Math.
- A second isolated build reproduced all four PDFs byte for byte.
- PDF validation found all 100 bookmarks in each file, the expected page sizes,
  embedded fonts, no empty streams, and no JavaScript, launch actions, or
  attachments.
- PDFium rendered and checked all 608 pages; clipping, edge-collision,
  suspicious-sparsity, and render errors: none.
- The corrected Chinese and English pages for Q004, Q016, Q025, Q051, Q059,
  Q071, Q081, and Q090 were visually reviewed at full resolution.

## Publication and supply-chain checks

- `LICENSE` contains CC BY-NC-SA 4.0; both READMEs accurately call the project
  source-available rather than OSI-approved open source.
- `SOURCES.md` distinguishes topic/method lineage from textual provenance and
  states that no commercial-textbook wording or worked solution is reproduced.
- OpenStax, MIT OpenCourseWare, Higher Education Press, and Tongji scope links
  were checked for this release.
- `THIRD_PARTY_NOTICES.md` identifies the build tools and embedded font
  families; font binaries and the TeX bundle are not committed.
- `package-lock.json` is present, dependencies are pinned or range-bounded, and
  `npm audit --omit=dev` reported zero vulnerabilities.
- A repository text scan found no credentials, private keys, personal absolute
  paths, local-only URLs, or unresolved editorial placeholders in release
  files.
- Build caches, virtual environments, `node_modules`, rendered-page work files,
  and temporary TeX assets are excluded by `.gitignore`.
- `SHA256SUMS` contains exactly the four release PDFs.

## Known limitations

- The workbook is an independent practice set aligned to the chapter scope; it
  is not an official Tongji or Higher Education Press edition.
- One hundred questions cannot exhaust every substitution and convergence-test
  pattern, and the Gamma-function material is explicitly enrichment.
- External reference availability can change after the audit date.
- This audit covers repository and PDF readiness; GitHub publication and
  Goodnotes import are separate delivery actions.
