import re
import sys

path = "engine/biographer.py"
with open(path, "r", encoding="utf-8") as f:
    txt = f.read()

pattern = re.compile(r'(?:(?:"[^"]*"|\'[^\']*\'))\s*(?:\n\s*)?(?:"[^"]*"|\'[^\']*\')')
found = list(pattern.finditer(txt))
problem_matches = []
for m in found:
    # determine whether there's a comma between the end of the first literal and the start of the second
    # locate the closing quote of the first literal within the match
    inner = m.group(0)
    # find the first occurrence of the close-quote of the first literal (either '"' or "'")
    # We can search for the pattern: quote, then characters, then quote
    quote_match = re.match(r'(?:"[^"]*"|\'[^\']*\')', inner)
    if not quote_match:
        continue
    end_of_first = quote_match.end()
    between = inner[end_of_first:]
    # if a comma exists in 'between' (before the next opening quote) then it's properly separated
    if ',' not in between:
        problem_matches.append((m.span(), m.group(0), inner))

if problem_matches:
    print('Found suspicious adjacent string-literal matches (missing comma between literals):')
    for span, raw, inner in problem_matches:
        start, end = span
        snippet = txt[max(0, start-80):min(len(txt), end+80)]
        print('-' * 60)
        print('MATCH TEXT:')
        print(repr(raw))
        print('\nCONTEXT:')
        print(snippet)
        prefix = txt[:start]
        line_no = prefix.count('\n') + 1
        print('\nLines around match:')
        print(f'Line ~{line_no}')
    sys.exit(1)
print('OK: no adjacent string literals detected in engine/biographer.py')
