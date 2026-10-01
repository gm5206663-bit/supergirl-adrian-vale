#!/usr/bin/env python3
"""Generate readable domain ledgers; JSON inputs remain the editable records."""
from pathlib import Path
import hashlib
import json
ROOT = Path(__file__).resolve().parents[1]

def load(root, name):
    return json.loads((root/name).read_text())

def wrap(root, path, content):
    digest = hashlib.sha256((root/path).read_bytes()).hexdigest()
    return f'<!-- GENERATED from {path}; SHA256: {digest} -->\n\n' + content.strip() + '\n'

def make_views(root):
    entities = {x['id']:x['name'] for x in load(root,'codex/ENTITIES.json')['entities']}
    r = load(root,'codex/RELATIONSHIP_LEDGER.json')
    text = '# Relationships — opening baselines and accepted changes\n\n'
    text += 'Epoch: ' + r['epoch'] + '. ' + r['anchor'] + '.\n\n'
    text += '**Romance:** ' + (r['romance_selection'] or 'not selected; no pairing implied by attraction or proximity') + '.\n\n'
    text += 'The entries distinguish author locks, source summaries and working designs. Changes require events and evidence, not invented affection scores. Source-side relationship context: ' + r['source_notes'] + '\n\n'
    for x in r['relationships']:
        text += f"## {x['id']} — {entities[x['from_entity']]} / {entities[x['to_entity']]}\n\n"
        text += f"**Type:** {x['kind']} · **Provenance:** {x['provenance']}\n\n"
        text += f"- **Opening baseline:** {x['baseline']}\n- **Possible development:** {x['development']}\n- **Boundary:** {x['guard']}\n- **Accepted changes:** {len(x['accepted_changes'])}\n\n"
        for delta in x['accepted_changes']:
            text += f"Accepted Chapter {delta['chapter']}: {delta['description']}\n\n"
    text += '## Updating a relationship\n\nRecord an interaction, who interpreted it, whether interpretation was mutual, what changed, and the accepted source scene. Respect, attraction, trust, knowledge and professional authority are separate dimensions. Do not collapse them into a single score.\n'
    views = {'codex/RELATIONSHIPS.md':wrap(root,'codex/RELATIONSHIP_LEDGER.json',text)}
    k = load(root,'codex/KNOWLEDGE_LEDGER.json')
    text = '# Knowledge-state ledger\n\n' + k.get('anchor','Opening records') + '. Unknown is not impossible; a later discovery needs evidence.\n\n'
    for x in k['records']:
        text += f"## {x['id']} — {entities[x['observer']]}: {x['fact']}\n\n**State:** {x['state']} · **Provenance:** {x['provenance']}\n\n{x['evidence']}\n\n"
    views['codex/KNOWLEDGE_STATE.md'] = wrap(root,'codex/KNOWLEDGE_LEDGER.json',text)
    a = load(root,'bible/ABILITY_REGISTRY.json')
    text = '# Ability ledger\n\n' + a['scope'] + '.\n\n'
    for x in a['abilities']:
        text += f"## {x['id']} — {x['name']}\n\n- **Provenance:** {x['provenance']}\n- **Development claim:** {x['development']}\n- **While sealed:** {x['sealed_access']}\n- **Scope:** {x['scope']}\n\n"
        if x.get('accepted_evidence'):
            ev = x['accepted_evidence']
            text += f"**Accepted evidence — Chapter {ev['chapter']}:** {ev['description']} Source: `{ev['path']}`.\n\n"
    text += 'No numeric combat ceiling, universal immunity or Talent Order is implied. Accepted feats above are distinct from the wider proposed suite.\n'
    views['bible/ABILITY_LEDGER.md'] = wrap(root,'bible/ABILITY_REGISTRY.json',text)
    c = load(root,'timeline/OC_CHRONOLOGY.json')
    text = '# OC chronology — ordered history\n\n' + c['calendar_policy'] + '.\n\n'
    for x in c['events']:
        text += f"## {x['id']} — {x['title']}\n\n**After:** {', '.join(x['after']) or 'origin'} · **Provenance:** {x['provenance']} · **Date/anchor:** {x['date_anchor'] or 'not assigned'}\n\n{x['description']}\n\n"
    text += 'Draft revisions are alternative candidates, not accepted continuation. Relative order does not convert prison stasis into lived years.\n'
    views['timeline/OC_CHRONOLOGY.md'] = wrap(root,'timeline/OC_CHRONOLOGY.json',text)
    d = load(root,'foundation/DESIGN_DECISIONS.json')
    text = '# Working-design register\n\n' + d['status_policy'] + '\n\n'
    for x in d['designs']:
        text += f"## {x['id']} — {x['title']}\n\n**Status:** {x['status']} · **Author approval recorded:** {x['author_approval_recorded']}\n\nSpecification: `{x['path']}`. Addresses: {', '.join(x['resolves_in_part']) or 'prospective planning'} .\n\n"
        if x.get('approval_receipt'):
            text += f"Approval receipt: {x['approval_receipt']}.\n\nScope: {x.get('approval_scope', 'See receipt')}.\n\n"
        if x.get('superseded_by'):
            text += f"Superseded by: {x['superseded_by']}.\n\n"
    views['foundation/DESIGN_REGISTER.md'] = wrap(root,'foundation/DESIGN_DECISIONS.json',text)
    return views

if __name__ == '__main__':
    for name, content in make_views(ROOT).items():
        (ROOT/name).write_text(content)
    print('Generated five domain-ledger views.')
