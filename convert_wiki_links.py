import os
import re
from pathlib import Path

root = Path('Physics Note')
figure_root = Path('Physics Note Figures')
docs = [
    Path('docs/Condensed Matter Physics.md'),
    Path('docs/Modern Optical and Atomic Physics.md'),
    Path('docs/Quantum Mechanics.md'),
    Path('docs/Thermal Physics.md'),
    Path('docs/Nuclear and Particle Physics.md'),
]

# build file index
files = list(root.rglob('*.md'))
index = {}
for path in files:
    key = path.stem.strip().lower()
    index.setdefault(key, []).append(path)

# helper normalization for approximate matching
def normalize(name: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', name.lower())

norm_index = {}
for key, paths in index.items():
    norm = normalize(key)
    norm_index.setdefault(norm, []).extend(paths)

pattern = re.compile(r'(!)?\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]')

for doc in docs:
    if not doc.exists():
        print(f'Missing doc: {doc}')
        continue
    text = doc.read_text(encoding='utf-8')
    changed = 0
    missing = []

    def replace(match):
        is_image = bool(match.group(1))
        target = match.group(2).strip()
        label = match.group(3)
        label_text = label.strip() if label else target
        # direct path if includes slash
        if '/' in target:
            target_path = root / (target + ('' if target.endswith('.md') else '.md'))
            if target_path.exists():
                rel = os.path.relpath(target_path, start=doc.parent).replace('\\', '/')
                return f'![' + label_text + '](' + rel + ')' if is_image else f'[{label_text}]({rel})'
        # image file search in figures folder
        if is_image and re.search(r'\.(png|jpe?g|gif|svg)$', target, re.IGNORECASE):
            img_path = figure_root / target
            if img_path.exists():
                rel = os.path.relpath(img_path, start=doc.parent).replace('\\', '/')
                return f'![' + label_text + '](' + rel + ')'
        # exact file stem match
        key = target.strip().lower()
        if key in index:
            target_path = index[key][0]
            rel = os.path.relpath(target_path, start=doc.parent).replace('\\', '/')
            return f'![' + label_text + '](' + rel + ')' if is_image else f'[{label_text}]({rel})'
        # normalized match
        norm = normalize(target)
        if norm in norm_index:
            target_path = norm_index[norm][0]
            rel = os.path.relpath(target_path, start=doc.parent).replace('\\', '/')
            return f'![' + label_text + '](' + rel + ')' if is_image else f'[{label_text}]({rel})'
        missing.append(target)
        return match.group(0)

    new_text = pattern.sub(replace, text)
    if new_text != text:
        doc.write_text(new_text, encoding='utf-8')
    # report
    print(f'Updated {doc}: {sum(1 for _ in pattern.finditer(text)) - sum(1 for _ in pattern.finditer(new_text))} replacements, {len(missing)} missing')
    if missing:
        print('Missing targets:')
        for m in sorted(set(missing)):
            print('  ', m)
    print('---')
