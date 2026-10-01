# Project working contract

Read HANDOFF.md → foundation/STATUS_PANEL.md → foundation/NO_MISTAKE_LIVE_RULES.md → latest audit → last accepted chapter. Read the relevant foundation before changing it.

The author’s latest instruction is the project authority. Preserve exact rulings in USER_LOCKS.json; distinguish menu selections from verbatim messages. This is not permission to disregard platform safety or handling of credentials.

One editable source of current state: `foundation/CURRENT_STATE_MANIFEST.json`. STATUS_PANEL, HANDOFF, SERIAL_LOG and STATUS are generated views. Change the underlying state and regenerate the same turn. Never infer accepted state from the highest chapter filename.

Run `python3 tools/verify.py` before and after changes, and `python3 tools/selftest.py` after tool changes. Structural PASS is not chapter acceptance. Run `python3 tools/verify.py --ship 1` for the first candidate’s release readiness; inspect the current result rather than assuming a historical BLOCK; technical readiness never supplies author acceptance.

Draft → source/coverage review → craft/power/knowledge review → technical checks → explicit acceptance receipt → numbered chapter + state and log updates. Do not skip from a user saying “start” to chat-only prose. Preserve existing drafts; never silently delete or relabel them rejected.

No background story transfer from other serials. No whole-workshop mirror. Retain only this project’s files and the directly applicable Talent master. Do not edit other repositories or publish this project without a specific destination and authorization. No credentials in files, URLs, logs or archives.

Deliver chapter files with coverage, state deltas, executed checks and a brief handoff. Readability and canon accuracy require real review, not a green word-count gate.

## Expanded domain records
`foundation/AUTHORITY_AND_PROVENANCE.md` assigns ownership for relationship, knowledge, ability and chronology records. After domain edits, run `python3 tools/render_codex.py`, then `python3 tools/render_state.py`, then `python3 tools/run_all.py`. Never silently promote a working design into a user lock. `foundation/FILE_CONTRACT.json` lists required populated files; the domain checker checks IDs, references, event order and generated views.
