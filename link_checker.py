from pathlib import Path
import re

root = Path('.').resolve()
docs_root = root / 'docs'
md_files = sorted(docs_root.rglob('*.md'))
link_re = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
exclude_prefixes = ('http://', 'https://', 'mailto:', '#', 'javascript:')

broken = []
all_links = 0
for md in md_files:
    text = md.read_text(encoding='utf-8', errors='ignore')
    for match in link_re.finditer(text):
        target = match.group(1).strip()
        all_links += 1
        if any(target.startswith(pref) for pref in exclude_prefixes):
            continue
        if target.startswith('#'):
            continue
        target_file = target.split('#', 1)[0] if '#' in target else target
        if not target_file:
            continue
        if target_file.startswith('/'):
            broken.append((md.relative_to(root), target, 'absolute path'))
            continue
        target_path = (md.parent / target_file).resolve()
        if docs_root not in target_path.parents and target_path != docs_root:
            broken.append((md.relative_to(root), target, 'outside docs'))
            continue
        if target_path.is_dir():
            if not (target_path / 'index.md').exists():
                broken.append((md.relative_to(root), target, 'dir without index'))
            continue
        if not target_path.exists():
            broken.append((md.relative_to(root), target, 'missing file'))

print(f'Total markdown files: {len(md_files)}')
print(f'Total links checked: {all_links}')
print(f'Broken links found: {len(broken)}')
for md, target, reason in broken:
    print(f'{md}: {target} -> {reason}')
