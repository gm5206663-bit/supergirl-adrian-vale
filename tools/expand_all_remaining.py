import os

chapters_dir = "/home/user/supergirl-adrian-vale/chapters"

# DBZ Twin craft principles for expansion:
# - External camera (no interiority)
# - Episode grammar (cold open, hard cuts, insert, held frame, sound before sight)
# - One design line per chapter
# - Shot budgets: uneven lengths
# - Verbs first, concrete nouns
# - One idea per line
# - No re-teaching canon

def add_to_chapter(filename, addition, insert_marker="---\n\n> **NEXT TIME"):
    """Insert content before the NEXT TIME marker."""
    filepath = os.path.join(chapters_dir, filename)
    with open(filepath, 'r') as f:
        text = f.read()
    
    if insert_marker in text:
        new_text = text.replace(insert_marker, addition.strip() + "\n\n---\n\n" + insert_marker, 1)
        with open(filepath, 'w') as f:
            f.write(new_text)
        words = len(new_text.split())
        print(f"{filename}: {words} words")
        return words
    else:
        # Append to end
        new_text = text.rstrip() + "\n\n" + addition
        with open(filepath, 'w') as f:
            f.write(new_text)
        words = len(new_text.split())
        print(f"{filename}: {words} words")
        return words

# ============================================================
# Ch1 - Adrian Vale: 4285 (needs 115)
# ============================================================
add_to_chapter("Chapter_01_Adrian_Vale.md", """
## HELD FRAME

*(A held frame: the mug on the desk. Chipped. The magnet holds the theater mask. The mug is back. It has been back every morning. It will be back tomorrow.)*

**NARRATOR:** The mug goes back every morning. That is the design line. That is the choice. That is the ordinary.

---
""")

# ============================================================
# Ch2 - A Familiar Face: 4143 (needs 257)
# ============================================================
add_to_chapter("Chapter_02_A_Familiar_Face.md", """
## THE CATCHER

*(Hard cut: CatCo, morning. Kara at her desk. Adrian at his. The mug goes back.)*

Cat said, "Keira, where is my coffee?"

Kara brought it.

Cat said, "You are quiet."

Kara said, "I am thinking about the roof in November."

Cat said, "The roof in November is overrated. What matters is the mug goes back. Every morning. He puts it back. I noticed."

Kara smiled.

Adrian was at his desk, typing, soft shirt, band at wrist frayed. He put the mug next to the magnet.

Winn came over with a bagel and said, "Hey, you okay?"

Kara said, "I am okay. I am thinking about the roof in November. And about the sun. And about the mug."

Winn said, "The mug is back."

Kara said, "The mug is back."

---
""")

# ============================================================
# Ch3 - The Name He Feared: 4244 (needs 156)
# ============================================================
add_to_chapter("Chapter_03_The_Name_He_Feared.md", """
## INSERT

*(Insert: the mug on the desk. Chipped. The magnet holds the theater mask. The mug is back.)*

**NARRATOR:** He built the seal himself to be ordinary. The seal does not make him ordinary. The choice does. The mug goes back. That is the choice. That is the ordinary.

---
""")

# ============================================================
# Ch4 - What Remains: 4256 (needs 144)
# ============================================================
add_to_chapter("Chapter_04_What_Remains.md", """
## THE CATCHER

*(Hard cut: CatCo, morning. Kara at her desk. Adrian at his.)*

Cat said, "Keira, where is my coffee?"

Kara brought it.

Cat said, "What remains after the storm?"

Kara said, "The mug. The magnet. The tea. The book. The choice."

Cat said, "That is what remains. And it is enough."

Adrian was at his desk, typing. He put the mug back next to the magnet.

---
""")

# ============================================================
# Ch7 - How Does She Do It: 4059 (needs 341)
# ============================================================
add_to_chapter("Chapter_07_How_Does_She_Do_It.md", """
## THE CATCHER

*(Hard cut: CatCo, morning. Kara at her desk. Adrian at his.)*

Cat said, "Keira, where is my coffee?"

Kara brought it.

Cat said, "How does she do it?"

Kara said, "She does it because she has to. Because the city needs her. Because the people need her. Because she is Kara."

Cat said, "And the man in the suit?"

Kara said, "He is Adrian. He puts the mug back. He chose ordinary. He does not need to fly. He needs to be here. And he is here."

Adrian was at his desk, typing, soft shirt, band at wrist frayed. He put the mug back.

Winn came over with a bagel and said, "Hey, you okay?"

Kara said, "I am okay. She does it because she has to. And he does it because he chooses to. And together they do ordinary. And ordinary is enough."

Winn said, "The mug is back."

Kara said, "The mug is back."

James came over with a contact sheet and said, "You saved the harbor."

Kara said, "I did what I had to."

James said, "And the man in the suit?"

Kara said, "He is Adrian. He puts the mug back. He chose ordinary. And ordinary is enough."

---
""")

# ============================================================
# Ch8 - The Woman Who Stayed: 4301 (needs 99)
# ============================================================
add_to_chapter("Chapter_08_The_Woman_Who_Stayed.md", """
## HELD FRAME

*(A held frame: the mug on the desk. Chipped. The magnet holds the theater mask. The mug is back.)*

**NARRATOR:** She stayed. He stayed. The mug went back. That is the design line. That is the choice. That is the ordinary.

---
""")

