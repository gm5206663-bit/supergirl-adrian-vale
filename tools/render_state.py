#!/usr/bin/env python3
"""Generate all live-state views from the one editable manifest. Standard library only."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ['README.md', 'HANDOFF.md', 'STATUS.md', 'foundation/STATUS_PANEL.md', 'foundation/SERIAL_LOG.md', 'foundation/CANON_LEDGER.md']

def make_views(root):
    raw = (root / 'foundation/CURRENT_STATE_MANIFEST.json').read_bytes()
    m = json.loads(raw)
    digest = hashlib.sha256(raw).hexdigest()
    stamp = '<!-- GENERATED from foundation/CURRENT_STATE_MANIFEST.json; SHA256: ' + digest + ' -->\n\n'
    i, s = m['identity'], m['opening_state']
    paths = sorted(set(str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts) | set(GENERATED))
    draft_lines = '\n'.join('- [' + d['path'] + '](' + d['path'] + '): ' + d['status'] for d in m['drafts']) or '- None.'
    common = f"**Epoch:** {m['epoch']} · **Revision:** {m['revision']}  \n**Accepted chapter edge:** {m['accepted_edge']} · **Next chapter:** {m['next_chapter']}  \n**Phase:** {m['phase']}"
    if m.get('active_audit'):
        common += '\n\n**Latest audit:** `'+m['active_audit']['path']+'` (dated findings; current acceptance state is shown above).\n'
    if m['identity'].get('public_identity_policy'):
        common += '\n**U23 public identity:** complete suit/mask for interventions; civilian identity protected. Visual resemblance is out-of-world only. See `bible/PUBLIC_IDENTITY_AND_COSTUME.md`.\n'
    latest_chapter=m['drafts'][-1]['chapter']
    accepted_lines='\n'.join(f"- [Chapter {c['number']}]({c['path']}): {c['acceptance_receipt']}" for c in m['accepted_chapters']) or '- None yet.'
    release_label = 'TECHNICALLY READY — author acceptance remains separate' if m['release']['ready'] else 'BLOCKED — outstanding candidate reviews/conflicts'
    overview = f'''# Supergirl — Adrian Vale

## The actual project files

This is the local, GitHub-ready working project—not another generic DC questionnaire kit. It records the author's chosen Supergirl premise, foundations, original draft, canon research, state and executable checks.

{common}

**Not published to GitHub.** No remote repository is configured. Local preparation does not imply permission to create or push a repository.

## Start here

| Read | Purpose |
|---|---|
| [PROJECT_ATLAS.md](PROJECT_ATLAS.md) | Full expanded foundation and codex navigation |
| [RELATIONSHIPS.md](codex/RELATIONSHIPS.md) | Dedicated relationship records and development boundaries |
| [MASTER_TIMELINE.md](timeline/MASTER_TIMELINE.md) | OC/source clocks, season-one map and 126-episode index |
| [HANDOFF.md](HANDOFF.md) | Current edge, locks, next action and verification |
| [MASTER_PROJECT_BIBLE.md](MASTER_PROJECT_BIBLE.md) | Story foundation and delegated identity |
| [STATUS_PANEL.md](foundation/STATUS_PANEL.md) | Generated current-state view |
| [USER_LOCKS.json](foundation/USER_LOCKS.json) | Exact typed rulings and selected options |
| [POWER_FOUNDATION.md](bible/POWER_FOUNDATION.md) | Sealed access versus true capability |
| [SEALING_DEVICE.md](bible/SEALING_DEVICE.md) | Self-built device, rules and open engineering |
| [ADAPTATION_TALENT_LOCAL_DC.md](bible/ADAPTATION_TALENT_LOCAL_DC.md) | This holder's application of the full master |
| [KNOWLEDGE_FIREWALL.md](codex/KNOWLEDGE_FIREWALL.md) | Who knows what, without reader/character leakage |
| [PILOT_BEAT_MAP.md](canon_coverage/PILOT_BEAT_MAP.md) | Source span and honest coverage gaps |
| [RETROSPECTIVE AUDIT](audits/CHAPTER_01_RETROSPECTIVE.md) | What the first draft does and does not establish |
| [STATUS.md](STATUS.md) | Complete file map |

## Your protagonist

**{i['earth_name']} / {i['kryptonian_name']}** — native male {i['species']}; apparently {i['apparent_age']}, exact chronology not yet set. Works directly for Cat Grant. Exceptionally powerful before Fort Rozz through his own red-sun development with Adaptation Talent. {m['background']['summary']} Kryptonian technology captured him. Exhausted by that life, he built his seal and chose ordinary living on Earth.

At the opening, active superpowers are human-level while sealed; release is voluntary. His real power is far above the show's Kara and Superman. He knows Kara only as a coworker. No romance, exact power numbers or automatic unsealing rage has been established.

## Chapter files

{accepted_lines}

### Preserved drafts and current candidate

{draft_lines}

Chapter 1 R1 is preserved as historical draft material with documented gaps and the superseded accident memory. The latest candidate is **Chapter {latest_chapter}, {m['drafts'][-1]['revision']}**; use its own coverage and review receipts. No revision is automatically accepted.

## Run the checks

```bash
python3 tools/render_codex.py
python3 tools/render_state.py
python3 tools/run_all.py
python3 tools/verify.py --ship {latest_chapter}
```

The first verifier checks structure/integrity. The final command currently reports **{release_label}** for the latest registered candidate. It does not accept or publish a chapter. See [audits/VALIDATION.md](audits/VALIDATION.md) for executed receipts.

## Contents and limits

Includes the complete unmodified Talent master; detailed working power, device and history designs; individual character dossiers; relationship, knowledge and ability ledgers; world, location, organization and technology codices; ordered OC history; a twenty-episode first-season map; factual metadata for all 126 episodes; prospective arcs; source/approval distinctions; draft and review records; synchronized views and tested validators. It does not include a full screenplay, a whole-account mirror, credentials, invented approval, or a claim that every later season has been verified.

Specific unresolved facts are in [OPEN_DECISIONS.md](foundation/OPEN_DECISIONS.md). Resolve those when relevant; do not ask the author to repeat settled choices. This project supersedes the earlier generic `dc-preparation/` kit for this story.

[Fan-work notice](NOTICE.md)
'''
    panel = f'''# Current status panel

{common}

## Current authority
Edit `foundation/CURRENT_STATE_MANIFEST.json`, then regenerate. This panel is a view, not a competing source of truth.

## Identity and access
- Earth name: {i['earth_name']}
- Kryptonian name: {i['kryptonian_name']}
- Species: {i['species']}; father: {i['ancestry']['father']}; mother: {i['ancestry']['mother']}
- Apparent age: {i['apparent_age']}; chronological age: {i['chronological_age'] if i['chronological_age'] is not None else 'OPEN'}
- Employment: {i['job']}
- Historical opening anchor: {s['anchor']}
- Accepted continuation anchor: {m.get('continuation_state',{}).get('anchor','opening')}
- Candidate endpoint record: {m.get('candidate_endpoint','not assigned')}
- Location: {s['location']}
- Historical opening seal: {s['seal']}; voluntary release: {s['voluntary_release']}
- Accessible superpowers: {s['accessible_superpowers']}
- Actual unsealed benchmark: {s['true_power']}
- Historical opening knowledge of Kara’s identity: {s['kara_identity_known']}
- Accepted continuation knowledge of Kara’s identity: {m.get('continuation_state',s).get('kara_identity_known')}
- Canon foreknowledge: {s['canon_foreknowledge']}
- Acquired skills erased by seal: {s['learned_skills_erased_by_seal']}

## Accepted source coverage
{', '.join(m['continuity']['accepted_canon_beats']) or 'None. No draft automatically consumes source beats.'}

## Publication
Remote configured: {m['remote']['configured']}. Repository: {m['remote']['repository'] or 'not selected'}. Remote changes made: {m['remote']['changes_made']}.

## Release state
Ready: {m['release']['ready']}. {m['release']['reason']}

## Open items
{', '.join(m['open_items'])}; see OPEN_DECISIONS.md. These are not permission to forget the author-established qualitative strength or invent weaknesses.
'''
    handoff = f'''# Handoff — Supergirl / Adrian Vale

## 1. What this is
A native male {i['species']} Talent holder with a genuinely criminal Fort Rozz past chooses an ordinary, voluntarily sealed life as Cat Grant's employee. The author selected the Supergirl television pilot and canon-on-page / OC-woven narration.

## 2. The live edge
{common}

The first chat chapter is preserved under drafts/ as R1. The latest candidate is **Chapter {latest_chapter}, {m['drafts'][-1]['revision']}**, at `{m['drafts'][-1]['path']}`: {m['drafts'][-1]['status']}. No draft automatically advances the accepted edge. Continuation receipts and adopted chapter files are recorded in the manifest; never infer adoption from a revision filename alone.

## 3. The one status source
`foundation/CURRENT_STATE_MANIFEST.json`. STATUS_PANEL, this handoff, SERIAL_LOG and the overview are generated from it. Do not edit a generated mirror to repair state.

## 4. Locks
Exact typed messages and menu choices: `foundation/USER_LOCKS.json`. Read them before prose. Local laws: `foundation/NO_MISTAKE_LIVE_RULES.md`. Full Talent reference and source hash: `reference/`.

Settled: male native {i['species']}; extraordinary before prison under a red sun; adverse temperament from his specific power development. {m['background']['summary']} Further locks: technological capture; self-built full-access suppression with voluntary release; exhausted, seeking ordinary life; direct Cat staff; no initial knowledge of Kara's species. Names/apparent age were delegated and created.

Later author history: sentencing judge **{m["background"].get("sentencing_judge", "unassigned")}**. {m["background"].get("prisoner_recognition", "Recognition requires evidence.")} {m["background"].get("astra_non_acquaintance", "")}

Revised reading branch: {" → ".join(m.get("reading_branch",{}).get("paths",[])) or "See manifest"}. Status: {m.get("reading_branch",{}).get("status","see manifest")}. Author facts do not silently adopt revised prose.

## 5. Forbidden now
No invented reincarnation, System, universal immunity, low-power reset, automatic omniscience, wrongful-conviction rewrite, obligatory redemption, or automatic rage each time the seal is released. No cross-fandom mechanics. No claim to have watched episodes that were only researched through summaries.

## 6. Stale and draft material
The generic `dc-preparation/` predates the settled premise and is superseded for this story. R1-specific props are not automatically accepted continuity. Newer author directions, including the food gifts, take precedence over earlier draft-only assumptions. Preserve R1 during revision. Its accident memory is superseded by U09/U10 and flagged in coverage; do not import it into new scenes. Do not archive it as rejected unless the author actually rejects it.

## 7. Open threads and next action
Read the latest candidate’s review and prewrite record. Adopted chapters and their continuation receipts are listed in the manifest. The latest candidate’s discoveries remain separate until adopted. Open mechanism/date/feat/device matters are scoped in OPEN_DECISIONS; ask only when necessary to a scene. The latest candidate and review receipt are registered in the manifest; do not rely on an older statement that R2 does not exist. The expanded PROJECT_ATLAS indexes working designs, detailed relationships and separate timelines; they do not advance accepted chapters.

## 8. Do not re-litigate
Do not ask the author again for the choices already above. Do not treat the seal as loss of his real strength or assume Krypton could not capture him. Do not infer that the author's anger was about prose after they explicitly identified missing files.

## 9. Verification and delivery
`python3 tools/verify.py` checks structural state; `python3 tools/selftest.py` proves defect detection; `python3 tools/verify.py --ship {latest_chapter}` checks candidate release readiness: **{release_label}**. See `audits/VALIDATION.md`. Only after review and explicit acceptance should a chapter enter chapters/ and advance the manifest. Deliver files, coverage, state and receipts together. Nothing has been pushed to GitHub.
'''
    log = '# Serial log\n\nEvents are read from the manifest; do not maintain a second editable chronology here.\n\n'
    for e in m['events']:
        log += f"## {e['id']} — {e['date']} — {e['kind']}\n\n{e['description']}\n\n"
    log += f"Accepted chapter edge: {m['accepted_edge']}. Draft prose is not an accepted event.\n"
    status = '# File map\n\nGenerated project navigation. File presence does not imply approval or canon verification.\n\n'
    status += '\n'.join(f'- [{p}]({p})' for p in paths) + '\n'
    canon = '# Accepted canon ledger\n\nGenerated from the manifest, not from draft filenames.\n\n'
    canon += 'Epoch: ' + m['epoch'] + '\n\n'
    canon += 'Accepted beat IDs: ' + (', '.join(m['continuity']['accepted_canon_beats']) or 'none') + '\n\n'
    for chapter in m['accepted_chapters']:
        canon += '- Chapter ' + str(chapter['number']) + ': coverage `' + chapter['coverage'] + '`; acceptance date ' + chapter['accepted_on'] + '.\n'
    canon += '\nDraft-only coverage lives in canon_coverage/. It does not advance this ledger. The pilot map is a planning index, not an accepted span or complete episode-viewing receipt.\n'
    return {k: stamp + v for k, v in [('README.md', overview), ('HANDOFF.md', handoff), ('foundation/STATUS_PANEL.md', panel), ('foundation/SERIAL_LOG.md', log), ('foundation/CANON_LEDGER.md', canon), ('STATUS.md', status)]}

def render(root):
    for name, content in make_views(root).items():
        (root / name).write_text(content, encoding='utf8')

if __name__ == '__main__':
    render(ROOT)
    print('Generated six views from the current manifest.')
