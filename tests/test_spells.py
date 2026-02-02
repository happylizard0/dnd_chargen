import pytest

from data.spells import ALL_SPELLS, SPELLS_BY_LEVEL


def test_spells_by_level_all_defined():
    missing = []
    for cls, level_map in SPELLS_BY_LEVEL.items():
        for lvl, spells in level_map.items():
            for s in spells:
                if s not in ALL_SPELLS:
                    missing.append((cls, lvl, s))
    if missing:
        missing_lines = "\n".join(f"{c} lvl {l}: {s}" for c, l, s in missing)
        pytest.fail(f"Some spells referenced by SPELLS_BY_LEVEL are missing from ALL_SPELLS:\n{missing_lines}")
