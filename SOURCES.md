# Sources, method lineage, and attribution boundaries

## What `source_lineage` means

Every question has a machine-validated `source_lineage` object:

- `category` records whether the item is an open-text method adaptation, a
  classic-method variant, or an original synthesis;
- `method_family` records the integration topic or technique being trained;
- `relation` is a fixed editorial description;
- `references` contains registered open educational pages that document the
  topic and method.

References establish **topic and method lineage only**. They do not claim that
a question, sentence, parameter choice, answer choice, or worked solution was
copied from a linked page.

| Category | Required relation | Meaning |
|---|---|---|
| `open_text_adaptation` | `adapted_from_open_text_topic_and_method` | Independently written exercise based on an openly documented method or archetype. |
| `classic_method_variant` | `independently_rewritten_classic_method_variant` | Independently written variant of a standard calculus method. |
| `original_synthesis` | `independently_synthesized_from_standard_methods` | Independently designed synthesis, comparison, proof, or diagnosis. |

No item attributes wording to Tongji, Stewart, Thomas, or another commercial
textbook. The `classic_method` flag identifies a teaching tradition, not
textual provenance.

## Open educational reference registry

The validator rejects unknown identifiers and references not registered for an
item’s method family. All links below were rechecked for this release.

| Identifier | Open educational page |
|---|---|
| `openstax-calculus-v1-5.2` | [OpenStax Calculus Volume 1, 5.2 The Definite Integral](https://openstax.org/books/calculus-volume-1/pages/5-2-the-definite-integral) |
| `openstax-calculus-v1-5.3` | [OpenStax Calculus Volume 1, 5.3 The Fundamental Theorem of Calculus](https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus) |
| `openstax-calculus-v1-5.5` | [OpenStax Calculus Volume 1, 5.5 Substitution](https://openstax.org/books/calculus-volume-1/pages/5-5-substitution) |
| `openstax-calculus-v2-3.1` | [OpenStax Calculus Volume 2, 3.1 Integration by Parts](https://openstax.org/books/calculus-volume-2/pages/3-1-integration-by-parts) |
| `openstax-calculus-v2-3.7` | [OpenStax Calculus Volume 2, 3.7 Improper Integrals](https://openstax.org/books/calculus-volume-2/pages/3-7-improper-integrals) |
| `mit-18.01sc-definite-integral` | [MIT OpenCourseWare 18.01SC, Unit 3: The Definite Integral and Its Applications](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-3-the-definite-integral-and-its-applications/) |
| `mit-18.01sc-improper-integrals` | [MIT OpenCourseWare 18.01SC, Session 91: Improper Integrals](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/resources/mit18_01scf10_ses91d/) |
| `mit-18.100a-gamma` | [MIT OpenCourseWare 18.100A calendar: improper integrals, convergence, and Gamma function](https://ocw.mit.edu/courses/18-100a-introduction-to-analysis-fall-2012/pages/calendar/) |

OpenStax and MIT OpenCourseWare publish their own license and attribution
terms. This repository links to their pages and does not incorporate their
problem statements or worked solutions.

## Method families

The registered families are:

- `riemann_sums_and_definition`
- `definite_integral_properties`
- `integral_mean_value_and_average`
- `fundamental_theorem_and_new_functions`
- `newton_leibniz_evaluation`
- `definite_integral_substitution`
- `definite_integral_by_parts`
- `improper_integral_infinite_interval`
- `improper_integral_singular_endpoint`
- `improper_integral_interior_singularity`
- `improper_integral_convergence_tests`
- `gamma_function_enrichment`

Each question’s reference list must be a subset of the sources allowed for its
family; this is enforced in `src/source_lineage.py` and the corpus tests.

## Tongji scope references

These public pages are used only to verify seventh-edition metadata, the
Chapter 5 title, and course scope:

- [Higher Education Press, Advanced Mathematics (7th edition), Volume I](https://www.hep.com.cn/book/show/f9a5ba29-e58e-4a42-9c1b-830a0e28f1f3)
- [Tongji University, Advanced Mathematics synchronous course preview](https://gaoshutongbu.tongji.edu.cn/kcyx.htm)

No Tongji problem statement or worked example is reproduced verbatim. The
textbook title and institutional names are used descriptively; this project is
unofficial and unaffiliated.

## Scope note

The Gamma-function and convergence-test material in Section 5 is explicitly
marked as enrichment. An integral with an interior singularity is split into
two independent one-sided improper integrals. A symmetric Cauchy principal
value is reported only as a principal value, never as ordinary convergence.
