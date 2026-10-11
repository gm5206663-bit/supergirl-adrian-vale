# REPAIR · 2026-10-11 · duplicate "padding" removed from chapters 9–14

**Who:** `tools/dedupe_paragraphs.py` (house tool, `soul-land-universal-kit`
`6972e5f`, applied here by the same operator who has been auditing this account).
**What it did:** removed paragraphs that appear more than once in one chapter.
**What it did not do:** touch a receipt, a draft revision, a checksum file, or a
single word of this serial's prose.

## The evidence

| chapter | passages removed | repeated words | words before | words after |
|---|---|---|---|---|
| 09 Red Faced and Named | 14 | 1,708 | 4,277 | 2,569 |
| 10 Red Faced Consequence | 20 | 738 | 3,467 | 2,729 |
| 11 The Sun | 34 | 2,949 | 4,282 | 1,333 |
| 12 The Kiss | 22 | 714 | 4,119 | 3,405 |
| 13 Human for a Day | 31 | 1,057 | 3,313 | 2,256 |
| 14 Hostile Takeover | 12 | 536 | 3,469 | 2,933 |

**7,702 repeated words across 133 duplicate passages.** In *Chapter 11 — The
Sun* the same combined closing paragraph — "There would be another headline
tomorrow. Tonight there was sun still in cells and chipped mug on desk…" — stood
**twenty times in a row**, two blank lines apart, at the end of the file. That is
not a refrain: a refrain varies. It is a loop that ran twenty times.

This is also the author's own stated criterion for this very chapter. The
acceptance record for Chapter 11 (`coverage "claimed_episode"`) reads:

> *"S01E06-08 — The Sun clean no ticker spam no Winn joke spam no meta"*

An acceptance that says *clean, no spam* was covering a file carrying 2,949
repeated words.

## The rule the tool applied

* A paragraph of **12 words or more** repeated exactly (whitespace-insensitive)
  keeps its **first** occurrence; later copies are deleted. Nothing is invented,
  nothing is reordered, every other byte is copied through.
* **Short beats are left alone.** `***` and `"Yes."` repeat on purpose throughout
  chapters 1–8 and were never candidates — which is why those chapters were not
  touched at all.
* **Distant echoes are left alone.** Chapter 15 carries two 12–25 word
  repetitions roughly seventy paragraphs apart; they read as callbacks, not
  padding, so they stay and are reported instead of deleted.
* Proof before write: the rebuilt file must equal an independently filtered copy
  of the original, paragraph for paragraph. A repair that cannot prove that is
  not written.

## The consequence, stated plainly

**Acceptance receipts are now stale, and that is visible on purpose.**
`tools/verify.py` fails with six `ACCEPTED_HASH` errors — chapters 09–14 no
longer match the sha256 recorded when each was accepted, against exactly these
revisions: R8, R5, R5, R6, R5, R8. That failure is **true**: accepted text was
changed. It was not silenced, and no receipt, date or hash was rewritten to
hide it. A new author receipt is the author's to write:

```
FAIL: ACCEPTED_HASH: missing or changed chapter chapters/Chapter_09_…md
… through Chapter_14
```

**The revision drafts still carry the padding.** They are history and were left
untouched, so **do not copy `drafts/Chapter_09…14` over `chapters/`** — that
would resurrect all 7,702 words. A clean revision must be cut from the repaired
chapter text.

**Five chapters are now below the episode header's target.** The headers claim
"Full 3000+ Words"; after the padding is gone, chapters 9, 10, 11, 13 and 14 sit
at 2,569 / 2,729 / 1,333 / 2,256 / 2,933. Only chapter 12 still clears 3,000.
The padding *was* the length. Restoring these chapters to their stated length
needs real prose — authoring, and therefore the author's work or the author's
explicit order. It is recorded here rather than papered over.

**Left for the author:** the 78 sentences over the house 60-word cap in this
serial. They are written in this serial's compressed beat style end to end —
the `foundation/` beats are written the same way — so they are treated as a
voice question, not a defect, and were not split. A boundary exists for fewer
than half of them; the rest have no punctuation to split on at all.

*Operator note: the repair was made under the standing delegation and the
2026-10-11 "Defect" ruling authorising chapter repair. It removes text and adds
none. If the author prefers the padded text, `git revert` this commit restores
it exactly.*
