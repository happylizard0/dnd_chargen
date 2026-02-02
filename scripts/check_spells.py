import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.spells import ALL_SPELLS, SPELLS_BY_LEVEL

missing = []
for cls, level_map in SPELLS_BY_LEVEL.items():
    for lvl, spells in level_map.items():
        for s in spells:
            if s not in ALL_SPELLS:
                missing.append((cls, lvl, s))

if missing:
    print('MISSING:')
    for m in missing:
        print(f"{m[0]} lvl {m[1]}: {m[2]}")
else:
    print('OK: all referenced spells are defined in ALL_SPELLS')
