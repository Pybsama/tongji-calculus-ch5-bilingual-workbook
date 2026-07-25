from copy import deepcopy
from pathlib import Path

from src.corpus import load_questions, validate_questions
from src.semantic_duplicates import semantic_duplicate_groups


ROOT = Path(__file__).resolve().parents[1]


def _fixture(
    item_id: str,
    item_type: str,
    zh_prompt: str,
    en_prompt: str,
) -> dict:
    return {
        "id": item_id,
        "type": item_type,
        "zh": {"prompt": zh_prompt},
        "en": {"prompt": en_prompt},
    }


def test_old_cross_part_evaluation_duplicates_are_detected_semantically() -> None:
    old_items = [
        _fixture(
            "Q045",
            "calculation",
            r"用换元法计算 $\int_0^1\frac{2x}{1+x^2}\,dx$，并同步变换上下限。",
            r"Use substitution to evaluate $\int_0^1\frac{2x}{1+x^2}\,dx$, transforming both limits.",
        ),
        _fixture(
            "Q051",
            "fill_blank",
            r"计算 $\displaystyle \int_0^1\frac{2x}{1+x^2}\,dx=\underline{\qquad}$。",
            r"Evaluate $\displaystyle \int_0^1\frac{2x}{1+x^2}\,dx=\underline{\qquad}$.",
        ),
        _fixture(
            "Q047",
            "calculation",
            r"用分部积分法计算 $\int_0^1xe^x\,dx$。",
            r"Use integration by parts to evaluate $\int_0^1xe^x\,dx$.",
        ),
        _fixture(
            "Q059",
            "calculation",
            r"计算 $\displaystyle \int_{0}^{1} x e^x\,\mathrm{d}x$。",
            r"Evaluate $\displaystyle \int_{0}^{1} x e^x\,\mathrm{d}x$.",
        ),
    ]

    assert semantic_duplicate_groups(old_items, language="zh") == [
        ("Q045", "Q051"),
        ("Q047", "Q059"),
    ]
    assert semantic_duplicate_groups(old_items, language="en") == [
        ("Q045", "Q051"),
        ("Q047", "Q059"),
    ]


def test_current_corpus_has_no_semantic_evaluation_duplicates() -> None:
    questions = load_questions(ROOT / "content" / "questions.json")

    assert semantic_duplicate_groups(questions, language="zh") == []
    assert semantic_duplicate_groups(questions, language="en") == []


def test_corpus_validator_blocks_the_two_old_duplicate_pairs() -> None:
    questions = load_questions(ROOT / "content" / "questions.json")
    duplicated = deepcopy(questions)
    by_id = {item["id"]: item for item in duplicated}
    by_id["Q051"]["zh"]["prompt"] = (
        r"计算 $\displaystyle \int_0^1\frac{2x}{1+x^2}\,dx=\underline{\qquad}$。"
    )
    by_id["Q051"]["en"]["prompt"] = (
        r"Evaluate $\displaystyle \int_{0}^{1}\frac{2x}{1+x^2}\,\mathrm{d}x"
        r"=\underline{\qquad}$."
    )
    by_id["Q059"]["zh"]["prompt"] = r"计算 $\int_{0}^{1}x e^x\,\mathrm{d}x$。"
    by_id["Q059"]["en"]["prompt"] = r"Evaluate $\displaystyle\int_0^1xe^x\,dx$."

    errors = validate_questions(duplicated, enforce_quotas=True)

    assert any(
        "Semantic duplicate direct-evaluation tasks (zh): Q045, Q051" in error
        for error in errors
    )
    assert any(
        "Semantic duplicate direct-evaluation tasks (en): Q047, Q059" in error
        for error in errors
    )
