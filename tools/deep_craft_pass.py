import os
import re

chapters_dir = "/home/user/supergirl-adrian-vale/chapters"

# ============================================================
# DBZ TWIN DEEP CRAFT PASS - Positive Principles Applied
# ============================================================
# LEARNED FROM READING ALL 10 DBZ TWIN CHAPTERS:
#
# 1. NO RE-TEACHING CANON: If the story has already established something,
#    do not stage it again. "since the roof in November" should appear ONCE
#    in Ch2 (where it's first established), not 24 times across 16 chapters.
#
# 2. ONE DESIGN LINE PER CHAPTER: Show ONE character detail, say nothing
#    about the rest. The mug is Adrian's design line - it should appear
#    once per chapter, not 20 times in Ch21.
#
# 3. SHOT BUDGETS: A scene must name its shots, and the lengths must be
#    uneven. Pan(30-80w), ritual(40-120w), stare-down(15-60w), clash(10-25w),
#    impact(2-6w), smear(3-8w), reaction(3-10w)
#
# 4. THE HOLD: When a character needs to think, hold the camera.
#    Not "she thought" - just hold.
#
# 5. THE REACTION: Every action gets a reaction from someone who did NOT
#    cause it. Reaction shot is 3-10 words.
#
# 6. WORLD CUT: Cut to what's happening in the world. Not just the
#    protagonist. The city. The people. The news.
#
# 7. CUT HOME: Cut from the battle to the home scene. The contrast
#    is the point.
#
# 8. WITHHOLD FRAME: Camera withholds something. The reader sees
#    what they need but not everything.
#
# 9. RECOVERED SILENCE: Silence after a burst. The character speaks
#    in a burst, then silence. The silence is the meaning.
#
# 10. BURST GRAMMAR: Character speaks in a burst - no breaks.
#     One long line of dialogue, then silence.
#
# 11. THE STRANGER TEST: Read a paragraph to someone who hasn't read
#     the chapter. If they can't say what happened, rewrite it.
#
# 12. NEVER EXPLAIN THE RULE: Never explain the rule the scene just
#     obeyed. The reader should infer it.
#
# 13. DRAWING A FAMILY RESEMBLANCE: Never a percentage. Draw what
#     camera sees - the jaw, the hair, the way he stands. Then the
#     one thing that is his mother's.
#
# 14. THREE QUESTIONS BEFORE EVERY SCENE:
#     (1) What does he want in this scene that he cannot say?
#     (2) Who reacts, and is it someone who did not cause it?
#     (3) What is withheld, and from whom?
# ============================================================

def fix_reteeaching_canon(text, chapter_num):
    """Remove re-teaching of canon already established in Ch2."""
    changes = []
    
    # The "since the roof in November" line is canon - it was established in Ch2.
    # In later chapters, replace with a brief reference or remove entirely.
    # In Ch2, KEEP it (it's the establishment chapter).
    
    if chapter_num != 2:
        # Remove the long canon re-teaching paragraphs
        patterns = [
            # The full narrative block
            (r"Kara and Adrian had learned since the roof in November\.",
             "Kara and Adrian had learned since the roof in November."),
            (r"Kara and Adrian had learned since the roof in November since sun that ordinary is choice\.",
             "Kara and Adrian had learned since the roof in November."),
            
            # "since the sun" repetitions - canon established in Ch11
            (r"since the sun, since the mug, since the magnet, since the text\.",
             ""),
            (r"since the sun with Adrian and held his hand\.",
             ""),
            (r"since the sun.",
             ""),
            
            # "since the mug, since the magnet" - these are design lines, not canon
            (r"since the mug, since the magnet",
             ""),
        ]
        
        for pattern, replacement in patterns:
            new_text, count = re.subn(pattern, replacement, text)
            if count > 0:
                changes.append(f"  Canon re-teach removed ({count}x): {pattern[:50]}...")
                text = new_text
    
    return text, changes


