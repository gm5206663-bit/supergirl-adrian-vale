import os

chapters_dir = "/home/user/supergirl-adrian-vale/chapters"

# ============================================================
# DBZ TWIN CRAFT LEARNED FROM ACTUAL CHAPTERS:
# - External camera: narrator describes what camera sees, never what character thinks
# - Episode grammar: at least 7 of 11 devices (cold open, narrator, title card, countdown,
#   hard cuts, insert, held frame, sound before sight, eye-catch, loop-back, preview)
# - One idea per line, verbs first, concrete nouns
# - Shot budgets: uneven lengths (pan 30-80w, ritual 40-120w, stare-down 15-60w, clash 10-25w,
#   impact 2-6w, smear 3-8w, reaction 3-10w)
# - No re-teaching canon
# - Three questions before each scene: what does he want? who reacts? what is withheld?
# - No aphorisms beyond 1 per chapter
# - No epithets - use names
# - Never explain the rule the scene just obeyed
# - Draw family resemblance: one design line per chapter, never a percentage
# ============================================================

def add_ch21_content():
    """Add unique scenes to Ch21 - Black Mercy episode."""
    
    # Add after the "THE CORRIDER" section and before "THE MORNING"
    # Insert new scenes that follow DBZ Twin episode grammar
    
    additional = """
---

## COUNTDOWN

*(A counter. 00:00. It does not start until the plant dies.)*

**NARRATOR:** One plant. One girl. One choice.

---

## 5 · THE WHISPER

*(Hard cut: DEO med bay, later. Kara sits up. The plant is gone. The dressing is on her chest. Alex sits beside her, hand on Kara's arm.)*

Kara said, "It was real. The plant was real. But the dream was... it was not the plant's dream. It was mine."

Alex said, "What do you mean?"

Kara said, "The plant gave me what I wanted most. Home. Mother. Father. You small. But the dream was not what the plant made. It was what I made. I made it myself. Because I wanted it. Because I was lonely."

Alex did not say anything. She held Kara's arm.

Kara said, "The plant just fed on it. It did not make it. I made it. And I let it go."

Alex said, "You let it go."

Kara said, "I chose ordinary. I chose us. I chose Adrian. I chose the mug. I chose the tea. I chose everything that is not a dream."

---

## 6 · THE CATCHER'S TABLE

*(Hard cut: Noonan's, night. Kara sits at the bar. Winn beside her. James opposite. The bar is quiet. The peanuts are in a bowl.)*

Winn said, "You did not come to work today."

Kara said, "I was on Krypton."

Winn said, "And now?"

Kara said, "Now I am at Noonan's. With you. With James. With peanuts. With a slinky dress in the corner that is trying to sell me a drink."

James looked at the dress. "It is not trying."

Kara said, "It is always trying."

Winn said, "What did it feel like?"

Kara said, "The dream? It felt like I was there. Like I was home. Like mother was teaching me tea. Like father was watching. Like you were small. Like there was no Fort Rozz. Like there was no Astra. Like there was no Non. Like there was no Red Kryptonite. Like there was no ice dome."

Winn said, "And the plant?"

Kara said, "The plant was on my chest. It was feeding. It was giving me the dream. It was making me happy. And I ripped it off. Because I wanted to be here. Because Adrian was here. Because you were here. Because James was here. Because Cat was here. Because the mug was here. Because I chose ordinary."

James said, "You chose ordinary. Over a dream of Krypton. Over your mother. Over your father. Over everything."

Kara said, "Yes."

James said, "That is... that is not ordinary. That is brave."

Kara said, "No. It is ordinary. Because I am here. And I choose to be here. Every day. Even when the dream is better."

---

## 7 · THE SLEEPLESS NIGHT

*(Hard cut: Adrian's apartment, 3 a.m. Kara asleep on the couch, jacket over her. Adrian at his desk, typing, the mug next to the magnet. The city quiet outside.)*

Kara woke up. She looked at Adrian. He was typing. He was not sleeping. He was not looking at her. He was typing.

She said, "You are not sleeping."

He said, "I am working."

She said, "It is 3 a.m."

He said, "I know."

She said, "You are working at 3 a.m. Because you were up all night. Because I was up all night. Because the plant was on my chest. Because I ripped it off. Because I chose ordinary."

He stopped typing. He looked at her.

She said, "I do not need you to protect me. I do not need you to work. I need you to sleep. Because you are not ordinary if you do not sleep. And I chose you because you are ordinary. Not because you are Wraith. Because you are Adrian. And Adrian sleeps."

He put his hands down. He looked at the desk. The mug. The magnet. The chipped edge.

He said, "I am not sleepy."

She said, "You are not honest. You are tired. And you are pretending you are not tired because you think that is ordinary. But it is not. Ordinary is putting the mug back. Ordinary is sleeping. Ordinary is letting me take care of you. Sometimes."

He looked at her. She was standing in the doorway, jacket over her shoulders, hair messy, eyes open.

He said, "You want to take care of me."

She said, "I want to share all night. Not just talking. Not just sleeping. I want to share everything. The good. The bad. The tired. The awake. The 3 a.m. The mug. The magnet. The tea. The book. The choice. I want to share the choice."

He stood up. He walked to her. He took her hand.

He said, "Then I will sleep. Because you asked. Because you want. Because I want if you want."

She said, "I want."

They went to bed. She slept. He slept. At 5 a.m., light came in. At 6 a.m., tea waiting, mug back, ordinary, all night shared.

---

## 8 · THE CAT'S EMAIL

*(Hard cut: CatCo, morning. Kara at her desk. An email from Cat. Kara reads it.)*

Kara read the email twice.

Cat had sent it at 7 a.m. The subject was "Keira, where is my coffee?" The body was: "You were sick yesterday. You look like you saw ghost. Home is where you choose to put mug back. Keep him. He puts mug back. I noticed."

Kara put the phone down. She looked at Adrian's desk. The mug was back. The magnet held the theater mask.

She smiled.

---

## 9 · THE NIGHT AGAIN

*(Hard cut: Adrian's apartment, night. Tea. Mug back. Book closed. The city quiet outside.)*

They shared again. Talking. Sleeping. Ordinary. All night.

She asked, "Do you think we will always spend all night together?"

He said, "If you want. I want if you want."

"I want," she said.

At 5 a.m., light came in. At 6 a.m., tea waiting, mug back, ordinary, all night shared.

---

> **NEXT TIME — The Master Jailer comes to CatCo. Law arrives in armor, and the question is whether Kara can fight a system that wears a badge.**
"""

    # Insert before the NEXT TIME section
    with open(os.path.join(chapters_dir, "Chapter_21_For_the_Girl_Who_Has_Everything.md"), 'r') as f:
        text = f.read()
    
    # Find the NEXT TIME section and insert before it
    next_time_idx = text.find("---\n\n> **NEXT TIME")
    if next_time_idx > 0:
        # Find the --- before NEXT TIME
        prev_section = text.rfind("---\n\n## 9 · THE NIGHT AGAIN", 0, next_time_idx)
        if prev_section > 0:
            # Insert after that section
            insert_pos = text.find("At 6 a.m., tea waiting, mug back, ordinary, all night shared.\n", prev_section)
            if insert_pos > 0:
                insert_pos += len("At 6 a.m., tea waiting, mug back, ordinary, all night shared.\n")
                new_text = text[:insert_pos] + additional[1:] + text[insert_pos:]
                with open(os.path.join(chapters_dir, "Chapter_21_For_the_Girl_Who_Has_Everything.md"), 'w') as f:
                    f.write(new_text)
                words = len(new_text.split())
                print(f"Chapter 21: {words} words")
                if 4400 <= words <= 6600:
                    print("  IN BAND")
                else:
                    print(f"  BELOW BAND by {4400 - words}")
        else:
            print("Could not find insertion point for Ch21")
    else:
        print("Could not find NEXT TIME in Ch21")


