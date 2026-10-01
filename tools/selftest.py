#!/usr/bin/env python3
"""Inject known defects in disposable copies. Never changes the live project."""
from pathlib import Path
import hashlib
import json
import shutil
import tempfile
from verify import ROOT, validate, ship, sha, REVIEWS, release_checks
from render_state import render

passed = 0
failed = 0

def write_json(p, value):
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def mutate_manifest(root, operation):
    p = root/'foundation/CURRENT_STATE_MANIFEST.json'
    m = json.loads(p.read_text()); operation(m); write_json(p, m)

def mutate_coverage(root, operation):
    m = json.loads((root/'foundation/CURRENT_STATE_MANIFEST.json').read_text())
    p = root/m['drafts'][-1]['coverage']
    cv = json.loads(p.read_text()); operation(cv); write_json(p, cv)

def ready_fixture(root):
    # Synthetic machine-check fixture, NOT a story review or author approval.
    p = root/'audits/SYNTHETIC_TEST_REVIEW.md'
    p.write_text('Synthetic gate fixture. Not real canon verification or user acceptance.\n')
    def prepare(cv):
        cv['release_ready'] = True
        cv['continuity_conflicts'] = []  # Synthetic fixture only, not a real correction.
        cv['beats'] = [{'id':'SG-P01','status':'covered'}]
        for k in REVIEWS:
            cv['reviews'][k] = 'pass'
        cv['review_receipts'] = {k:{'path':str(p.relative_to(root)),'sha256':sha(p)} for k in REVIEWS}
    mutate_coverage(root, prepare)

def accepted_fixture(root):
    # Preserve the real multi-chapter shape; substitute receipts only in this copy.
    ready_fixture(root)
    m = json.loads((root/'foundation/CURRENT_STATE_MANIFEST.json').read_text())
    assert m['accepted_chapters'], 'Synthetic accepted-ledger test needs an adopted chapter'
    for chapter in m['accepted_chapters']:
        chapter['acceptance_receipt'] = 'SYNTHETIC TEST ONLY — not real approval'
        chapter['accepted_on'] = '2026-09-28'
    write_json(root/'foundation/CURRENT_STATE_MANIFEST.json', m)

def case(name, mutation, expected=None, release=False, clean=False, release_revision=None):
    global passed, failed
    with tempfile.TemporaryDirectory(prefix='supergirl-gate-selftest-') as td:
        root = Path(td)/'project'
        shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        mutation(root)
        if release and release_revision:
            m = json.loads((root/'foundation/CURRENT_STATE_MANIFEST.json').read_text())
            d = next(d for d in m['drafts'] if d['revision']==release_revision)
            errors = release_checks(root,m,json.loads((root/d['coverage']).read_text()))
        else:
            latest=json.loads((root/'foundation/CURRENT_STATE_MANIFEST.json').read_text())['drafts'][-1]['chapter']
            errors = ship(root, latest) if release else validate(root, check_views=False)[0]
        ok = not errors if clean else any(x.startswith(expected) for x in errors)
        if ok:
            passed += 1; print('PASS:',name)
        else:
            failed += 1; print('FAIL:',name,errors)

