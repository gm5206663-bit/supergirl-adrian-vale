# Executed validation — foundation-013 / canon audit

**29 September 2026.** No new story prose; accepted edge 3, Chapter 4 delivered candidate, interrupted Chapter 5 held.

| Check | Result |
|---|---|
| Entry baseline `run_all.py --ship 4` | FAILED: stale generated STATUS.md; suite stopped |
| Corrected structure/domain/mirrors | PASS |
| Defect tests, including new orphan-draft test | 51/51 PASS |
| Chapter 4 technical release | READY; not author acceptance |
| Chapter 5 technical release | BLOCKED as intended; held/superseded route |
| Accepted/draft manuscripts and Talent master | All byte-for-byte unchanged |
| Pending U19 versus accepted state | Explicitly separated; no adoption performed |

## Receipts
- `test-results/foundation-013-entry-baseline.txt` records the initially observed failure (summary, not a fabricated console transcript).
- `test-results/foundation-013-run-all.txt`: executed structure/domain checks and all 51 tests.
- `test-results/foundation-013-ship4.txt` / `foundation-013-ship5.txt`: actual separate release results.
- `test-results/foundation-013-protected-hashes.json`: before/after manuscript and reference hashes.
- `test-results/foundation-013-integrity.txt`: JSON/Python syntax, protected hashes, accepted edge and held-state assertions.
- Root `CHECKSUMS.sha256` covers every packaged project file except itself; no claim to be its own checksum.

Historical foundation-012 validation is preserved at `history/VALIDATION_foundation_012.md`; its previous delivered archive has not been overwritten.

## Limits
51 tests establish only the defects they exercise. They do not verify every sentence, certify security, adopt a chapter, independently watch an episode or establish all-series canon. See the canon audit for manual findings and unresolved sources. No remote GitHub operation occurred.
