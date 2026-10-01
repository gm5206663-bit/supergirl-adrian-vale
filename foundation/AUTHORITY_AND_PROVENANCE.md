# Authority, provenance and file ownership

## Claim classes
- **USER LOCK:** directly supplied or selected by the author; evidence in USER_LOCKS.json.
- **DELEGATED DESIGN:** a choice made under an explicit delegation, such as Adrian's names and apparent age.
- **WORKING DESIGN:** substantive assistant-created story material prepared in response to the request for all foundations. Usable as a proposed writing foundation, not a fabricated user quotation or DC canon fact.
- **CANON SUMMARY:** independently sourced description of the television story, with stated source quality. It is not a direct episode-viewing receipt.
- **DRAFT EVENT:** appeared in an unaccepted draft; must not become accepted history automatically.
- **OPEN:** not defined or not sufficiently verified. Unknown is not the same as impossible.

## Ownership of facts
| Information | Editable authority | Human-readable view |
|---|---|---|
| Current chapter edge, epoch, opening access, acceptance | CURRENT_STATE_MANIFEST.json | STATUS_PANEL, HANDOFF, SERIAL_LOG, CANON_LEDGER |
| Author wording | USER_LOCKS.json | Rules/bible summaries; do not overwrite the wording |
| Working design scope | DESIGN_DECISIONS.json plus named design document | Design register |
| Entity IDs | codex/ENTITIES.json | Character dossiers |
| Opening relationship records | codex/RELATIONSHIP_LEDGER.json | codex/RELATIONSHIPS.md |
| Information boundaries | codex/KNOWLEDGE_LEDGER.json | codex/KNOWLEDGE_STATE.md |
| Ability claims and their provenance | bible/ABILITY_REGISTRY.json | bible/ABILITY_LEDGER.md |
| Ordered OC history | timeline/OC_CHRONOLOGY.json | timeline/OC_CHRONOLOGY.md |
| Broadcast metadata | timeline/EPISODE_INDEX.json | EPISODE_INDEX.csv |

Current chapter state remains in one manifest. Supporting ledgers hold detailed domain records; they cannot override its opening locks. Automated checks cross-check the overlap. Generated documents say which input controls them.

## Change discipline
A proposed relationship is not an accepted scene. A prospective arc is not a promised ending. A source title/airdate is not an in-world timestamp. User approval of one detail does not approve every neighboring proposal. Changes update their owner and regenerate the related views in the same turn.

## Accepted-event records
`accepted_event` now records facts evidenced by an adopted chapter. Knowledge/chronology rows require source_chapter and source_path matching the manifest; relationship deltas also retain the chapter hash and a concrete description. Opening baselines are not overwritten by candidate-only discoveries. U13’s adoption basis is explicitly a request to continue from the latest delivered version, not fabricated broader approval.
