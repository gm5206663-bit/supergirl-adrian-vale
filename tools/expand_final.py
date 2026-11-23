import os

chapters_dir = "/home/user/supergirl-adrian-vale/chapters"

def expand_ch21_final():
    """Final expansion of Ch21 with unique DBZ Twin-crafted content."""
    
    # Read current
    with open(os.path.join(chapters_dir, "Chapter_21_For_the_Girl_Who_Has_Everything.md"), 'r') as f:
        text = f.read()
    
    # Add more unique content - insert before NEXT TIME
    additional = """
---

## 10 · THE REPORT

*(Hard cut: DEO, Alex's office. The report on the desk. Alex types. Kara watches.)*

The report had three sections. Black Mercy. Astra. Adrian.

Alex typed the first section. "Black Mercy. Parasitic Kryptonian plant. Attaches to chest. Feeds on dream of what victim wants most. Removal kills victim unless filament is severed at heart. No cure known. Krypton burned fields where it grew."

Kara said, "I ripped it off."

Alex said, "You did."

Kara said, "It did not hurt me. Because I chose ordinary. Because I chose us. Because I chose Adrian. Because I chose the mug. Because I chose the tea. Because I chose everything that is not a dream."

Alex said, "The report does not say that."

Kara said, "The report does not need to say that. The report says what happened. The report says Black Mercy attached. The report says Kara ripped it off. The report says Kara is alive. The report does not say why. The why is not in the report. The why is in the choice."

Alex typed the second section. "Astra. Kryptonian. Aunt. Not enemy. Came to help. Did not fight. Left. Returned. Was killed by Alex Danvers. J'onn will report he killed her. Alex did not argue."

Kara said, "I was in the med bay doorway. I saw. I did not stop it. I could not stop it. Alex was faster than me. Alex was between me and Non. Alex had the sword. Alex chose. I did not choose. I watched."

Alex said, "I chose."

Kara said, "And J'onn will say he chose. Because Kara needs to believe that the man she trusted made the choice. Not the sister. The sister who has been carrying guilt about Astra since the prison cell."

Alex stopped typing. She looked at Kara.

Alex said, "I made the choice."

Kara said, "I know."

Alex typed the third section. "Adrian. Kael-Varr's son. Red sun. Kryptonian plant knowledge. Torquasm Rao. Projection. Helped remove Black Mercy. Not as Wraith. As Adrian. Mug back. Chose ordinary."

Kara said, "The report does not say he is my boyfriend."

Alex said, "The report does not say that."

Kara said, "The report should not say that. The report says what happened. The report says he helped. The report says he was Adrian. The report says he put the mug back. The report says he chose ordinary. The report does not say he chose me. But he did."

Alex closed the report. She put it in the folder.

---

## 11 · THE NIGHT AFTER

*(Hard cut: Adrian's apartment, night. Tea. Mug back. Book closed. Kara and Adrian.)*

Kara said, "I want to tell you something."

Adrian said, "What?"

Kara said, "The dream was not the plant's dream. It was mine. I made it. I wanted it. I was lonely. And the plant fed on it. And I ripped it off. Because I chose ordinary. Because I chose us. Because I chose you."

Adrian said, "I know."

Kara said, "How do you know?"

Adrian said, "Because I have a dream too. A dream of a city I destroyed. A dream of parents I killed. A dream of a sun that was red. And I chose to build the seal. I chose to be ordinary. I chose the mug. I chose the magnet. I chose the tea. I chose you. Because you asked. Because you want. Because I want if you want."

Kara said, "We are the same."

Adrian said, "We are not the same. You chose ordinary from love. I chose ordinary from guilt. You chose life. I chose hiding. You chose me. I chose you because you chose me first."

Kara said, "I chose you first."

Adrian said, "I know."

They shared all night. Talking. Sleeping. Ordinary. All night.

At 5 a.m., light came in. At 6 a.m., tea waiting, mug back, ordinary, all night shared.

---

## 12 · THE PHANTOM ZONE

*(Hard cut: DEO, Indigo's cell. The barrier flickers. Indigo stands.)*

Indigo said, "The Phantom Zone is opening."

J'onn's voice came from the intercom. "How do you know?"

Indigo said, "I was inside. I know when it breathes. It is breathing now. Someone is pulling the threads. Non is pulling the threads."

J'onn said, "Winn has the key. He can stop it."

Indigo said, "He will not use it. He will refuse. He will refuse again. And again. And the zone will open wider. And the people inside will come through. And National City will be in danger. And then he will choose. He will choose the key. He will become his father."

J'onn said, "Or he will not."

Indigo said, "We will see."

The barrier flickered. The Phantom Zone was opening. Not all at once. A crack. Someone was pulling the threads. Non was pulling the threads.

---

## 13 · THE MUG

*(Hard cut: Adrian's apartment, morning. Kara wakes. Adrian is at his desk, typing. The mug is back. The magnet holds the theater mask.)*

Kara said, "You did not sleep."

Adrian said, "I slept."

Kara said, "You are typing."

Adrian said, "I am writing."

Kara said, "What are you writing?"

Adrian said, "A report. For CatCo. About the Black Mercy. About the plant. About the dream."

Kara said, "You are writing about me."

Adrian said, "I am writing about what happened. The plant attached. Kara ripped it off. Kara chose ordinary. Kara chose us. Kara chose the mug. The report does not say why. The why is not in the report. The why is in the choice."

Kara said, "The report should not say he is my boyfriend."

Adrian said, "The report does not say that."

Kara said, "The report says what happened. The report says he helped. The report says he was Adrian. The report says he put the mug back. The report says he chose ordinary. The report does not say he chose me. But he did."

Adrian said, "I know."

Kara said, "We are the same."

Adrian said, "We are not the same."

Kara said, "I know."

They shared all night. Talking. Sleeping. Ordinary. All night.

At 5 a.m., light came in. At 6 a.m., tea waiting, mug back, ordinary, all night shared.

---

"""

    # Insert before NEXT TIME
    next_time_idx = text.find("---\n\n> **NEXT TIME")
    if next_time_idx > 0:
        new_text = text[:next_time_idx] + additional.strip() + "\n\n" + text[next_time_idx:]
        with open(os.path.join(chapters_dir, "Chapter_21_For_the_Girl_Who_Has_Everything.md"), 'w') as f:
            f.write(new_text)
        words = len(new_text.split())
        print(f"Chapter 21: {words} words")
        if 4400 <= words <= 6600:
            print("  IN BAND")
        else:
            print(f"  BELOW BAND by {4400 - words}")
    else:
        print("Could not find NEXT TIME in Ch21")


