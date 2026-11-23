import os
import re

chapters_dir = "/home/user/supergirl-adrian-vale/chapters"

# DBZ Twin aphorism rule: at most 1 "ordinary is" line per chapter
# The narrative block appears in 17 chapters verbatim - keep only in Ch2
narrative_aphorism_full = """Kara and Adrian had learned since the roof in November, since the sun that ordinary is choice. Adrian had learned under red sun that red sun can harm temperament and emotional stability. His parents were murdered because of a mixed union. He destroyed a city in his rage. He was caught when he was exhausted. He built the seal himself to be ordinary."""

narrative_aphorism_ch26 = """Kara and Adrian had learned since the roof in November since sun that ordinary is choice. Adrian had learned under red sun that red sun can harm temperament and emotional stability. His parents were murdered because of a mixed union. He destroyed a city in his rage. He was caught when he was exhausted. He built the seal himself to be ordinary."""

# Dialogue aphorisms - keep at most 1 per chapter
aphorism_variants = [
    "That is... that is ordinary. That is what ordinary is. Learning, every day, choosing, every day.",
    "That is... that is what ordinary is. Learning, every day, choosing, every day.",
    "That is... that is what ordinary is. Trying. Every day. Choosing. Every day.",
    "That is what ordinary is. Learning. Every day. Choosing. Every day.",
]

# Replacement: concrete action instead of aphorism
# Each chapter gets a context-appropriate replacement based on the speaker
def get_replacement(speaker, chapter_num):
    """Return a concrete action replacement for the aphorism."""
    replacements = {
        "Adrian": "Adrian put his mug down and pointed at the counter. \"Finish that, and the report goes to CatCo before five.\"",
        "Alex": "Alex tapped the console. \"Two calls. Five minutes each. Then you're off.\"",
    }
    return replacements.get(speaker, "He put his mug down. \"Finish that, and the report goes in before five.\"")

def process_chapter(filepath, chapter_num):
    with open(filepath, 'r') as f:
        text = f.read()
    
    orig_len = len(text)
    changes = []
    
    # Step 1: Narrative aphorism - keep only in Ch2
    for variant in [narrative_aphorism_full, narrative_aphorism_ch26]:
        if chapter_num != 2 and variant in text:
            # Replace with brief factual statement
            short = "Kara and Adrian had learned since the roof in November. Adrian had learned under red sun that red sun can harm temperament and emotional stability. His parents were murdered because of a mixed union. He destroyed a city in his rage. He was caught when he was exhausted. He built the seal himself to be ordinary."
            text = text.replace(variant, short)
            changes.append(f"  Narrative aphorism shortened")
    
    # Step 2: Dialogue aphorisms - keep at most 1 per chapter
    aphorism_count = 0
    for variant in aphorism_variants:
        # Find all occurrences
        while variant in text:
            if aphorism_count >= 1:
                # Replace with concrete action - find the speaker from context
                # Look backwards from the aphorism position for "He said" or "Adrian said" etc.
                idx = text.index(variant)
                before = text[:idx]
                # Find the speaker
                speaker = "He"
                for sp in ["Adrian said", "Alex said", "J'onn said", "She said"]:
                    if sp in before[-200:]:
                        speaker = sp.split(" said")[0]
                        break
                
                replacement = get_replacement(speaker, chapter_num)
                text = text[:idx] + replacement + text[idx+len(variant):]
                changes.append(f"  Dialogue aphorism replaced ({aphorism_count+1})")
            else:
                aphorism_count += 1
                # Keep this one, move to next variant
                break
    
    # Step 3: Fix "ordinary is" in narrative (non-dialogue) - reduce to at most 1
    # Find standalone "ordinary is" lines in narrative (not in quotes)
    lines = text.split('\n')
    narrative_ordinary_count = 0
    new_lines = []
    for line in lines:
        if "ordinary is" in line and '"' not in line:
            narrative_ordinary_count += 1
            if narrative_ordinary_count >= 2:
                # Replace with concrete action
                new_lines.append("He did not answer. He turned the page and kept reading.")
                changes.append(f"  Narrative 'ordinary is' replaced")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    text = '\n'.join(new_lines)
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(text)
    
    new_len = len(text)
    diff = new_len - orig_len
    print(f"Chapter {chapter_num}: {orig_len} -> {new_len} ({diff:+d})")
    for c in changes:
        print(c)
    if not changes:
        print("  No changes")
    print()

# Process all 26 chapters
for i in range(1, 27):
    fname = f"Chapter_{i:02d}_"
    for fn in os.listdir(chapters_dir):
        if fn.startswith(fname) and fn.endswith('.md'):
            filepath = os.path.join(chapters_dir, fn)
            process_chapter(filepath, i)
            break

print("=== ASPHORISM SWEEP COMPLETE ===")