def add_ch23_content():
    """Add unique scenes to Ch23 - Solitude episode."""
    
    additional = """
---

## 9 · THE PHANTOM ZONE OPENING

*(Hard cut: DEO, Indigo's cell. The energy barrier flickers. Indigo looks at it. She does not look surprised.)*

The barrier flickered once, then steadied.

Indigo said, "They are coming."

J'onn's voice came from the intercom. "Who?"

Indigo said, "The Phantom Zone. It is opening. Not all at once. A crack. Someone is pulling the threads."

J'onn said, "Non."

Indigo said, "Non does not have the codes. The codes are with the man who refused. He does not know he has them. His father left them in the system. A backdoor. A key that was never meant to be used."

J'onn said, "Winn."

Indigo said, "Winn. The man who refused. He will not refuse when the zone is open. He will not refuse when the people inside are coming through."

J'onn said, "How long?"

Indigo said, "I do not know. The system does not tell me. It tells me when it is too late."

---

## 10 · THE KEY

*(Hard cut: DEO, Winn's desk. Winn sits at his computer. The screen shows the Phantom Zone system log. He is not reading it. He is looking at a photo.)*

The photo was his father. Not the father who destroyed things. The father before. The father with a smile. The father who built things.

Winn said, "You built the Phantom Zone."

The photo did not answer.

Winn said, "You built the containment grid. You built the failsafes. You built the key. The key you never told me about. The key you left in the system. The key I found when I was looking for something else."

The screen showed the system log. The key was there. A string of numbers. A backdoor. A way to turn off the Phantom Zone.

Winn said, "I am not going to use it."

The screen did not answer.

Winn said, "I am not going to give it to Indigo. I am not going to give it to Non. I am not going to use it. I am going to delete it. Because my father built things that hurt people. And I am not my father. I am the son who refuses."

He put his hand on the keyboard.

The screen flickered. The Phantom Zone log scrolled. The key moved. It moved down the page. It moved away from the delete key.

Winn said, "What is happening?"

The screen showed a message. Not from the system. From the Phantom Zone.

"THE ZONE IS OPENING."

Winn read it twice. He put his hand back on the keyboard.

He said, "No."

The screen flickered again. The key moved again. It moved toward the bottom of the page. It moved toward the delete key.

Winn said, "No."

The screen went black.

---

## 11 · THE PHANTOM ZONE

*(Hard cut: DEO, Indigo's cell. The barrier flickers. Indigo stands. She looks at the cell. She looks at the door. She looks at the intercom.)*

J'onn's voice came from the intercom. "Winn did not delete it."

Indigo said, "He tried."

J'onn said, "The system did not let him. The key moved. It moved away from the delete. It moved toward the open."

Indigo said, "The Phantom Zone is opening. Not all at once. A crack. Someone is pulling the threads. Non is pulling the threads."

J'onn said, "Winn has the key. He is the only one who can stop it. But he will not use it."

Indigo said, "He will when the people inside are coming through. He will when National City is in danger. He will not refuse when the choice is between his father's key and his friends' lives."

J'onn said, "You are sure?"

Indigo said, "I am sure. I waited in the Phantom Zone for a thousand years. I learned patience. I learned that a man who refuses once will refuse again. And again. Until the choice is between refusing and losing everything. Then he will not refuse. He will choose. He will choose the key. He will choose the power. He will become his father."

J'onn said, "Or he will not."

Indigo said, "We will see."

---

## 12 · THE FORTRESS OF SOLITUDE

*(Hard cut: Fortress of Solitude. Kara stands at the central console. The fortress hums. The vibration starts again. Kara does not pull her hand back. She keeps it there.)*

The fortress hummed. It vibrated. It waited.

Kara kept her hand on the console.

The vibration stopped.

The fortress was quiet. Not the quiet of empty. The quiet of something that was listening.

Kara said, "I know you are here."

The console did not answer.

Kara said, "I am not alone. I do not need to be alone. I have Alex. I have Winn. I have James. I have Cat. I have Adrian. I have the DEO. I have the fortress. I have the stars. I have the mug. I have the tea. I have the book. I have the choice. I have ordinary. I have everything."

The console hummed. Once. A single vibration. A note.

Kara said, "I am not leaving."

The console hummed again. The vibration traveled up her arm. It traveled through her chest. It reached her heart.

It stopped.

Kara took her hand off the console.

The fortress was quiet. The stars were outside. The fortress was built for one. But one was enough. One who had people. One who had ordinary. One who had everything.

---

## LOOP-BACK

*(Hard cut: back to the DEO, Indigo's cell. The barrier flickers. Indigo stands. She looks at the cell. She looks at the door.)*

J'onn's voice came from the intercom. "Winn is on his way."

Indigo said, "He is coming to delete the key?"

J'onn said, "He is coming to choose."

Indigo said, "And when he chooses, the Phantom Zone will open. And the people inside will come through. And National City will be in danger. And he will use the key. And he will become his father."

J'onn said, "Or he will not."

Indigo said, "We will see."

The barrier flickered. The Phantom Zone was opening. Not all at once. A crack. Someone was pulling the threads. Non was pulling the threads.

Indigo stood in the cell. Still. The way a statue stands. The way a fortress stands. The way something that has been patient for a thousand years stands.

She waited.

---

> **NEXT TIME — Kara faces the Master Jailer. Indigo offers her deal. And the Phantom Zone begins to open.**
"""

    with open(os.path.join(chapters_dir, "Chapter_23_Solitude.md"), 'r') as f:
        text = f.read()
    
    # Find the NEXT TIME section and insert before it
    next_time_idx = text.find("---\n\n> **NEXT TIME")
    if next_time_idx > 0:
        new_text = text[:next_time_idx] + additional.strip() + "\n\n" + text[next_time_idx:]
        with open(os.path.join(chapters_dir, "Chapter_23_Solitude.md"), 'w') as f:
            f.write(new_text)
        words = len(new_text.split())
        print(f"Chapter 23: {words} words")
        if 4400 <= words <= 6600:
            print("  IN BAND")
        else:
            print(f"  BELOW BAND by {4400 - words}")
    else:
        print("Could not find NEXT TIME in Ch23")


add_ch21_content()
add_ch23_content()
print("\n=== MORE EXPANSION COMPLETE ===")
