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

---

## RE-ACCEPTANCE PENDING — added 2026-10-12

The repairs above changed chapters 09–15 AFTER the author accepted them. The house does not rewrite an ACCEPTED_HASH receipt — the acceptance is the author's act — so `tools/verify.py` reports exactly these seven chapters by design until the author re-accepts. The CI workflow pins this set: any failure BESIDES these fails the build.

To re-accept, the author reads each chapter, then the manifest entry in `foundation/CURRENT_STATE_MANIFEST.json` (`accepted_chapters`) gets the new `sha256` below with a fresh `accepted_on` and receipt line — or say the word and it is done for the chapters named.

| chapter | old sha256 (accepted) | new sha256 (repaired) |
|---|---|---|
| chapters/Chapter_09_Red_Faced_and_Named.md | `5242cb1d9b9b…` | `7d9361f95527349abfd2a94e7a4f2f426ba0aaae74d9743d88160562ca4509e1` |
| chapters/Chapter_10_Red_Faced_Consequence.md | `96c06c73e408…` | `ab25fb602154df6365826671a6b2e0daa765b8c3e97cfc0c794e8f14825ef0a0` |
| chapters/Chapter_11_The_Sun.md | `016a5dd5b6ca…` | `b0d93e134735042dc9b6e15773bd0041d5e5840baa4869f4335151f4ed38b739` |
| chapters/Chapter_12_The_Kiss.md | `85c151539c91…` | `1eb7c4d6f9818762579c9bcc3a04a91d3f5343804402f35a51ba41705011fa48` |
| chapters/Chapter_13_Human_for_a_Day.md | `a383f170299e…` | `11865eb6e3008da75eaaf9ab1b834a4082966a38ac740b3fe68204c3e642de27` |
| chapters/Chapter_14_Hostile_Takeover.md | `e1bfdce40e10…` | `0b8e6b6d6ff34cf962aa86742bbbfe8d2c51d3678e5b63aae3fee2093e78330c` |
| chapters/Chapter_15_Blood_Bonds.md | `9b16317f2296…` | `a54ea126932cbc07a2a3635d487eac28dba6335f92bf4e62907a795fb0bd2bf7` |

*Changed by:* the 2026-10-11 padding-loop repair (additive-free deletion of duplicated passages, keep-first) and the 2026-10-12 shelf pass (one stutter collapsed). Word sequences of the removed material are recoverable from `git log` for each chapter.