case('clean structural project passes', lambda r: None, clean=True)
case('unregistered interrupted draft caught', lambda r: (r/'drafts/Chapter_99_Orphan_R1.md').write_text('Unregistered draft\n'), 'UNREGISTERED_DRAFT:')
case('missing required foundation caught', lambda r: (r/'bible/SEALING_DEVICE.md').unlink(), 'REQUIRED:')
case('invalid JSON caught', lambda r: (r/'foundation/USER_LOCKS.json').write_text('{bad'), 'JSON:')
case('wrong next chapter caught', lambda r: mutate_manifest(r, lambda m: m.update(next_chapter=m['accepted_edge'])), 'NEXT:')
case('false accepted edge caught', lambda r: mutate_manifest(r, lambda m: m.update(accepted_edge=m['accepted_edge']+1,next_chapter=m['next_chapter']+1)), 'EDGE:')
case('changed draft hash caught', lambda r: (r/'drafts/Chapter_01_Adrian_Vale_R1.md').write_text('Altered\n'), 'DRAFT_HASH:')
case('changed master reference caught', lambda r: (r/'reference/talent_master_v2.md').write_text('Altered\n'), 'REFERENCE:')
case('opening identity knowledge leak caught', lambda r: mutate_manifest(r, lambda m: m['opening_state'].update(kara_identity_known=True)), 'KNOWLEDGE:')
case('opening foreknowledge leak caught', lambda r: mutate_manifest(r, lambda m: m['opening_state'].update(canon_foreknowledge=True)), 'KNOWLEDGE:')
case('stale epoch coverage caught', lambda r: mutate_coverage(r, lambda cv: cv.update(epoch='old-epoch')), 'EPOCH:')
case('unregistered accepted chapter caught', lambda r: (r/'chapters/Chapter_01_Orphan.md').write_text('Not accepted\n'), 'UNREGISTERED:')
case('accepted source-union mismatch caught', lambda r: mutate_manifest(r, lambda m: m['continuity'].update(accepted_canon_beats=['SG-P01'])), 'COVERAGE:')
case('competing state authority caught', lambda r: mutate_manifest(r, lambda m: m['source_authority'].update(current_state='other.json')), 'AUTHORITY:')
case('path traversal caught', lambda r: mutate_manifest(r, lambda m: m['drafts'][0].update(path='../outside.md')), 'DRAFT_RECORD:')
case('historical R1 release remains blocked', lambda r: None, 'SHIP_READY:', release=True, release_revision='R1')
case('unreviewed latest candidate cannot ship', lambda r: mutate_coverage(r,lambda cv:cv.update(release_ready=False)), 'SHIP_READY:', release=True)
case('incomplete canon span caught', lambda r: mutate_coverage(r, lambda cv: cv.update(release_ready=True,beats=[{'id':'SG-P01','status':'missing'}])), 'SHIP_BEATS:', release=True)
case('missing review receipts caught', lambda r: mutate_coverage(r, lambda cv: cv.update(release_ready=True,review_receipts={})), 'SHIP_RECEIPT:', release=True)
case('complete synthetic release fixture passes', ready_fixture, release=True, clean=True)
case('complete synthetic accepted ledger passes', accepted_fixture, clean=True)

def no_approval(r):
    accepted_fixture(r)
    mutate_manifest(r, lambda m: m['accepted_chapters'][0].pop('acceptance_receipt'))
case('missing acceptance receipt caught', no_approval, 'ACCEPTANCE:')

