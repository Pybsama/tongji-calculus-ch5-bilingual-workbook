from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sys
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.bilingual_checks import validate_bilingual
from src.corpus import load_questions, validate_questions
from src.formula_semantics import audit_formula_semantics
from src.math_markup import audit_text


PART = ROOT / "content" / "parts" / "part_a_q001_q050.json"


def walk_strings(value: Any, path: str = "root") -> Iterable[tuple[str, str]]:
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_strings(child, f"{path}[{index}]")
    elif isinstance(value, dict):
        for key, child in value.items():
            yield from walk_strings(child, f"{path}.{key}")


def main() -> int:
    questions = load_questions(PART)
    errors = validate_questions(questions, enforce_quotas=False)
    errors.extend(validate_bilingual(questions))

    expected_ids = [f"Q{index:03d}" for index in range(1, 51)]
    actual_ids = [item["id"] for item in questions]
    if actual_ids != expected_ids:
        errors.append("checkpoint IDs must be ordered exactly Q001-Q050")

    expected_sections = Counter({1: 20, 2: 24, 3: 6})
    actual_sections = Counter(item["section"] for item in questions)
    if actual_sections != expected_sections:
        errors.append(
            f"checkpoint section counts: expected {dict(expected_sections)}, "
            f"got {dict(actual_sections)}"
        )

    formula_count = 0
    for item in questions:
        for path, text in walk_strings(item, item["id"]):
            errors.extend(f"{path}: {message}" for message in audit_text(text))
            errors.extend(
                f"{path}: {message}" for message in audit_formula_semantics(text)
            )
            formula_count += len(text.split("$")[1::2])

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    categories = Counter(
        item["source_lineage"]["category"] for item in questions
    )
    print(
        "Validated 50 questions with enforce_quotas=False; "
        f"formulas={formula_count}; "
        f"sections={dict(sorted(actual_sections.items()))}; "
        f"lineage={dict(sorted(categories.items()))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
