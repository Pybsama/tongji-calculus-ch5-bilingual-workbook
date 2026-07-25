from __future__ import annotations


SOURCE_LINEAGE_CATEGORIES = frozenset(
    {
        "open_text_adaptation",
        "classic_method_variant",
        "original_synthesis",
    }
)

CATEGORY_RELATIONS = {
    "open_text_adaptation": "adapted_from_open_text_topic_and_method",
    "classic_method_variant": "independently_rewritten_classic_method_variant",
    "original_synthesis": "independently_synthesized_from_standard_methods",
}

SOURCE_REFERENCES = {
    "openstax-calculus-v1-5.2": {
        "title": "OpenStax Calculus Volume 1, 5.2 The Definite Integral",
        "url": "https://openstax.org/books/calculus-volume-1/pages/5-2-the-definite-integral",
    },
    "openstax-calculus-v1-5.3": {
        "title": "OpenStax Calculus Volume 1, 5.3 The Fundamental Theorem of Calculus",
        "url": (
            "https://openstax.org/books/calculus-volume-1/pages/"
            "5-3-the-fundamental-theorem-of-calculus"
        ),
    },
    "openstax-calculus-v1-5.5": {
        "title": "OpenStax Calculus Volume 1, 5.5 Substitution",
        "url": "https://openstax.org/books/calculus-volume-1/pages/5-5-substitution",
    },
    "openstax-calculus-v2-3.1": {
        "title": "OpenStax Calculus Volume 2, 3.1 Integration by Parts",
        "url": "https://openstax.org/books/calculus-volume-2/pages/3-1-integration-by-parts",
    },
    "openstax-calculus-v2-3.7": {
        "title": "OpenStax Calculus Volume 2, 3.7 Improper Integrals",
        "url": "https://openstax.org/books/calculus-volume-2/pages/3-7-improper-integrals",
    },
    "mit-18.01sc-definite-integral": {
        "title": "MIT OpenCourseWare 18.01SC, Unit 3: The Definite Integral and Its Applications",
        "url": (
            "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/"
            "pages/unit-3-the-definite-integral-and-its-applications/"
        ),
    },
    "mit-18.01sc-improper-integrals": {
        "title": "MIT OpenCourseWare 18.01SC, Session 91: Improper Integrals",
        "url": (
            "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/"
            "resources/mit18_01scf10_ses91d/"
        ),
    },
    "mit-18.100a-gamma": {
        "title": "MIT OpenCourseWare 18.100A, Improper Integrals and Gamma Function",
        "url": (
            "https://ocw.mit.edu/courses/18-100a-introduction-to-analysis-fall-2012/"
            "pages/calendar/"
        ),
    },
}

METHOD_FAMILY_REFERENCES = {
    "riemann_sums_and_definition": frozenset(
        {"openstax-calculus-v1-5.2", "mit-18.01sc-definite-integral"}
    ),
    "definite_integral_properties": frozenset(
        {"openstax-calculus-v1-5.2", "mit-18.01sc-definite-integral"}
    ),
    "integral_mean_value_and_average": frozenset(
        {"openstax-calculus-v1-5.2", "mit-18.01sc-definite-integral"}
    ),
    "fundamental_theorem_and_new_functions": frozenset(
        {"openstax-calculus-v1-5.3", "mit-18.01sc-definite-integral"}
    ),
    "newton_leibniz_evaluation": frozenset(
        {"openstax-calculus-v1-5.3", "mit-18.01sc-definite-integral"}
    ),
    "definite_integral_substitution": frozenset(
        {"openstax-calculus-v1-5.5", "mit-18.01sc-definite-integral"}
    ),
    "definite_integral_by_parts": frozenset(
        {"openstax-calculus-v2-3.1", "mit-18.01sc-definite-integral"}
    ),
    "improper_integral_infinite_interval": frozenset(
        {"openstax-calculus-v2-3.7", "mit-18.01sc-improper-integrals"}
    ),
    "improper_integral_singular_endpoint": frozenset(
        {"openstax-calculus-v2-3.7", "mit-18.01sc-improper-integrals"}
    ),
    "improper_integral_interior_singularity": frozenset(
        {"openstax-calculus-v2-3.7", "mit-18.01sc-improper-integrals"}
    ),
    "improper_integral_convergence_tests": frozenset(
        {"openstax-calculus-v2-3.7", "mit-18.01sc-improper-integrals"}
    ),
    "gamma_function_enrichment": frozenset(
        {"mit-18.100a-gamma", "openstax-calculus-v2-3.7"}
    ),
}
