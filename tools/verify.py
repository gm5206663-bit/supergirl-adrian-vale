#!/usr/bin/env python3
"""Local structural gate and separate release gate. Neither replaces literary/canon review."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys
from render_state import make_views
from verify_foundation import check as check_foundation

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
 'AGENTS.md', 'NOTICE.md', 'README.md', 'HANDOFF.md', 'STATUS.md', 'MASTER_PROJECT_BIBLE.md',
 'foundation/CURRENT_STATE_MANIFEST.json', 'foundation/STATUS_PANEL.md', 'foundation/SERIAL_LOG.md',
 'foundation/USER_LOCKS.json', 'foundation/NO_MISTAKE_LIVE_RULES.md', 'foundation/STYLE_LAW.md',
 'foundation/OPEN_DECISIONS.md', 'foundation/DC_TIMELINE.md', 'foundation/CONTINUITY.md',
 'foundation/DELIVERY_WORKFLOW.md', 'foundation/PREWRITE_Chapter_01_R2.md',
 'bible/CHARACTER_ADRIAN_VALE.md', 'bible/ADAPTATION_TALENT_LOCAL_DC.md',
 'bible/POWER_FOUNDATION.md', 'bible/SEALING_DEVICE.md',
 'codex/KNOWLEDGE_FIREWALL.md', 'codex/CAST_AND_RELATIONSHIPS.md', 'codex/BUTTERFLY_REGISTRY.md',
 'canon_coverage/SOURCE_REGISTER.md', 'canon_coverage/PILOT_BEAT_MAP.md',
 'reference/talent_master_v2.md', 'reference/GITHUB_SOURCE_RECEIPTS.json',
 'audits/CHAPTER_01_RETROSPECTIVE.md', 'audits/MISTAKES_AND_CORRECTIONS.md',
 'tools/render_state.py', 'tools/verify.py', 'tools/selftest.py',
 'drafts/README.md', 'chapters/README.md'
]
REVIEWS = ('canon', 'continuity', 'power', 'knowledge', 'prose')
SECRET = re.compile(rb'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def local(root, value):
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError('not a relative path')
    p = (root / value).resolve()
    p.relative_to(root.resolve())
    return p

def validate(root=ROOT, check_views=True):
    errors, warnings = [], []
    for name in REQUIRED:
        p = root / name
        if not p.is_file() or not p.stat().st_size:
            errors.append('REQUIRED: ' + name)
    parsed = {}
    for p in root.rglob('*.json'):
        try:
            parsed[str(p.relative_to(root))] = json.loads(p.read_text(encoding='utf8'))
        except (ValueError, UnicodeError) as e:
            errors.append('JSON: ' + str(p.relative_to(root)) + ': ' + str(e))
    m = parsed.get('foundation/CURRENT_STATE_MANIFEST.json')
    if not isinstance(m, dict):
        return errors + ['MANIFEST: missing valid object'], warnings
    fields = {'schema_version','project_id','epoch','revision','identity','opening_state','accepted_edge','next_chapter','accepted_chapters','drafts','source_authority','events','release','continuity','remote','updated_on','phase','open_items'}
    if not fields.issubset(m):
        return errors + ['SCHEMA: missing fields ' + ', '.join(sorted(fields - set(m)))], warnings
    if m['schema_version'] != 1 or not isinstance(m['epoch'], str) or not m['epoch']:
        errors.append('SCHEMA: version or epoch invalid')
    edge = m['accepted_edge']
    if type(edge) is not int or edge < 0:
        return errors + ['EDGE: invalid accepted edge'], warnings
    if m['next_chapter'] != edge + 1:
        errors.append('NEXT: next chapter does not follow accepted edge')
    if m['source_authority'].get('current_state') != 'foundation/CURRENT_STATE_MANIFEST.json':
        errors.append('AUTHORITY: competing current-state source')
    if m['remote'].get('configured') and not m['remote'].get('repository'):
        errors.append('REMOTE: configured without a repository')
    if not isinstance(m['events'], list) or not m['events']:
        errors.append('LOG: no event receipt')
    else:
        ids = [e.get('id') for e in m['events']]
        if len(set(ids)) != len(ids) or any(not e.get('description') or not e.get('date') for e in m['events']):
            errors.append('LOG: duplicate or incomplete event')
    locks = parsed.get('foundation/USER_LOCKS.json', {})
    if not locks.get('locks') or not locks.get('evidence'):
        errors.append('LOCKS: no recorded author evidence')
    ref = root / 'reference/talent_master_v2.md'
    receipts = parsed.get('reference/GITHUB_SOURCE_RECEIPTS.json', {}).get('records', [])
    matches = [r for r in receipts if r.get('path') == 'reference/talent_master_v2.md']
    if len(matches) != 1:
        errors.append('REFERENCE: missing master receipt')
    elif not ref.is_file() or sha(ref) != matches[0].get('sha256') or m['source_authority'].get('talent_master_sha256') != matches[0].get('sha256'):
        errors.append('REFERENCE: Talent master hash mismatch')
    # Opening snapshot is historical; later discoveries belong to continuation state.
    s = m['opening_state']
    if s.get('seal') != 'engaged' or s.get('voluntary_release') is not True:
        errors.append('OPENING: historical seal snapshot violates author lock')
    if s.get('kara_identity_known') is not False or s.get('canon_foreknowledge') is not False:
        errors.append('KNOWLEDGE: opening knowledge lock violated')
    if edge == 0 and m['continuity'].get('accepted_canon_beats'):
        errors.append('COVERAGE: source beats consumed with no accepted chapter')
    accepted = m['accepted_chapters']
    if not isinstance(accepted, list) or not isinstance(m['drafts'], list):
        return errors + ['SCHEMA: chapter records must be arrays'], warnings
    nums = [c.get('number') for c in accepted]
    if any(type(n) is not int for n in nums) or sorted(nums) != list(range(1, edge + 1)):
        errors.append('EDGE: accepted ledger is not the exact contiguous sequence')
    registered = set()
    accepted_beats = set()
    for c in accepted:
        try:
            rel = c['path']; p = local(root, rel)
            if not re.fullmatch(r'chapters/Chapter_\d{2,}_[^/]+\.md', rel):
                errors.append('ACCEPTED_PATH: not a numbered accepted chapter')
            registered.add(rel)
            if c.get('epoch') != m['epoch']:
                errors.append('EPOCH: accepted chapter belongs to another epoch')
            if not p.is_file() or sha(p) != c.get('sha256'):
                errors.append('ACCEPTED_HASH: missing or changed chapter ' + rel)
            if not c.get('acceptance_receipt') or not c.get('accepted_on'):
                errors.append('ACCEPTANCE: missing author receipt or date')
            coverage_path = local(root, c['coverage'])
            cv = json.loads(coverage_path.read_text())
            if not cv.get('accepted') or cv.get('epoch') != m['epoch'] or cv.get('chapter') != c.get('number'):
                errors.append('COVERAGE: accepted chapter coverage scope mismatch')
            if cv.get('draft_sha256') != c.get('sha256'):
                errors.append('COVERAGE: accepted content is not the reviewed content')
            errors.extend(release_checks(root, m, cv))
            accepted_beats.update(b['id'] for b in cv.get('beats', []) if b.get('status') in ('covered','changed_with_receipt'))
            if p.is_file():
                story = p.read_text()
                if ',,' in story or 'details in STATUS.md' in story:
                    errors.append('PROSE: punctuation/editorial leakage in accepted prose')
                if re.search(r'\b(?:soul rings?|martial souls?|IATS|IODS)\b', story, re.I):
                    errors.append('SCOPE: possible cross-fandom mechanics in accepted prose; review required')
        except (KeyError, ValueError, OSError, TypeError) as e:
            errors.append('ACCEPTED_RECORD: ' + str(e))
    on_disk = {str(p.relative_to(root)) for p in (root / 'chapters').glob('Chapter_*.md')}
    if on_disk != registered:
        errors.append('UNREGISTERED: accepted chapter directory and ledger differ')
    if set(m['continuity'].get('accepted_canon_beats', [])) != accepted_beats:
        errors.append('COVERAGE: accepted beat union and manifest differ')
    declared_drafts = {d.get("path") for d in m["drafts"]}
    disk_drafts = {str(p.relative_to(root)) for p in (root / "drafts").glob("Chapter_*.md")}
    if disk_drafts != declared_drafts:
        errors.append("UNREGISTERED_DRAFT: draft directory and manifest differ")
    draft_ids = []
    for d in m['drafts']:
        try:
            p = local(root, d['path']); cvp = local(root, d['coverage'])
            if not d['path'].startswith('drafts/'):
                errors.append('DRAFT_PATH: draft outside drafts/')
            if not p.is_file() or sha(p) != d.get('sha256'):
                errors.append('DRAFT_HASH: changed or missing draft')
            cv = json.loads(cvp.read_text())
            if cv.get('epoch') != m['epoch']:
                errors.append('EPOCH: draft coverage belongs to another epoch')
            if cv.get('draft_sha256') != d.get('sha256') or cv.get('draft_path') != d['path']:
                errors.append('DRAFT_COVERAGE: wrong reviewed draft')
            if cv.get('chapter') != d.get('chapter') or cv.get('revision') != d.get('revision'):
                errors.append('DRAFT_COVERAGE: number/revision mismatch')
            draft_ids.append((d.get('chapter'),d.get('revision')))
        except (KeyError, ValueError, OSError, TypeError) as e:
            errors.append('DRAFT_RECORD: ' + str(e))
    if len(set(draft_ids)) != len(draft_ids):
        errors.append('DRAFT_RECORD: duplicate chapter revision')
    for p in root.rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and SECRET.search(p.read_bytes()):
            errors.append('SECRET: recognizable credential pattern in ' + str(p.relative_to(root)))
    if check_views:
        try:
            for name, expected in make_views(root).items():
                if not (root/name).is_file() or (root/name).read_text() != expected:
                    errors.append('MIRROR: stale generated ' + name)
        except (KeyError, TypeError, ValueError) as e:
            errors.append('MIRROR: cannot render malformed state: ' + str(e))
    errors.extend(check_foundation(root, check_views=check_views))
    if not accepted:
        warnings.append('No accepted chapters. Structural PASS is not a chapter quality/acceptance result.')
    warnings.append('No full episode viewing, literary quality, or complete security audit is established by this script.')
    return errors, warnings

def release_checks(root, m, cv):
    errors = []
    if cv.get('epoch') != m['epoch']:
        errors.append('SHIP_EPOCH: coverage epoch mismatch')
    if cv.get('continuity_conflicts'):
        errors.append('SHIP_CONTINUITY: unresolved recorded continuity conflict')
    if cv.get('release_ready') is not True:
        errors.append('SHIP_READY: candidate is not marked review-complete')
    sources = cv.get('sources', [])
    if not sources or any(not all(s.get(k) for k in ('id','url','title','accessed','verification')) for s in sources):
        errors.append('SHIP_SOURCE: incomplete source receipts')
    beats = cv.get('beats', [])
    valid = {'covered','changed_with_receipt','outside_span','not_shown_by_source'}
    if not beats or any(b.get('status') not in valid for b in beats):
        errors.append('SHIP_BEATS: missing, partial, or unverified source coverage')
    if not any(b.get('status') in ('covered','changed_with_receipt') for b in beats):
        errors.append('SHIP_BEATS: no verified in-span beat')
    if len({b.get('id') for b in beats}) != len(beats):
        errors.append('SHIP_BEATS: duplicate beat IDs')
    for b in beats:
        if b.get('status') in ('changed_with_receipt','not_shown_by_source') and not b.get('reason'):
            errors.append('SHIP_BEATS: changed/omitted beat has no reason')
    refs = cv.get('review_receipts', {})
    for key in REVIEWS:
        if cv.get('reviews', {}).get(key) != 'pass':
            errors.append('SHIP_REVIEW: ' + key + ' review incomplete')
        try:
            r = refs[key]; p = local(root, r['path'])
            if not p.is_file() or not p.stat().st_size or sha(p) != r['sha256']:
                errors.append('SHIP_RECEIPT: missing/changed ' + key + ' evidence')
        except (KeyError, ValueError, TypeError):
            errors.append('SHIP_RECEIPT: missing ' + key + ' evidence')
    return errors

def ship(root, chapter):
    try:
        m = json.loads((root/'foundation/CURRENT_STATE_MANIFEST.json').read_text())
        drafts = [d for d in m['drafts'] if d.get('chapter') == chapter]
        if not drafts:
            return ['SHIP_DRAFT: no registered candidate']
        d = drafts[-1]
        cv = json.loads(local(root, d['coverage']).read_text())
        return release_checks(root, m, cv)
    except (ValueError, KeyError, OSError, TypeError) as e:
        return ['SHIP_SCHEMA: ' + str(e)]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ship', type=int, help='separate release readiness for latest registered revision of chapter')
    args = parser.parse_args()
    errors, warnings = validate(ROOT)
    for x in warnings:
        print('NOTE:', x)
    for x in errors:
        print('FAIL:', x)
    if errors:
        print('STRUCTURE: FAIL')
        sys.exit(1)
    print('STRUCTURE: PASS — layout, state, hashes, references and generated mirrors checked')
    if args.ship is not None:
        blocks = ship(ROOT, args.ship)
        for b in blocks:
            print('BLOCK:', b)
        if blocks:
            print('RELEASE: BLOCKED — not an accepted chapter')
            sys.exit(2)
        print('RELEASE: TECHNICALLY READY — recorded reviews present; author acceptance remains separate')
    sys.exit(0)
