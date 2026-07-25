from __future__ import annotations

from src.chapter_config import SECTION_INFO

DIFFICULTY_LABELS = {
    "basic": ("基础", "Basic"),
    "standard": ("常规", "Standard"),
    "advanced": ("进阶", "Advanced"),
    "hard": ("困难", "Hard"),
    "challenge": ("挑战", "Challenge"),
}

TYPE_LABELS = {
    "single_choice": ("单项选择", "Single choice"),
    "multiple_choice": ("多项选择", "Multiple choice"),
    "true_false": ("判断辨析", "True/false with justification"),
    "fill_blank": ("填空", "Fill in the blank"),
    "calculation": ("计算", "Calculation"),
    "proof": ("证明", "Proof"),
    "comprehensive": ("参数·综合·应用", "Parameter / synthesis / application"),
    "error_diagnosis": ("错解诊断", "Error diagnosis"),
}

TIER_LABELS = {
    "foundation": ("基础篇", "Foundation"),
    "methods": ("方法篇", "Methods"),
    "synthesis": ("综合篇", "Synthesis"),
    "challenge": ("挑战篇", "Challenge"),
}
