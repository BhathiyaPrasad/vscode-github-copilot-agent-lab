#!/usr/bin/env python3
"""Idempotent script to insert dracula.css link into app/templates/base.html
Run from the project root.
"""
from pathlib import Path
p = Path('app/templates/base.html')
if not p.exists():
    print(f"Error: {p} not found")
    raise SystemExit(1)
text = p.read_text(encoding='utf-8')
link = "<link rel=\"stylesheet\" href=\"{{ url_for('static', path='css/dracula.css') }}\">"
if link in text:
    print('dracula.css already linked in base.html')
    raise SystemExit(0)
anchor = "<link rel=\"stylesheet\" href=\"{{ url_for('static', path='css/app.css') }}\">"
if anchor in text:
    new = text.replace(anchor, anchor + "\n    " + link)
    p.write_text(new, encoding='utf-8')
    print('Inserted dracula.css link into base.html')
else:
    print('Could not find app.css link anchor in base.html; aborting')
    raise SystemExit(2)
