#!/usr/bin/env python3
"""Cross-check expanded foundation records. Structural integrity, not canon truth."""
from pathlib import Path
import json
from render_codex import make_views
ROOT=Path(__file__).resolve().parents[1]
PROVENANCE={'user_lock','working_design','canon_summary','delegated_design','draft_event','accepted_event','open'}

def check(root=ROOT, check_views=True):
    errors=[]
    def load(name):
        try:return json.loads((root/name).read_text())
        except (OSError,ValueError):
            errors.append('DOMAIN_JSON: '+name);return {}
    def path_ok(name):
        try:
            if not isinstance(name,str) or Path(name).is_absolute():return False
            p=(root/name).resolve();p.relative_to(root.resolve())
            return p.is_file() and p.stat().st_size>0
        except (ValueError,TypeError):return False
    def unique(rows, label):
        ids=[r.get('id') for r in rows]
        if any(not x for x in ids) or len(set(ids))!=len(ids):errors.append(label+': duplicate/missing ID')
    contract=load('foundation/FILE_CONTRACT.json')
    required=contract.get('required_files',[])
    if not required:errors.append('DOMAIN_FILES: no expanded-file contract')
    for p in required:
        if not path_ok(p):errors.append('DOMAIN_FILES: missing/empty/unsafe '+str(p))
    m=load('foundation/CURRENT_STATE_MANIFEST.json')
    accepted_by_number={c.get('number'):c for c in m.get('accepted_chapters',[])}
    def accepted_source(row):
        c=accepted_by_number.get(row.get('source_chapter'))
        return c is not None and row.get('source_path')==c.get('path')
    entities=load('codex/ENTITIES.json').get('entities',[]);unique(entities,'ENTITY')
    ids={r.get('id') for r in entities}
    for r in entities:
        if not path_ok(r.get('profile')):errors.append('ENTITY: missing profile '+str(r.get('id')))
    rel=load('codex/RELATIONSHIP_LEDGER.json');rows=rel.get('relationships',[]);unique(rows,'RELATION')
    if rel.get('epoch')!=m.get('epoch'):errors.append('RELATION: wrong epoch')
    for r in rows:
        if r.get('from_entity') not in ids or r.get('to_entity') not in ids:errors.append('RELATION: unknown entity')
        if r.get('provenance') not in PROVENANCE:errors.append('RELATION: invalid provenance')
        if not all(r.get(k) for k in ('baseline','development','guard')):errors.append('RELATION: incomplete substantive entry')
        if m.get('accepted_edge')==0 and r.get('accepted_changes'):errors.append('RELATION: fabricated accepted change at edge zero')
        for delta in r.get('accepted_changes',[]):
            if not isinstance(delta,dict):
                errors.append('RELATION: malformed accepted delta');continue
            c=accepted_by_number.get(delta.get('chapter'))
            if not c or delta.get('path')!=c.get('path') or delta.get('sha256')!=c.get('sha256') or not delta.get('description'):
                errors.append('RELATION: accepted delta has no matching chapter receipt')
    kn=load('codex/KNOWLEDGE_LEDGER.json');rows=kn.get('records',[]);unique(rows,'KNOWLEDGE_LEDGER')
    if kn.get('epoch')!=m.get('epoch'):errors.append('KNOWLEDGE_LEDGER: wrong epoch')
    for r in rows:
        if r.get('observer') not in ids:errors.append('KNOWLEDGE_LEDGER: unknown observer')
        if r.get('state') not in {'known','unknown','not_established','suspected'}:errors.append('KNOWLEDGE_LEDGER: invalid state')
        if r.get('provenance') not in PROVENANCE or not r.get('evidence'):errors.append('KNOWLEDGE_LEDGER: missing provenance/evidence')
        if r.get('provenance')=='accepted_event' and not accepted_source(r):errors.append('KNOWLEDGE_LEDGER: invalid accepted source')
    if m.get('accepted_edge')==0:
        for fact in ['kara_kryptonian_identity','future_episode_events']:
            matching=[r for r in rows if r.get('observer')=='adrian' and r.get('fact')==fact]
            if len(matching)!=1 or matching[0].get('state')!='unknown':errors.append('KNOWLEDGE_LEDGER: opening lock mismatch '+fact)
    current=m.get('continuation_state',{})
    if current:
        expected_state='known' if current.get('kara_identity_known') else 'unknown'
        matches=[r for r in rows if r.get('observer')=='adrian' and r.get('fact')=='kara_kryptonian_identity']
        if len(matches)!=1 or matches[0].get('state')!=expected_state:errors.append('KNOWLEDGE_LEDGER: continuation state mismatch')
    future=[r for r in rows if r.get('observer')=='adrian' and r.get('fact')=='future_episode_events']
    if len(future)!=1 or future[0].get('state')!='unknown':errors.append('KNOWLEDGE_LEDGER: native character acquired future episode knowledge')
    ab=load('bible/ABILITY_REGISTRY.json');rows=ab.get('abilities',[]);unique(rows,'ABILITY')
    if ab.get('epoch')!=m.get('epoch'):errors.append('ABILITY: wrong epoch')
    for r in rows:
        if r.get('provenance') not in PROVENANCE or not all(r.get(k) for k in ('development','sealed_access','scope')):errors.append('ABILITY: unsupported/incomplete entry')
        if r.get('provenance')=='open' and r.get('development')!='unassigned':errors.append('ABILITY: unresolved capability falsely assigned')
    ch=load('timeline/OC_CHRONOLOGY.json');rows=ch.get('events',[]);unique(rows,'CHRONOLOGY')
    if ch.get('epoch')!=m.get('epoch'):errors.append('CHRONOLOGY: wrong epoch')
    events={r.get('id'):r for r in rows}
    for r in rows:
        if r.get('provenance') not in PROVENANCE:errors.append('CHRONOLOGY: invalid provenance')
        if r.get('provenance')=='accepted_event' and not accepted_source(r):errors.append('CHRONOLOGY: invalid accepted source')
        if any(x not in events for x in r.get('after',[])):errors.append('CHRONOLOGY: unknown predecessor')
    visiting=set();done=set()
    def visit(i):
        if i in visiting:return False
        if i in done or i not in events:return True
        visiting.add(i)
        for prev in events[i].get('after',[]):
            if not visit(prev):return False
        visiting.remove(i);done.add(i);return True
    if any(not visit(i) for i in events):errors.append('CHRONOLOGY: causal cycle')
    expected=contract.get('locked_history_order',[])
    for before,after in zip(expected,expected[1:]):
        if before not in events.get(after,{}).get('after',[]):errors.append('CHRONOLOGY: locked order changed '+before+' → '+after)
    designs=load('foundation/DESIGN_DECISIONS.json').get('designs',[]);unique(designs,'DESIGN')
    for d in designs:
        if not path_ok(d.get('path')):errors.append('DESIGN: missing specification')
        if d.get('status') not in {'working_design','author_approved','superseded'}:errors.append('DESIGN: invalid status')
        if (d.get('status')=='author_approved' or d.get('author_approval_recorded')) and not d.get('approval_receipt'):errors.append('DESIGN: invented approval without receipt')
    episodes=load('timeline/EPISODE_INDEX.json').get('episodes',[])
    pairs=[(r.get('season'),r.get('broadcast_episode')) for r in episodes]
    if len(set(pairs))!=len(pairs):errors.append('EPISODE: duplicate broadcast index')
    if len(episodes)!=contract.get('episode_metadata_count'):errors.append('EPISODE: metadata count changed')
    for r in episodes:
        if not all(r.get(k) for k in ('title','airdate','url')):errors.append('EPISODE: incomplete metadata')
    pair={r['broadcast_episode']:r['title'] for r in episodes if r.get('season')==1}
    if pair.get(4)!='Livewire' or pair.get(5)!='How Does She Do It?':errors.append('EPISODE: broadcast order overwritten by story order')
    # Author amendment U09/U10: compare substantive background mirrors, not prose keywords.
    locks=load('foundation/USER_LOCKS.json').get('locks',{})
    ancestry=locks.get('ancestry')
    if ancestry:
        identity=m.get('identity',{});background=m.get('background',{})
        if identity.get('ancestry')!=ancestry:errors.append('BACKGROUND: ancestry differs from author lock')
        if ancestry=={'father':'Kryptonian','mother':'Daxamite'} and identity.get('species')!='Kryptonian–Daxamite hybrid':
            errors.append('BACKGROUND: species label contradicts mixed ancestry')
        for field,lock in [('parental_status','parental_status'),('parents_death_kind','family_death_kind'),('destroyed_city_world','destroyed_city_world'),('parents_murder_world','parents_murder_world')]:
            if background.get(field)!=locks.get(lock):errors.append('BACKGROUND: manifest mismatch '+field)
        if events.get('T01',{}).get('ancestry')!=ancestry:errors.append('BACKGROUND: birth chronology mismatch')
        if events.get('T03',{}).get('cause')!=locks.get('family_death_kind'):errors.append('BACKGROUND: family-loss chronology mismatch')
        if events.get('T04',{}).get('world')!=locks.get('destroyed_city_world'):errors.append('BACKGROUND: catastrophe world mismatch')
        records={d.get('id'):d for d in designs}
        if records.get('D03',{}).get('status')!='superseded':errors.append('BACKGROUND: superseded D03 revived')
        if records.get('D08',{}).get('status')!='author_approved':errors.append('BACKGROUND: approved D08 scope lost')
    # U15/U16 are author background, not acceptance of newly generated prose.
    evidence_ids={x.get('id') for x in load('foundation/USER_LOCKS.json').get('evidence',[])}
    if {'U15','U16'} <= evidence_ids:
        for field in ('sentencing_judge','prisoner_recognition'):
            if not locks.get(field) or m.get('background',{}).get(field)!=locks[field]:
                errors.append('RESCUE_HISTORY: author/background mismatch '+field)
        knowledge={(x.get('observer'),x.get('fact')):x for x in kn.get('records',[])}
        for observer,fact in [('adrian','alura_sentenced_him'),('adrian','astra_non_personal_prison_acquaintance'),('adrian','kara_zor_el_family_recognition'),('astra','kael_identity_and_fear'),('non','kael_identity_and_fear'),('vartox','kael_identity_and_fear')]:
            row=knowledge.get((observer,fact),{})
            if row.get('state')!='known' or row.get('provenance')!='user_lock':
                errors.append('RESCUE_HISTORY: missing author knowledge '+observer+'/'+fact)
        relationships={x.get('id'):x for x in rel.get('relationships',[])}
        for ident,other in [('R07','astra'),('R17','non'),('R18','vartox')]:
            row=relationships.get(ident,{})
            if row.get('provenance')!='user_lock' or row.get('to_entity')!=other:
                errors.append('RESCUE_HISTORY: missing author relationship '+ident)
    if 'U23' in evidence_ids:
        policy = locks.get('public_identity_policy', {})
        if m.get('identity', {}).get('public_identity_policy') != policy:
            errors.append('PUBLIC_IDENTITY: manifest differs from U23 costume/concealment lock')
        if policy.get('reference_exists_in_story') is not False or not policy.get('complete_suit_and_mask') or not policy.get('deliberate_concealment'):
            errors.append('PUBLIC_IDENTITY: U23 scope lost; visual reference is not an in-world character')
    if check_views:
        try:
            for path,text in make_views(root).items():
                if not (root/path).is_file() or (root/path).read_text()!=text:errors.append('CODEX_VIEW: stale '+path)
        except (KeyError,TypeError,ValueError,OSError) as e:errors.append('CODEX_VIEW: cannot render '+str(e))
    return errors

if __name__=='__main__':
    errors=check()
    for e in errors:print('FAIL:',e)
    print('FOUNDATION: '+('FAIL' if errors else 'PASS — files, references, ledgers, causal order and view synchronization'))
    raise SystemExit(1 if errors else 0)
