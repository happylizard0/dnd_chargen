![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success)


# D&D Character Generator 

A lightweight, extensible Dungeons & Dragons (5e-inspired) character generator with a friendly CLI and a modular engine for building, leveling, and inspecting characters. This repository focuses on deterministic rules logic, clear data structures, and flavorful backstory generation.

---

## Known Limitations

- Backstory content is still stored in Python dictionaries
- Spell data is incomplete for some classes/levels
- No GUI or web interface yet


## Quick Start

Requirements
- Python 3.10+ (3.11+ recommended)
- Optional dev tools: `pytest`, `black`, `ruff`, `mypy`

Setup (Windows example)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip
# Install basic dev tools (recommended)
pip install pytest black ruff mypy
```

Run the CLI
```powershell
python -m main
```

Interact with the menu to create new characters, load/level, or view characters.

---

## Key Features

- CLI-driven character creation and leveling (`cli_utils.py`) 
- Clear, typed `Character` dataclass and model (`engine/models.py`) 
- Rules engine implementing PHB-style mechanics (`engine/rules.py`) 
- Spell initialization and slot progression (`data/constants.py`, `engine/builder.py`) 
- Flavorful backstory generator with race/class/background flair (`engine/biographer.py`) 
- Simple JSON persistence for saved characters (`data/persist.py`) 
- Unit tests for core spellcasting behavior (`tests/test_spellcasting.py`) 

---

## Notable Fixes & Current State

- Fixed silent bug where adjacent string literals in `biographer.py` were inadvertently concatenated (missing commas). ✅
- The main menu now correctly routes the **View Character** option to `cli_view_character`. ✅

If you find other content issues or formatting problems in the large `biographer` flair blocks, consider moving them into a JSON/YAML file for easier editing and automated content QA.

---

## Developer Guide

Project layout (top-level):
```
.dnd_Chargen/
  main.py                # CLI entry-point
  cli_utils.py           # CLI helpers and menus
  engine/
    builder.py           # Build/level characters
    biographer.py        # Backstory generator (large flair dictionaries)
    models.py            # Character dataclass
    rules.py             # Rules logic (hp, mods, slots)
  data/
    constants.py         # RACES, CLASSES, BACKGROUNDS, SPELL_SLOT_PROGRESSIONS
    persist.py           # Read/write character JSON
    spells/               # Organized lists of spells by class/level
  tests/                 # Unit tests (pytest)
```

Coding and testing recommendations
- Keep business logic in `engine/`; keep content data in `data/`.
- When editing large content blocks (`biographer.py`), run quick import tests and add content tests to guard against accidental concatenation or syntactic errors.
- Use `pytest` for test suites. Example: `python -m pytest -q`

Make randomness deterministic for tests
- Many functions use Python's `random`. To make unit tests deterministic, either set a seed in tests (`random.seed(0)`) or modify the functions to accept an injectable RNG object.

---

## Tests & CI

Run tests locally
```powershell
python -m pytest -q
```

Suggested CI (GitHub Actions)
- Run `pytest`, `ruff`/`flake8`, `mypy`, and `black --check` on PRs.
- Add a content QA job that checks for accidental concatenated strings in `biographer.py` (regex-based check).

---

## Roadmap & Improvements

Short-term improvements
- Add unit tests for `engine/biographer.py` to ensure lists are well-formed and content entries appear as expected.
- Extract flavor dictionaries (race/class/background flair) into `data/backstories.json` (or YAML) and load them via a small loader to improve editability.

Medium-term
- Add `pre-commit` hooks for formatting and linting (`black`, `ruff`) and a `pyproject.toml`.
- Expand spell data and integrate more levels into the builder's known/prepared/slot logic.

Long-term
- Add a small web interface or TUI for content authoring and character previews.
- Add comprehensive integration tests (build many characters and assert invariants across the rules engine).

---

## Contributing

Contributions are welcome. Please follow these guidelines:
1. Fork and branch
2. Add or update tests for any new logic or content changes
3. Run `black .` and `ruff .` before committing
4. Open a PR and describe the change concisely

---

## Example: Generate a quick backstory in Python
```py
from types import SimpleNamespace
from engine import biographer

char = SimpleNamespace(char_class='Wizard', race='Human', alignment='True Neutral', background='Acolyte')
print(biographer.generate_backstory(char))
```

Tip: If you need testable output, seed `random` or add an RNG parameter to `generate_backstory`.

---

## License

This project is open source — defaulting to the MIT License. Add a `LICENSE` file if you plan to publish this project publicly.

---

SUPPORT YOUR FLGS!