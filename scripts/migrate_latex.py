from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.math_markup import audit_text


PARTS = ROOT / "content" / "parts"


def _localized_payload(question: dict[str, Any]) -> dict[str, Any]:
    """Return the canonical payload.

    Chapter 5 source is authored directly in explicit standard LaTeX. The
    migration gate is therefore intentionally identity-preserving: raw or
    ambiguous math is rejected instead of being guessed into a new meaning.
    """

    return deepcopy(question)


def migrate(path: Path) -> list[dict[str, Any]]:
    items = json.loads(path.read_text(encoding="utf-8"))
    return [_localized_payload(item) for item in items]


def _audit(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            _audit(item, f"{path}.{key}", errors)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _audit(item, f"{path}[{index}]", errors)
    elif isinstance(value, str):
        for message in audit_text(value):
            errors.append(f"{path}: {message}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="rewrite part files only if canonicalization changes them",
    )
    args = parser.parse_args()

    errors: list[str] = []
    changed = 0
    for path in sorted(PARTS.glob("part_*.json")):
        before = json.loads(path.read_text(encoding="utf-8"))
        after = [_localized_payload(item) for item in before]
        changed += int(before != after)
        _audit(after, path.name, errors)
        if args.write and before != after:
            path.write_text(
                json.dumps(after, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    mode = "rewritten" if args.write else "would change"
    print(f"LaTeX migration audit passed; {changed} part files {mode}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
