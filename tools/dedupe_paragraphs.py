#!/usr/bin/env python3
"""Mechanical dedupe: remove paragraphs of >=12 words that repeat exactly
(whitespace-insensitive) within one chapter, keeping the first occurrence.
Does not touch receipts, drafts, checksums, or prose beyond exact repeats.
Same rule as the house dedupe tool applied 2026-10-11 to chapters 9-14."""
import re, sys, hashlib
from pathlib import Path

MIN_WORDS = 12

def para_key(p):
    return re.sub(r'\s+', ' ', p.strip().lower())

def para_words(p):
    return len(p.split())

def process(path):
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    out = []
    seen = {}
    removed = 0
    for line in lines:
        stripped = line.strip()
        if stripped and para_words(stripped) >= MIN_WORDS:
            key = para_key(stripped)
            if key in seen:
                removed += 1
                continue
            seen[key] = True
        out.append(line)
    new = '\n'.join(out)
    if new != text:
        old_hash = hashlib.sha256(text.encode()).hexdigest()[:16]
        new_hash = hashlib.sha256(new.encode()).hexdigest()[:16]
        path.write_text(new, encoding='utf-8')
        print(f"{path.name}: removed {removed} repeated paragraphs | {old_hash} -> {new_hash} | {len(text.split())}w -> {len(new.split())}w")
    else:
        print(f"{path.name}: no exact repeats removed")

def main():
    base = Path('/home/user/supergirl-adrian-vale/chapters')
    for p in sorted(base.glob('Chapter_*.md')):
        process(p)

if __name__ == '__main__':
    main()