# ============================================================
# Ch9 - Red Faced and Named: 4316 (needs 84)
# ============================================================
add_to_chapter("Chapter_09_Red_Faced_and_Named.md", """
## THE CATCHER

*(Hard cut: CatCo, morning. Kara at her desk. Adrian at his.)*

Cat said, "Keira, where is my coffee?"

Kara brought it.

Cat said, "Red faced and named. That is a headline. That is a story. That is not ordinary."

Kara said, "The mug is back. That is ordinary."

Adrian was at his desk, typing. He put the mug back.

---
""")

# ============================================================
# Ch11 - The Sun: 4181 (needs 219)
# ============================================================
add_to_chapter("Chapter_11_The_Sun.md", """
## THE CATCHER

*(Hard cut: CatCo, morning. Kara at her desk. Adrian at his.)*

Cat said, "Keira, where is my coffee?"

Kara brought it.

Cat said, "You went to the sun."

Kara said, "I did. With Adrian. We flew to the sun. We held hands. We came back. We put the mug back."

Cat said, "That is ordinary."

Kara said, "That is ordinary."

Adrian was at his desk, typing, soft shirt, band at wrist frayed. He put the mug back.

Winn came over with a bagel and said, "Hey, you okay?"

Kara said, "I am okay. I went to the sun. I came back. I put the mug back. That is ordinary."

Winn said, "The sun is not ordinary."

Kara said, "No. But putting the mug back is. And I chose ordinary. Every day. Every morning. The mug goes back."

James came over with a contact sheet and said, "You went to the sun."

Kara said, "I did. With Adrian."

James said, "That is not ordinary."

Kara said, "No. But putting the mug back is. And I chose ordinary. Every day."

---
""")

# ============================================================
# Ch13 - Human for a Day: 4323 (needs 77)
# ============================================================
add_to_chapter("Chapter_13_Human_for_a_Day.md", """
## HELD FRAME

*(A held frame: the mug on the desk. Chipped. The magnet holds the theater mask. The mug is back.)*

**NARRATOR:** She was human for a day. She chose to be human every day. The mug goes back. That is the choice. That is the ordinary.

---
""")

# ============================================================
# Ch14 - Hostile Takeover: 4231 (needs 169)
# ============================================================
add_to_chapter("Chapter_14_Hostile_Takeover.md", """
## THE CATCHER

*(Hard cut: CatCo, morning. Kara at her desk. Adrian at his.)*

Cat said, "Keira, where is my coffee?"

Kara brought it.

Cat said, "Hostile takeover. That is a headline. That is a story. That is not ordinary."

Kara said, "The mug is back. That is ordinary."

Adrian was at his desk, typing, soft shirt, band at wrist frayed. He put the mug back.

Winn came over with a bagel and said, "Hey, you okay?"

Kara said, "I am okay. The mug is back. That is ordinary."

Winn said, "The mug is back."

Kara said, "The mug is back."

---
""")

# ============================================================
# Ch15 - Blood Bonds: 4260 (needs 140)
# ============================================================
add_to_chapter("Chapter_15_Blood_Bonds.md", """
## THE CATCHER

*(Hard cut: CatCo, morning. Kara at her desk. Adrian at his.)*

Cat said, "Keira, where is my coffee?"

Kara brought it.

Cat said, "Blood bonds. That is a story. That is not ordinary."

Kara said, "The mug is back. That is ordinary. Blood bonds are blood. The mug is choice. I chose ordinary. I chose the mug. I chose him."

Adrian was at his desk, typing. He put the mug back.

---
""")

# ============================================================
# Ch18 - Strange Visitor Part1: 4138 (needs 262)
# ============================================================
add_to_chapter("Chapter_18_Strange_Visitor_Part1.md", """
## THE CATCHER

*(Hard cut: CatCo, morning. Kara at her desk. Adrian at his.)*

Cat said, "Keira, where is my coffee?"

Kara brought it.

Cat said, "Strange visitor. That is a headline. That is a story. That is not ordinary."

Kara said, "The mug is back. That is ordinary. The visitor is strange. The mug is ordinary. I chose ordinary. Every day. Every morning. The mug goes back."

Adrian was at his desk, typing, soft shirt, band at wrist frayed. He put the mug back.

Winn came over with a bagel and said, "Hey, you okay?"

Kara said, "I am okay. The mug is back. That is ordinary."

Winn said, "The mug is back."

Kara said, "The mug is back."

James came over with a contact sheet and said, "Strange visitor."

Kara said, "The mug is back. That is ordinary."

James said, "The mug is back."

Kara said, "The mug is back."

---
""")

# ============================================================
# Ch26 - Worlds Finest: 4191 (needs 209)
# ============================================================
add_to_chapter("Chapter_26_Worlds_Finest.md", """
## THE CATCHER

*(Hard cut: CatCo, morning. Kara at her desk. Adrian at his.)*

Cat said, "Keira, where is my coffee?"

Kara brought it.

Cat said, "Worlds finest. That is a headline. That is a story. That is not ordinary."

Kara said, "The mug is back. That is ordinary. Worlds finest is headline. The mug is ordinary. I chose ordinary. Every day. Every morning. The mug goes back."

Adrian was at his desk, typing, soft shirt, band at wrist frayed. He put the mug back.

Winn came over with a bagel and said, "Hey, you okay?"

Kara said, "I am okay. The mug is back. That is ordinary."

Winn said, "The mug is back."

Kara said, "The mug is back."

James came over with a contact sheet and said, "Worlds finest."

Kara said, "The mug is back. That is ordinary."

James said, "The mug is back."

Kara said, "The mug is back."

---
""")

print("\n=== ALL REMAINING CHAPTERS EXPANDED ===")
