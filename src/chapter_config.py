from __future__ import annotations


CHAPTER_NUMBER = 5

CHAPTER_TITLES = {
    "zh": ("定积分", "第五章"),
    "en": ("Definite Integrals", "Chapter 5"),
}

SECTION_INFO = {
    1: ("定积分的概念与性质", "Definition and Properties of the Definite Integral"),
    2: (
        "微积分基本公式",
        "The Fundamental Theorem of Calculus",
    ),
    3: (
        "定积分的换元法和分部积分法",
        "Substitution and Integration by Parts for Definite Integrals",
    ),
    4: ("反常积分", "Improper Integrals"),
    5: (
        "反常积分的审敛法与 Gamma 函数（选学）",
        "Convergence Tests and the Gamma Function (Enrichment)",
    ),
}

SECTION_QUOTAS = {1: 20, 2: 24, 3: 26, 4: 18, 5: 12}

OUTPUT_FILENAMES = {
    ("zh", "exercises"): "同济高数第七版_第五章_习题册_中文.pdf",
    ("zh", "solutions"): "同济高数第七版_第五章_超详细解析_中文.pdf",
    ("en", "exercises"): "Tongji_Calculus_7e_Chapter_5_Exercises_EN.pdf",
    (
        "en",
        "solutions",
    ): "Tongji_Calculus_7e_Chapter_5_Detailed_Solutions_EN.pdf",
}

SCOPE_BOUNDARY_ZH = (
    "只使用截至第五章已经建立的工具；第五节反常积分审敛法与 Gamma 函数明确标为选学。"
)
SCOPE_BOUNDARY_EN = (
    "Use only tools established through Chapter 5; convergence tests for "
    "improper integrals and the Gamma function are explicitly enrichment topics."
)
