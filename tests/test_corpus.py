from copy import deepcopy
import json
from pathlib import Path

from src.corpus import (
    DIFFICULTY_QUOTAS,
    SECTION_QUOTAS,
    TYPE_QUOTAS,
    load_questions,
    validate_questions,
)
from src.source_lineage import (
    CATEGORY_RELATIONS,
    METHOD_FAMILY_REFERENCES,
    SOURCE_LINEAGE_CATEGORIES,
    SOURCE_REFERENCES,
)


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "content" / "questions.json"
SCHEMA = ROOT / "content" / "schema.json"
SOURCES = ROOT / "SOURCES.md"


def test_quota_totals_are_one_hundred() -> None:
    assert SECTION_QUOTAS == {1: 20, 2: 24, 3: 26, 4: 18, 5: 12}
    assert sum(SECTION_QUOTAS.values()) == 100
    assert sum(TYPE_QUOTAS.values()) == 100
    assert sum(DIFFICULTY_QUOTAS.values()) == 100


def test_final_corpus_is_complete_and_valid() -> None:
    assert CORPUS.exists(), "Run scripts/merge_corpus.py after authoring all content parts."
    questions = load_questions(CORPUS)
    assert validate_questions(questions, enforce_quotas=True) == []


def test_every_question_has_verifiable_source_lineage() -> None:
    questions = load_questions(CORPUS)
    assert len(questions) == 100
    assert {item["source_lineage"]["category"] for item in questions} == (
        SOURCE_LINEAGE_CATEGORIES
    )
    for item in questions:
        lineage = item["source_lineage"]
        assert lineage["category"] in SOURCE_LINEAGE_CATEGORIES
        assert lineage["relation"] == CATEGORY_RELATIONS[lineage["category"]]
        assert lineage["method_family"] in METHOD_FAMILY_REFERENCES
        assert lineage["references"]
        assert len(lineage["references"]) == len(set(lineage["references"]))
        assert set(lineage["references"]) <= set(SOURCE_REFERENCES)
        assert set(lineage["references"]) <= METHOD_FAMILY_REFERENCES[lineage["method_family"]]


def test_source_lineage_validation_rejects_false_or_unverifiable_claims() -> None:
    questions = load_questions(CORPUS)

    missing = deepcopy(questions)
    del missing[0]["source_lineage"]
    assert any("missing fields ['source_lineage']" in error for error in validate_questions(missing))

    unknown_reference = deepcopy(questions)
    unknown_reference[0]["source_lineage"]["references"] = ["copyrighted-textbook-unspecified"]
    assert any("unknown source reference" in error for error in validate_questions(unknown_reference))

    inconsistent_relation = deepcopy(questions)
    inconsistent_relation[0]["source_lineage"]["relation"] = (
        "independently_synthesized_from_standard_methods"
    )
    assert any("relation must be" in error for error in validate_questions(inconsistent_relation))


def test_source_lineage_schema_matches_runtime_registry() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    lineage = schema["$defs"]["source_lineage"]["properties"]
    assert set(lineage["category"]["enum"]) == SOURCE_LINEAGE_CATEGORIES
    assert set(lineage["method_family"]["enum"]) == set(METHOD_FAMILY_REFERENCES)
    assert set(lineage["relation"]["enum"]) == set(CATEGORY_RELATIONS.values())
    assert set(lineage["references"]["items"]["enum"]) == set(SOURCE_REFERENCES)


def test_source_registry_is_documented_and_uses_official_open_hosts() -> None:
    documentation = SOURCES.read_text(encoding="utf-8")
    allowed_hosts = ("https://openstax.org/", "https://ocw.mit.edu/")
    for source_id, source in SOURCE_REFERENCES.items():
        assert f"`{source_id}`" in documentation
        assert source["url"].startswith(allowed_hosts)
        assert source["url"] in documentation


def test_formula_migration_golden_cases_preserve_semantics() -> None:
    questions = {item["id"]: item for item in load_questions(CORPUS)}

    assert r"\frac{x}{a}" in questions["Q053"]["en"]["choices"][3]
    assert r"\varphi(a)" in questions["Q054"]["zh"]["solution"]["steps"][0]
    assert r"\varphi([\alpha,\beta])" in questions["Q060"]["en"]["prompt"]
    assert questions["Q062"]["en"]["answer"] == "True."
    assert r"\frac{a^3}{3}" in questions["Q066"]["en"]["answer"]
    assert r"|x|e^{x^2}" in questions["Q067"]["en"]["prompt"]
    assert r"e-1" in questions["Q067"]["en"]["answer"]
    assert r"\operatorname{PV}" in questions["Q075"]["zh"]["answer"]
    assert r"a\le0" in questions["Q077"]["zh"]["answer"]
    assert r"\sqrt{x}" in questions["Q083"]["en"]["prompt"]
    assert r"\frac{f\!\left(\frac{1}{t}\right)}{t^2}" in questions["Q088"]["en"]["prompt"]
    assert r"\frac{|\sin x|}{x}" in questions["Q092"]["en"]["solution"]["steps"][5]
    assert r"\Gamma(s)" in questions["Q093"]["en"]["prompt"]
    assert r"\alpha>0" in questions["Q099"]["en"]["answer"]
    assert r"\frac{\Gamma(a)}{b^a}" in questions["Q100"]["en"]["answer"]

    serialized = json.dumps(list(questions.values()), ensure_ascii=False)
    assert "______" not in serialized
    assert r"\\Sigma" not in serialized
    assert r"\\operatorname{\\operatorname" not in serialized


