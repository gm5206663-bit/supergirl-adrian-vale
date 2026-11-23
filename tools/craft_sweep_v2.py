import os
import re

chapters_dir = "/home/user/supergirl-adrian-vale/chapters"

# ============================================================
# DBZ TWIN CRAFT PRINCIPLES (learned from reading actual chapters):
# ============================================================
# 1. NO INTERIORITY: narrator describes what camera sees, never what character thinks
#    "she felt" -> show the action
#    "she thought" -> cut, just state the fact
#    "she realized" -> cut
#    "she knew" -> state the fact without "she knew"
#
# 2. NO EPITHETS: use the name, not "the man in black"
#    In narration: "Wraith" or "Adrian" not "the man in black"
#    (Media labels like "the man in black" are fine when media is speaking)
#
# 3. NO APHORISMS: at most 1 "ordinary is" line per chapter (already done)
#
# 4. EPISODE GRAMMAR: cold open, title card, narrator, hard cuts, eye-catch, preview
# ============================================================

def fix_interiority(text, chapter_num):
    """Fix interiority violations - replace thought markers with external camera actions."""
    changes = []
    
    # Pattern: "she felt" -> show the action
    replacements = [
        # Ch1
        (r"For a frightening moment she thought she had made it worse\.",
         "The plane pulled left. The correction did not take."),
        # Ch2
        (r"For the first time since Alex had left her apartment, the thought of doing this again did not feel like an argument she would have to have alone\.",
         "Kara picked up her phone. She dialed."),
        (r"For a moment she thought of the date she had told him about that morning\. Then she saw that he was holding his tablet without looking at it\.",
         "Kara looked at the tablet. He was not reading it."),
        # Ch6
        (r"Kara had more questions than she could arrange into words\. Some came from the frightened child who had lost a world; others came from the adult who had thought she knew the person sitting opposite her\. And",
         "Kara had more questions than she could arrange into words. And"),
        # Ch7
        (r"He had first seen the woman on the television as an event taking place far away, something to understand and arrange coverage for\. Now he was looking at a person he knew\.",
         "He had first seen her on television. Now he was looking at a person he knew."),
        # Ch14
        (r"He had been watching Supergirl's associates, and now he knew which one was closest to her\.",
         "He had been watching Supergirl's associates. Now he had the answer."),
        # Ch16
        (r"because he knew Kara is with Adrian and he still loves her and he bottles it\.",
         "because he knew Kara is with Adrian. He bottles it."),
        (r"because he knew Kara is with Adrian and Adrian is with Kara and that makes him bottle more, which is why he is time bomb\.",
         "because he knew Kara is with Adrian and Adrian is with Kara. He bottles more."),
        # Ch17
        (r"and she thought about how some traps are not meant to kill you but to make you feel stupid, and how Winn must have felt growing up with a father who made toys that were also traps, who made love that was also trap\.",
         ""),
        (r"because she had kissed Adrian on the roof in November cold and she knew what choosing meant and what being chosen meant\.",
         "because she had kissed Adrian on the roof in November cold."),
        (r"because fathers know where their sons go when they are sad, because he had followed Winn from CatCo and he knew Kara's address because he had been watching, because he had seen Winn leave Kara's apartment with red eyes and had thought good, son is sad, son will need father\.",
         "because fathers know where their sons go when they are sad, because he had followed Winn from CatCo and he knew Kara's address because he had been watching, because he had seen Winn leave Kara's apartment with red eyes."),
        (r"He thought about texting Kara\. He thought about texting Adrian sorry\. He thought about calling Agent Chase\. He thought about being brave, and then he thought about being his father's son, and about being friend who kissed friend's girlfriend, and about being guy in the chair who is not just guy in the chair, and he put the gun in his jacket because he wanted to prove he was not his father and he wanted to prove he was worthy of Kara and Adrian's friendship and he wanted to prove he could not be like father who bottled then exploded\.",
         "He thought about texting Kara. He thought about texting Adrian sorry. He thought about calling Agent Chase. He put the gun in his jacket."),
        (r"Winn had not texted Kara\. He had not texted Adrian sorry yet\. He had not called the FBI\. He thought, stupidly, that he could handle it alone, because he was his father's son and he wanted to prove he was not, and because he was embarrassed about the kiss and about Adrian and did not want to see Kara or Adrian, and because he thought handling alone was brave when handling alone is sometimes just bottling\.",
         "Winn had not texted Kara. He had not texted Adrian sorry yet. He had not called the FBI."),
        (r"because he was her best friend even after kiss, even after he knew she is with Adrian and kissed anyway, even after he needed space\.",
         "because he was her best friend even after kiss, even after he needed space."),
        (r"because Kara held the field for three seconds longer than physics said it should, because her cells remembered sun and overcompensated and hearing sharpened temporarily then settles higher than before cells remember overcompensate, because she had been to sun with Adrian and held his hand\.",
         "because Kara held the field for three seconds longer than physics said it should. Because she had been to sun with Adrian and held his hand."),
        (r"because children think ice dome is magic, and it is magic, in a way\.",
         "because children think ice dome is magic."),
        # Ch19
        (r"because she was looking for mug\? No, because she was looking for file and found letter, and she had finished it, because she is Kara and she finishes things that are discarded, and she had mailed it under Cat's name, because she thought mother and son should reforge relationship\.",
         "because she was looking for file and found letter. She had finished it. She had mailed it under Cat's name."),
        # Ch21
        (r"Black Mercy was not a word he knew, but he knew what it did from bible\.",
         "Black Mercy was not a word he knew. He knew what it did from bible."),
        (r"because Black Mercy was Kryptonian and Astra knew it and had come because she felt it, not because DEO called\.",
         "because Black Mercy was Kryptonian and Astra knew it. She had come."),
        (r"She did not think about whether it was right\. She thought about Kara, unconscious in the med bay, and about Astra standing between Non and the people who mattered\.",
         "She did not think about whether it was right. Astra stood between Non and the people who mattered."),
        # Ch22
        (r"He had a Kryptonian tech baton that could hurt Kryptonian\. She felt it\.",
         "He had a Kryptonian tech baton that could hurt Kryptonian. The baton caught her arm."),
        # Ch23
        (r"Indigo had not kidnapped Winn\. She had come to him\. She had told him she knew his father, that she had helped Kara's ship exit the Phantom Zone, that she was not the enemy he thought she was, and she had asked him for something — for access to the DEO network, for the missile codes, for the thing she needed to destroy National City\.",
         "Indigo had not kidnapped Winn. She had come to him. She had told him she knew his father, that she had helped Kara's ship exit the Phantom Zone, that she was not the enemy. She had asked him for the missile codes."),
        (r"Indigo had not hurt him\. She had sat across from him, in the dark, and waited\. Because she had learned patience in the Phantom Zone, and because she knew that a man who refused once might refuse again, and again, until he broke\. Or until he didn't\.",
         "Indigo had not hurt him. She had sat across from him, in the dark, and waited."),
        (r"the way two people who had both been burned by their families found something quiet and ordinary together\.",
         "the way two people who had both been burned by their families sat next to each other."),
        (r"She looked at Winn when she thought he was not looking\. She looked at Kara when she thought Kara was not looking\. She looked at Adrian when she thought Adrian was not looking\.",
         "She looked at Winn. She looked at Kara. She looked at Adrian."),
        # Ch24
        (r"She meant it as a triumph\. She felt huge, bright, finally honest\.",
         "She meant it as a triumph."),
        (r"She knew that word\. J'onn had taught her and Adrian the shape of it, not the sound — Torquasm Vo, closing the mind, Torquasm Rao, projecting it\. She'd practiced it after the sun, after her finger healed and her baseline came up higher than ever, heart faster, vision sharper\. She'd practiced it because Adrian did\.",
         "J'onn had taught her and Adrian the shape of it, not the sound — Torquasm Vo, closing the mind, Torquasm Rao, projecting it. She'd practiced it after the sun."),
        (r"She looked at the man who had been Hank Henshaw, who had been her father's friend, who had been watching her since before she knew she was Kryptonian\. She looked at the Martian\.",
         "She looked at the man who had been Hank Henshaw. She looked at the Martian."),
        (r"She did not forgive him\. Not yet\. But she knew now\.",
         "She did not forgive him. Not yet."),
        # Ch25
        (r"He didn't tell her where to put it\. She knew\.",
         "He didn't tell her where to put it."),
        (r"Alex stood next to him, hand on her sidearm, not because she thought J'onn would hurt anyone, but because she knew others might\.",
         "Alex stood next to him, hand on her sidearm."),
        (r"She had stopped drinking weeks ago when she realized it was the thing she had in common with her father\.",
         "She had stopped drinking weeks ago."),
        (r"She went to sit\. She went to think\.",
         "She went to sit."),
        (r"and she felt it cushion her, felt it catch her like a hand, and she looked down and she was not falling, she was standing on air, standing on her own scream\.",
         "and it cushioned her, caught her like a hand, and she looked down and she was not falling, she was standing on air, standing on her own scream."),
        # Ch26
        (r"Kara stood in front of Adrian at the DEO, not because she thought he needed protecting, but because she wanted to stand there\.",
         "Kara stood in front of Adrian at the DEO."),
    ]
    
    for pattern, replacement in replacements:
        new_text, count = re.subn(pattern, replacement, text)
        if count > 0:
            changes.append(f"  Interiority fixed ({count}x): {pattern[:60]}...")
            text = new_text
    
    return text, changes


