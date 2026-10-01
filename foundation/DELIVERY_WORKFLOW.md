# Delivery workflow

## Before a chapter
1. Read HANDOFF, live manifest/panel, locks and relevant local foundations.
2. Run the structural verifier and inspect warnings.
3. Read latest accepted work and audit; do not continue an unaccepted draft as established history.
4. Verify the selected canon span, record source quality, and prepare coverage before drafting.
5. Record a scene plan, knowledge boundaries, power/access state, stakes and intended changes.

## Draft and review
6. Save the actual prose file, not just chat output. Keep reference apparatus separate.
7. Complete itemized canon, continuity, character, power, knowledge and prose reviews, citing the actual draft and hash.
8. Run technical checks. Fix content/state rather than weakening gates. Complete the candidate coverage JSON with review references and an accurate source span.
9. `python3 tools/verify.py --ship N` checks a registered draft’s technical readiness. It does not provide author acceptance and cannot verify the truth of a manually entered review.

## Acceptance and handoff
10. Only after explicit acceptance: add chapters/Chapter_NN_Title.md and matching accepted coverage, record receipt/date/hash in accepted_chapters, advance accepted_edge/next_chapter, add event and canon-beat IDs, update the actual knowledge/butterfly records.
11. Run `python3 tools/render_state.py`, then `python3 tools/verify.py` and the self-tests when tools change.
12. Deliver chapter, coverage, updated state and test receipt together. GitHub publication requires a destination and authorization; local files do not mean a push happened.

## Fresh session
Use the root handoff and source receipts. Recheck live GitHub only for relevant references, not by permanently mirroring the entire account. The older generic dc-preparation kit is superseded for this story.

## Expanded ledgers
When relationships, knowledge, abilities, design status or OC chronology change, edit their owning JSON ledger, add the evidence, run `python3 tools/render_codex.py`, then `python3 tools/render_state.py` and `python3 tools/run_all.py`. Read AUTHORITY_AND_PROVENANCE before treating a proposal as fact. No automatic love scores or undated accepted events.
