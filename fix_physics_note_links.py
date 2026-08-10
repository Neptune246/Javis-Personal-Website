import os
import re
from pathlib import Path
from urllib.parse import quote

base_dir = Path(__file__).resolve().parent
root = base_dir / 'docs' / 'Physics Note'
figure_root = base_dir / 'docs' / 'Physics Note Figures'

if not root.exists():
    raise SystemExit(f'Missing root folder: {root}')

files = sorted(root.rglob('*.md'))
index = {}
norm_index = {}


def normalize(name: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', name.lower())


for path in files:
    key = path.stem.strip().lower()
    index.setdefault(key, []).append(path)
    norm_index.setdefault(normalize(key), []).append(path)

wiki_pattern = re.compile(r'(!)?\[\[([^\]|#]+?)(?:#([^\]|]+))?(?:\|([^\]]+))?\]\]')
md_link_pattern = re.compile(r'(!?\[[^\]]*\]\()([^\)]+)(\))')
image_ext_guard = re.compile(r'\.(png|jpe?g|gif|svg|bmp|webp)$', re.IGNORECASE)

all_missing = {}

for doc in files:
    text = doc.read_text(encoding='utf-8')
    missing = []
    replacements = [0]

    def replace_wiki(match):
        is_image = bool(match.group(1))
        target = match.group(2).strip()
        anchor = match.group(3)
        label = match.group(4)
        label_text = label.strip() if label else target

        for prefix in ('docs/Physics Note/', 'Physics Note/', '../Physics Note/', './Physics Note/'):
            if target.startswith(prefix):
                target = target[len(prefix):].lstrip('/')
                break

        if is_image and image_ext_guard.search(target):
            img_path = figure_root / target
            if img_path.exists():
                rel = Path(os.path.relpath(img_path, start=doc.parent)).as_posix()
                rel = '/'.join(quote(part, safe='') for part in rel.split('/'))
                replacements[0] += 1
                return f'![{label_text}]({rel})'

        if '/' in target:
            candidate = root / target
            if candidate.exists():
                if candidate.is_dir():
                    candidate = candidate / 'index.md'
                if candidate.exists():
                    if not candidate.suffix:
                        candidate = candidate.with_suffix('.md')
                    rel = Path(os.path.relpath(candidate, start=doc.parent)).as_posix()
                    if anchor:
                        rel = f'{rel}#{anchor}'
                    replacements[0] += 1
                    return f'![{label_text}]({rel})' if is_image else f'[{label_text}]({rel})'
            candidate_with_ext = candidate.with_suffix('.md')
            if candidate_with_ext.exists():
                rel = Path(os.path.relpath(candidate_with_ext, start=doc.parent)).as_posix()
                if anchor:
                    rel = f'{rel}#{anchor}'
                replacements[0] += 1
                return f'![{label_text}]({rel})' if is_image else f'[{label_text}]({rel})'

        if is_image and image_ext_guard.search(target):
            img_path = figure_root / target
            if img_path.exists():
                rel = Path(os.path.relpath(img_path, start=doc.parent)).as_posix()
                rel = '/'.join(quote(part, safe='') for part in rel.split('/'))
                replacements[0] += 1
                return f'![{label_text}]({rel})'

        key = target.strip().lower()
        candidate = None
        if key in index:
            candidate = index[key][0]
        else:
            norm = normalize(target)
            if norm in norm_index:
                candidate = norm_index[norm][0]

        if candidate and candidate.exists():
            rel = Path(os.path.relpath(candidate, start=doc.parent)).as_posix()
            if anchor:
                rel = f'{rel}#{anchor}'
            replacements[0] += 1
            return f'![{label_text}]({rel})' if is_image else f'[{label_text}]({rel})'

        missing.append(target)
        return match.group(0)

    def replace_md_link(match):
        prefix, target, suffix = match.groups()
        target = target.strip()
        if target.startswith(('http://', 'https://', 'mailto:', '#', 'data:')):
            return match.group(0)

        if 'Physics Note Figures/' in target:
            target_path = target.split('Physics Note Figures/', 1)[1]
            img_path = figure_root / target_path
            if img_path.exists():
                rel = Path(os.path.relpath(img_path, start=doc.parent)).as_posix()
                rel = '/'.join(quote(part, safe='') for part in rel.split('/'))
                replacements[0] += 1
                return f'{prefix}{rel}{suffix}'

        return match.group(0)

    text = wiki_pattern.sub(replace_wiki, text)
    text = md_link_pattern.sub(replace_md_link, text)

    if text != doc.read_text(encoding='utf-8'):
        doc.write_text(text, encoding='utf-8')

    if missing or replacements[0]:
        all_missing[str(doc.relative_to(root))] = {
            'replacements': replacements[0],
            'missing': sorted(set(missing)),
        }

for path, info in all_missing.items():
    print(f'{path}: {info["replacements"]} replacements, {len(info["missing"])} missing')
    if info['missing']:
        print('  Missing targets:')
        for m in info['missing']:
            print('   ', m)
        print()

print('Done. Processed', len(files), 'Physics Note files.')