def stale_test():
    global passed, failed
    with tempfile.TemporaryDirectory(prefix='supergirl-mirror-test-') as td:
        r=Path(td)/'project'
        shutil.copytree(ROOT,r,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        render(r)
        (r/'foundation/STATUS_PANEL.md').write_text('Stale panel\n')
        errors=validate(r,check_views=True)[0]
        if any(x.startswith('MIRROR:') for x in errors):
            passed+=1;print('PASS: stale generated panel caught')
        else:
            failed+=1;print('FAIL: stale generated panel',errors)
stale_test()
def change_json(root, path, operation):
    p=root/path; value=json.loads(p.read_text()); operation(value); write_json(p,value)

case('relationship entity reference checked', lambda r: change_json(r,'codex/RELATIONSHIP_LEDGER.json',lambda d:d['relationships'][0].update(to_entity='nonexistent')), 'RELATION:')
case('unaccepted relationship event checked', lambda r: change_json(r,'codex/RELATIONSHIP_LEDGER.json',lambda d:d['relationships'][0].update(accepted_changes=['invented event'])), 'RELATION:')
case('knowledge ledger cannot bypass opening lock', lambda r: change_json(r,'codex/KNOWLEDGE_LEDGER.json',lambda d:d['records'][0].update(state='unknown' if d['records'][0]['state']=='known' else 'known')), 'KNOWLEDGE_LEDGER:')
case('chronology causal cycle checked', lambda r: change_json(r,'timeline/OC_CHRONOLOGY.json',lambda d:d['events'][0].update(after=['T05'])), 'CHRONOLOGY:')
case('locked family-loss/rampage order checked', lambda r: change_json(r,'timeline/OC_CHRONOLOGY.json',lambda d:d['events'][3].update(after=['T01'])), 'CHRONOLOGY:')
# Inject both incompatible fields by stable ID; the last row may be a valid new author lock.
case('unresolved ability cannot be marked achieved', lambda r: change_json(r,'bible/ABILITY_REGISTRY.json',lambda d:next(x for x in d['abilities'] if x['id']=='A10').update(provenance='open',development='confirmed')), 'ABILITY:')
case('design approval needs a receipt', lambda r: change_json(r,'foundation/DESIGN_DECISIONS.json',lambda d:d['designs'][0].update(author_approval_recorded=True)), 'DESIGN:')
case('broadcast/story order distinction checked', lambda r: change_json(r,'timeline/EPISODE_INDEX.json',lambda d:d['episodes'][3].update(title='How Does She Do It?')), 'EPISODE:')
case('duplicate character IDs checked', lambda r: change_json(r,'codex/ENTITIES.json',lambda d:d['entities'].append(d['entities'][0].copy())), 'ENTITY:')

case('hybrid ancestry mirror checked', lambda r: mutate_manifest(r,lambda m:m['identity']['ancestry'].update(mother='Kryptonian')), 'BACKGROUND:')
case('obsolete pure-Kryptonian species label caught', lambda r: mutate_manifest(r,lambda m:m['identity'].update(species='Kryptonian')), 'BACKGROUND:')
case('parental standing mirror checked', lambda r: mutate_manifest(r,lambda m:m['background']['parental_status'].update(father='king of Krypton')), 'BACKGROUND:')
case('obsolete accident background caught', lambda r: mutate_manifest(r,lambda m:m['background'].update(parents_death_kind='accident')), 'BACKGROUND:')
case('wrong catastrophe world caught', lambda r: mutate_manifest(r,lambda m:m['background'].update(destroyed_city_world='Daxam')), 'BACKGROUND:')
case('obsolete accident chronology caught', lambda r: change_json(r,'timeline/OC_CHRONOLOGY.json',lambda d:d['events'][2].update(cause='accident')), 'BACKGROUND:')
case('wrong catastrophe chronology world caught', lambda r: change_json(r,'timeline/OC_CHRONOLOGY.json',lambda d:d['events'][3].update(world='Daxam')), 'BACKGROUND:')
case('superseded family proposal cannot revive silently', lambda r: change_json(r,'foundation/DESIGN_DECISIONS.json',lambda d:d['designs'][2].update(status='working_design')), 'BACKGROUND:')
def unresolved_conflict(r):
    ready_fixture(r)
    mutate_coverage(r,lambda cv:cv.update(continuity_conflicts=[{'id':'RC01','description':'synthetic unresolved conflict'}]))
case('review flags do not clear a continuity conflict', unresolved_conflict, 'SHIP_CONTINUITY:', release=True)

case('changed adopted chapter bytes caught', lambda r:(r/'chapters/Chapter_01_Adrian_Vale.md').write_text('tampered'), 'ACCEPTED_HASH:')
case('relationship delta source receipt checked', lambda r:change_json(r,'codex/RELATIONSHIP_LEDGER.json',lambda d:d['relationships'][0]['accepted_changes'][0].update(chapter=999)), 'RELATION:')
case('accepted knowledge source receipt checked', lambda r:change_json(r,'codex/KNOWLEDGE_LEDGER.json',lambda d:next(x for x in d['records'] if x['provenance']=='accepted_event').update(source_chapter=999)), 'KNOWLEDGE_LEDGER:')
case('accepted chronology source receipt checked', lambda r:change_json(r,'timeline/OC_CHRONOLOGY.json',lambda d:next(x for x in d['events'] if x['provenance']=='accepted_event').update(source_chapter=999)), 'CHRONOLOGY:')

case('Alura sentencing mirror cannot revert', lambda r:mutate_manifest(r,lambda m:m['background'].update(sentencing_judge=None)), 'RESCUE_HISTORY:')
case('universal prisoner recognition cannot revert', lambda r:mutate_manifest(r,lambda m:m['background'].update(prisoner_recognition='unestablished')), 'RESCUE_HISTORY:')
case('Vartox author knowledge cannot revert', lambda r:change_json(r,'codex/KNOWLEDGE_LEDGER.json',lambda d:next(x for x in d['records'] if x['id']=='K32').update(state='unknown')), 'RESCUE_HISTORY:')
case('Astra acquaintance cannot become speculative', lambda r:change_json(r,'codex/RELATIONSHIP_LEDGER.json',lambda d:next(x for x in d['relationships'] if x['id']=='R07').update(provenance='working_design')), 'RESCUE_HISTORY:')
case('Non acquaintance cannot disappear', lambda r:change_json(r,'codex/RELATIONSHIP_LEDGER.json',lambda d:d.update(relationships=[x for x in d['relationships'] if x['id']!='R17'])), 'RESCUE_HISTORY:')
case('family recognition cannot become unknown', lambda r:change_json(r,'codex/KNOWLEDGE_LEDGER.json',lambda d:next(x for x in d['records'] if x['id']=='K29').update(state='unknown')), 'RESCUE_HISTORY:')

case('U23 complete suit cannot silently disappear', lambda r:mutate_manifest(r,lambda m:m['identity']['public_identity_policy'].update(complete_suit_and_mask=False)), 'PUBLIC_IDENTITY:')
case('visual reference cannot become in-world character', lambda r:mutate_manifest(r,lambda m:m['identity']['public_identity_policy'].update(reference_exists_in_story=True)), 'PUBLIC_IDENTITY:')

print(f'\nSELFTEST: {passed}/{passed+failed} passed; {failed} failed')
raise SystemExit(1 if failed else 0)