def test_every_choice_option_and_answer_key_matches_the_math_audit() -> None:
    questions = {item["id"]: item for item in load_questions(CORPUS)}
    expected_keys = {
        "Q001": {"B"},
        "Q002": {"C"},
        "Q003": {"A"},
        "Q004": {"D"},
        "Q005": {"A", "C", "D"},
        "Q006": {"A", "B", "D"},
        "Q021": {"C"},
        "Q022": {"B"},
        "Q023": {"A"},
        "Q024": {"D"},
        "Q025": {"A", "B", "D"},
        "Q026": {"A", "B", "D"},
        "Q052": {"B"},
        "Q053": {"A", "B", "D"},
        "Q058": {"C"},
        "Q061": {"A", "C", "D"},
    }
    choice_items = {
        item_id: item
        for item_id, item in questions.items()
        if item["type"] in {"single_choice", "multiple_choice"}
    }
    assert set(choice_items) == set(expected_keys)

    for item_id, item in choice_items.items():
        for language in ("zh", "en"):
            choices = item[language]["choices"]
            assert len(choices) == 4
            assert all(
                choice.startswith(f"{label}. ")
                for label, choice in zip("ABCD", choices, strict=True)
            )
            recorded_key = {
                letter for letter in "ABCD" if letter in item[language]["answer"]
            }
            assert recorded_key == expected_keys[item_id]


def test_parameter_sign_and_endpoint_hypotheses_are_explicit() -> None:
    questions = {item["id"]: item for item in load_questions(CORPUS)}

    for language, integrable in (("zh", "可积"), ("en", "integrable")):
        assert integrable in questions["Q004"][language]["prompt"]
        assert integrable in questions["Q016"][language]["prompt"]
        assert integrable in questions["Q090"][language]["prompt"]

    parameter_contracts = {
        "Q066": (r"a>0", r"\frac{a^3}{3}"),
        "Q071": (r"p>1", None),
        "Q077": (r"a", r"a>0"),
        "Q085": (r"a>0", r"\frac{\pi}{4a}"),
        "Q089": (r"p", r"p<1"),
        "Q091": (r"p", r"p>1"),
        "Q093": (r"s", r"s>0"),
        "Q098": (r"a>0", r"\frac{m!}{a^{m+1}}"),
        "Q099": (r"\alpha,\beta", r"\alpha>0"),
        "Q100": (r"a,b", r"a>0"),
    }
    for item_id, (prompt_token, answer_token) in parameter_contracts.items():
        for language in ("zh", "en"):
            assert prompt_token in questions[item_id][language]["prompt"]
            if answer_token is not None:
                assert answer_token in questions[item_id][language]["answer"]

    for language in ("zh", "en"):
        assert r"\beta>0" in questions["Q099"][language]["answer"]
        assert r"b>0" in questions["Q100"][language]["answer"]
        assert r"\frac{\Gamma(a)}{b^a}" in questions["Q100"][language]["answer"]


def test_absolute_value_and_principal_value_cases_keep_branch_information() -> None:
    questions = {item["id"]: item for item in load_questions(CORPUS)}

    for language in ("zh", "en"):
        assert r"|x-1|" in questions["Q014"][language]["prompt"]
        assert questions["Q014"][language]["answer"] == r"$\frac52$"
        assert r"\left|\int_a^b f(x)\,dx\right|" in questions["Q019"][language]["prompt"]
        assert r"|x|e^{x^2}" in questions["Q067"][language]["prompt"]
        assert r"e-1" in questions["Q067"][language]["answer"]
        assert r"\operatorname{PV}" in questions["Q075"][language]["answer"]
        assert r"\operatorname{PV}" in questions["Q081"][language]["answer"]
        assert r"(x-1)^2" in questions["Q086"][language]["prompt"]
        assert r"\frac{|\sin x|}{x}" in " ".join(
            questions["Q092"][language]["solution"]["steps"]
        )