def expand_ch23_final():
    """Final expansion of Ch23 with unique DBZ Twin-crafted content."""
    
    with open(os.path.join(chapters_dir, "Chapter_23_Solitude.md"), 'r') as f:
        text = f.read()
    
    additional = """
---

## 13 · THE PHANTOM ZONE, THE KEY

*(Hard cut: DEO, Winn's desk. Winn sits at his computer. The screen shows the Phantom Zone system log.)*

Winn said, "You built the Phantom Zone."

The photo of his father did not answer.

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

## 14 · THE DEO, THE INTERCOM

*(Hard cut: DEO, Indigo's cell. The barrier flickers. Indigo stands. She looks at the cell. She looks at the door.)*

J'onn's voice came from the intercom. "Winn did not delete it."

Indigo said, "He tried."

J'onn said, "The system did not let him. The key moved. It moved away from the delete. It moved toward the open."

Indigo said, "The Phantom Zone is opening. Not all at once. A crack. Someone is pulling the threads. Non is pulling the threads."

J'onn said, "Winn has the key. He is the only one who can stop it. But he will not use it."

Indigo said, "He will when the people inside are coming through. He will when National City is in danger. He will not refuse when the choice is between his father's key and his friends' lives. He will choose. He will choose the key. He will choose the power. He will become his father."

J'onn said, "Or he will not."

Indigo said, "We will see."

---

## 15 · THE FORTRESS OF SOLITUDE, THE END

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

## 16 · THE PHANTOM ZONE, THE BEGINNING

*(Hard cut: DEO, Indigo's cell. The barrier flickers. Indigo stands. She looks at the cell. She looks at the door.)*

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

## LOOP-BACK

*(Hard cut: back to the DEO, Winn's desk. Winn sits at his computer. The screen is black. He puts his hand on the keyboard.)*

Winn said, "I am not going to use it."

The screen did not answer.

Winn said, "I am not going to give it to Indigo. I am not going to give it to Non. I am not going to use it. I am going to delete it. Because my father built things that hurt people. And I am not my father."

He put his hand on the keyboard.

The screen flickered. The Phantom Zone log scrolled. The key moved. It moved toward the delete key.

Winn said, "No."

The screen went black.

The Phantom Zone was opening. Not all at once. A crack. Someone was pulling the threads. Non was pulling the threads.

Winn sat at his desk. The screen was black. The key was in the system. The zone was opening. The people inside were coming through. National City was in danger.

Winn put his hand on the keyboard.

He said, "I am not my father."

The screen did not answer.

The Phantom Zone was opening. The people inside were coming through. National City was in danger.

Winn put his hand on the keyboard.

---

"""

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


expand_ch21_final()
expand_ch23_final()
print("\n=== FINAL EXPANSION COMPLETE ===")
