import re


def test_no_adjacent_string_literals_in_biographer():
    """Detect accidental adjacent string literals (missing commas) in `engine/biographer.py`.
    This is a heuristic: it searches for two string literals adjacent (possibly across lines) without a comma in between.
    """
    path = "engine/biographer.py"
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()

    # Match two string literals adjacent with optional whitespace/newline but no comma between
    pattern = re.compile(r'(?:(?:"[^"]*"|\'[^\']*\'))\s*(?:\n\s*)?(?:"[^"]*"|\'[^\']*\')')
    matches = pattern.findall(txt)
    assert not matches, f"Found adjacent string literals (possible missing commas) in {path}: {matches}"
