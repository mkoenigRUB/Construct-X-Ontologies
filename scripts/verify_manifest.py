import glob, json, os, re
import rdflib

mani = json.load(open('MANIFEST.json', encoding='utf-8'))
OWL = rdflib.Namespace('http://www.w3.org/2002/07/owl#')

def path_for(section, key):
    if section == 'domain_ontologies':
        return f'{key}/{key}-ontology.ttl'
    if section == 'core_ontologies':
        return f'core-ontologies/{key}.ttl'
    if section == 'link_ontologies':
        return f'link-ontologies/{key}.ttl'
    if section == 'schedule_vocabularies':
        return f'construction-schedule/vocab/{key}.ttl'
    if section == 'breakdown_vocabularies':
        return f'breakdown-structure/{key}.ttl'
    if section == 'boq_vocabularies':
        return f'gaeb-boq/{key}-vocab.ttl'
    if section == 'site_vocabularies':
        return f'construction-site/construction-site-{key}.ttl'
    if section == 'delivery_vocabularies':
        return f'construction-delivery/construction-delivery-{key}.ttl'
    if section == 'built_asset_vocabularies':
        return f'built-asset/built-asset-{key}.ttl'
    if section == 'project_vocabularies':
        return f'construction-project/construction-project-{key}.ttl'
    if section == 'contract_vocabularies':
        return f'construction-contract/construction-contract-{key}.ttl'
    if section == 'notification_vocabularies':
        return f'notification-content/{key}-vocabulary.ttl'
    if section == 'extensions':
        return f'extensions/{key}/ontology/{key}.ttl'
    return None

print('=== MANIFEST CROSS-CHECK ===')
print('top-level keys:', list(mani.keys()))

skipped = warned = missing = compared = mismatched = total = 0

def file_version(path):
    g = rdflib.Graph(); g.parse(path, format='turtle')
    vers = []
    for s in g.subjects(rdflib.RDF.type, OWL.Ontology):
        vers.extend(str(v) for v in g.objects(s, OWL.versionInfo))
    return vers

def handle(section, key, ver):
    global skipped, warned, missing, compared, mismatched
    # special non-TTL / no-repo-file sections
    if section == 'json_ld_context':
        ok = os.path.exists('contexts/construct-x-context.jsonld')
        skipped += 1
        print(f'[SKIP ] {section}/{key}: contexts/construct-x-context.jsonld exists={ok}')
        return
    if section == 'sdk':
        skipped += 1
        print(f'[SKIP ] {section}/{key}: no repo file (external SDK)')
        return
    exp = path_for(section, key)
    if exp is None:
        missing += 1
        print(f'[MISS ] {section}/{key}: no path rule for section')
        return
    if os.path.exists(exp):
        vers = file_version(exp)
        compared += 1
        if str(ver) in vers:
            print(f'[ OK  ] {section}/{key}: {exp} versionInfo={vers} == manifest {ver}')
        else:
            mismatched += 1
            print(f'[MISM ] {section}/{key}: {exp} versionInfo={vers} != manifest {ver}')
        return
    # expected path absent -> look for a naming-mismatch candidate
    d = os.path.dirname(exp) or '.'
    flat = os.path.join(d, key + '.ttl')
    if os.path.exists(flat):
        actual = flat
    else:
        cands = [f for f in glob.glob(os.path.join(d, '*.ttl')) if key in os.path.basename(f)]
        actual = cands[0] if len(cands) == 1 else None
    if actual:
        warned += 1
        print(f'[WARN ] {section}/{key}: expected {exp}, found {actual} (naming mismatch; no version comparison)')
    else:
        missing += 1
        print(f'[MISS ] {section}/{key}: expected {exp}, no candidate in {d}/')

for section, d in mani.items():
    if not isinstance(d, dict):
        continue
    for key, ver in d.items():
        total += 1
        handle(section, key, ver)

print(f'TOTAL entries: {total} | SKIPPED: {skipped} | WARN naming-mismatch: {warned} | '
      f'MISSING: {missing} | version comparisons: {compared} | version mismatches: {mismatched}')

# --- prefix collision check across all repo ttl ---
prefixes = {}
for p in glob.glob('**/*.ttl', recursive=True):
    if '.venv' in p or 'shacl-venv' in p or 'validenv' in p or 'contexts' in p:
        continue
    text = open(p, encoding='utf-8').read()
    for m in re.finditer(r'@prefix\s+([A-Za-z0-9_-]+):\s*<([^>]+)>', text):
        pref, iri = m.group(1), m.group(2)
        if iri in prefixes and prefixes[iri] != pref:
            print('COLLISION IRI', iri, prefixes[iri], pref)
        prefixes[iri] = pref
conx = [(pr, i) for i, pr in prefixes.items() if 'construct-x' in i]
print('=== distinct construct-x prefix->IRI bindings:', len(conx))
print('=== total distinct @prefix IRI bindings:', len(prefixes))
