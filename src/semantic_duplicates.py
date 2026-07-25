from __future__ import annotations

from collections import defaultdict
import re
from typing import Any, Iterable


# These formats can ask for the same exact evaluation even when their surface
# instructions differ ("calculate", "fill the blank", or "choose the value").
# Proof, diagnosis, and true/false items may intentionally revisit a theorem
# with a different learning objective, so they are not classified as direct
# evaluation tasks here.
DIRECT_EVALUATION_TYPES = frozenset(
    {
        "single_choice",
        "multiple_choice",
        "fill_blank",
        "calculation",
        "comprehensive",
    }
)

_STYLE_COMMAND = re.compile(
    r"\\(?:displaystyle|textstyle|scriptstyle|scriptscriptstyle|limits)\b"
)
_DELIMITER_SIZE_COMMAND = re.compile(
    r"\\(?:left|right|big|Big|bigg|Bigg)\b"
)
_LATEX_SPACE = re.compile(r"\\(?:,|!|;|:|quad\b|qquad\b)")
_DIFFERENTIAL_D = re.compile(
    r"\\(?:mathrm|operatorname|text)\{d\}|\\rm\s+d\b"
)
_ANSWER_BLANK = re.compile(r"=\\underline\{.*\}\s*$")
_SINGLE_SCRIPT_GROUP = re.compile(r"([_^])\{([A-Za-z0-9])\}")


def _math_segments(text: str) -> Iterable[str]:
    """Yield explicitly delimited inline-math segments from validated text."""

    pieces = text.split("$")
    if len(pieces) % 2 == 0:
        return
    yield from pieces[1::2]


def canonical_integral_signature(formula: str) -> str | None:
    """Return a notation-insensitive signature for an integral expression.

    This deliberately fingerprints the mathematical expression rather than the
    surrounding natural-language prompt. It ignores display/style commands,
    LaTeX spacing, harmless single-token brace variants, differential ``d``
    typography, a leading name such as ``I(a)=``, and a trailing answer blank.
    It is not intended to prove symbolic equivalence between arbitrary
    integrands; it catches repeated evaluation tasks written with routine TeX
    variations.
    """

    value = _STYLE_COMMAND.sub("", formula)
    value = value.replace(r"\dfrac", r"\frac").replace(r"\tfrac", r"\frac")
    value = _DELIMITER_SIZE_COMMAND.sub("", value)
    value = _LATEX_SPACE.sub("", value)
    value = _DIFFERENTIAL_D.sub("d", value)
    value = value.replace(r"\cdot", "")
    value = re.sub(r"\s+", "", value)
    value = _ANSWER_BLANK.sub("", value)

    integral_start = value.find(r"\int")
    if integral_start < 0:
        return None
    value = value[integral_start:]

    previous = None
    while value != previous:
        previous = value
        value = _SINGLE_SCRIPT_GROUP.sub(r"\1\2", value)
    return value.rstrip(".,;，。；")


def evaluation_signature(
    item: dict[str, Any],
    *,
    language: str = "en",
) -> str | None:
    """Return the direct-evaluation signature for one localized question."""

    if item.get("type") not in DIRECT_EVALUATION_TYPES:
        return None
    localized = item.get(language)
    if not isinstance(localized, dict):
        return None
    prompt = localized.get("prompt")
    if not isinstance(prompt, str):
        return None

    signatures = [
        signature
        for segment in _math_segments(prompt)
        if (signature := canonical_integral_signature(segment)) is not None
    ]
    if not signatures:
        return None
    return " || ".join(signatures)


def semantic_duplicate_groups(
    items: Iterable[dict[str, Any]],
    *,
    language: str = "en",
) -> list[tuple[str, ...]]:
    """Return sorted ID groups that repeat one direct-evaluation task."""

    by_signature: defaultdict[str, list[str]] = defaultdict(list)
    for item in items:
        signature = evaluation_signature(item, language=language)
        if signature is not None:
            by_signature[signature].append(str(item.get("id", "")))

    groups = [
        tuple(sorted(item_ids))
        for item_ids in by_signature.values()
        if len(item_ids) > 1
    ]
    return sorted(groups)