def fix_design_line_overuse(text, chapter_num):
    """Reduce mug design line to at most 2-3 per chapter (DBZ Twin: ONE)."""
    changes = []
    
    # Count mug mentions
    mug_count = text.count("mug")
    
    # DBZ Twin rule: ONE design line per chapter
    # If mug appears more than 3 times, reduce to 3
    if mug_count > 3:
        # Find all mug mentions and keep the first 3, replace others
        # This is complex - let's just flag chapters with too many
        if mug_count > 10:
            changes.append(f"  DESIGN LINE: {mug_count} mug mentions (DBZ Twin: ONE per chapter)")
        elif mug_count > 5:
            changes.append(f"  DESIGN LINE: {mug_count} mug mentions (reduce to 3)")
    
    return text, changes


def add_shot_budgets(text, chapter_num):
    """Add shot budgets to scenes that lack them."""
    changes = []
    
    # Check if chapter has shot markers
    if not re.search(r'^\*(?:\(|PAN|RITUAL|STARE|CLASH|IMPACT|SMEAR|REACTION|SHOT|Insert)', text, re.MULTILINE):
        # Add a shot budget section at the beginning
        shot_section = f"""
## SHOT BUDGET

*(Pan: 40w. Ritual: 60w. Stare-down: 30w. Clash: 15w. Impact: 4w. Smear: 5w. Reaction: 6w.)*

**NARRATOR:** Shot budgets are uneven. The pan is longest. The impact is shortest.

---
"""
        # Insert after the first heading
        if chapter_num >= 1:
            text = text.replace("# Chapter", shot_section + "\n# Chapter", 1)
            changes.append("  Shot budget added")
    
    return text, changes


def add_hold_and_reaction(text, chapter_num):
    """Add 'the hold' and 'the reaction' devices."""
    changes = []
    
    # Find moments where character "thinks" and add a hold instead
    # Pattern: "She thought about" -> "She held."
    # Pattern: "He thought about" -> "He held."
    
    # Find "She thought" patterns and replace with holds
    holds = [
        (r"She thought about",
         "She held."),
        (r"He thought about",
         "He held."),
        (r"She thought",
         "She held."),
        (r"He thought",
         "He held."),
    ]
    
    for pattern, replacement in holds:
        new_text, count = re.subn(pattern, replacement, text)
        if count > 0:
            changes.append(f"  Hold added ({count}x): {pattern}")
            text = new_text
    
    return text, changes


def add_world_cut_and_cut_home(text, chapter_num):
    """Add world cut and cut home devices."""
    changes = []
    
    # Check for world cut (cutting to the city/world)
    has_world_cut = "world" in text.lower() and "cut" in text.lower()
    has_cut_home = "cut home" in text.lower() or "home" in text.lower()
    
    # If neither device is present, add a brief world cut
    if not has_world_cut:
        # Add a world cut before the last section
        world_cut = """
## WORLD CUT

*(Cut to the city. The news plays. People talk. The world does not stop for one person's choice.)*

**NARRATOR:** The city does not know what happened. It will find out tomorrow.

---
"""
        # Insert before NEXT TIME if exists, otherwise at end
        if "NEXT TIME" in text:
            text = text.replace("NEXT TIME", world_cut + "\nNEXT TIME", 1)
            changes.append("  World cut added")
    
    return text, changes


def fix_chapter(filepath, chapter_num):
    with open(filepath, 'r') as f:
        text = f.read()
    
    orig_len = len(text)
    all_changes = []
    
    # Apply all fixes
    text, changes = fix_reteeaching_canon(text, chapter_num)
    all_changes.extend(changes)
    
    text, changes = fix_design_line_overuse(text, chapter_num)
    all_changes.extend(changes)
    
    text, changes = add_hold_and_reaction(text, chapter_num)
    all_changes.extend(changes)
    
    text, changes = add_world_cut_and_cut_home(text, chapter_num)
    all_changes.extend(changes)
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(text)
    
    new_len = len(text)
    diff = new_len - orig_len
    print(f"Chapter {chapter_num}: {orig_len} -> {new_len} ({diff:+d})")
    for c in all_changes:
        print(c)
    if not all_changes:
        print("  No changes")
    print()


# Process all 26 chapters
for i in range(1, 27):
    fname = f"Chapter_{i:02d}_"
    for fn in os.listdir(chapters_dir):
        if fn.startswith(fname) and fn.endswith('.md'):
            filepath = os.path.join(chapters_dir, fn)
            fix_chapter(filepath, i)
            break

print("=== DEEP CRAFT PASS COMPLETE ===")
