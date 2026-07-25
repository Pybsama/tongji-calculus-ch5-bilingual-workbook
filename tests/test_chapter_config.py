from src.chapter_config import (
    CHAPTER_NUMBER,
    CHAPTER_TITLES,
    OUTPUT_FILENAMES,
    SECTION_INFO,
    SECTION_QUOTAS,
)


def test_chapter_configuration_is_complete() -> None:
    assert CHAPTER_NUMBER == 5
    assert set(CHAPTER_TITLES) == {"zh", "en"}
    assert set(SECTION_INFO) == set(SECTION_QUOTAS)
    assert SECTION_QUOTAS == {1: 20, 2: 24, 3: 26, 4: 18, 5: 12}
    assert sum(SECTION_QUOTAS.values()) == 100
    assert set(OUTPUT_FILENAMES) == {
        ("zh", "exercises"),
        ("zh", "solutions"),
        ("en", "exercises"),
        ("en", "solutions"),
    }
    assert all("5" in name or "第五章" in name for name in OUTPUT_FILENAMES.values())