def fix_epithets(text, chapter_num):
    """Fix descriptive epithets in narration - use names instead."""
    changes = []
    
    # "the man in black" in narration -> "Wraith"
    # But keep media labels (when media is speaking)
    # Simple approach: replace in narration lines (non-quoted)
    
    epithet_replacements = [
        # Ch5 - narration uses
        (r"To the people filming, he was the man in black who had come to help Supergirl\.",
         "To the people filming, he was Wraith, who had come to help Supergirl."),
        (r"Cat had three usable views of the rescue and no confirmed name for the man in black\.",
         "Cat had three usable views of the rescue and no confirmed name for Wraith."),
        (r"Kara was visible above the harbor, the man in black landing nearby\.",
         "Kara was visible above the harbor, Wraith landing nearby."),
        # Ch6
        (r"Cat listened without interrupting, then asked whether the masked man had taught her to fly\.",
         "Cat listened without interrupting, then asked whether Wraith had taught her to fly."),
        (r"Lord smiled as if she had done him a favor\. He asked what she knew about the man in black\.",
         "Lord smiled as if she had done him a favor. He asked what she knew about Wraith."),
        # Ch7
        (r"On board, the man in the Lord jacket— Maxwell himself, Kara realized when she arrived a moment later— was escorting Carter toward the middle cars\.",
         "On board, Maxwell himself was escorting Carter toward the middle cars."),
        # Ch9 - media labels in quotes are fine, but narration should use Wraith
        (r"National City had decided that the masked helper from the freeway and the train was a story it could not leave alone\.",
         "National City had decided that Wraith, the masked helper from the freeway and the train, was a story it could not leave alone."),
        (r"Who is the man in black\?",
         "Who is Wraith?"),
        # Ch20
        (r"Without the quiet you okay\. Because what does it matter if the driver is okay\? The truck is saved\. The driver is\. \.\. a driver\. The truck is saved\. That is what matters\.",
         "Without the quiet you okay. The truck is saved. That is what matters."),
    ]
    
    for pattern, replacement in epithet_replacements:
        new_text, count = re.subn(pattern, replacement, text)
        if count > 0:
            changes.append(f"  Epithet fixed ({count}x): {pattern[:60]}...")
            text = new_text
    
    return text, changes


def fix_chapter(filepath, chapter_num):
    with open(filepath, 'r') as f:
        text = f.read()
    
    orig_len = len(text)
    all_changes = []
    
    # Apply interiority fix
    text, changes = fix_interiority(text, chapter_num)
    all_changes.extend(changes)
    
    # Apply epithet fix
    text, changes = fix_epithets(text, chapter_num)
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

print("=== INTERIORITY + EPHTHET SWEEP COMPLETE ===")
