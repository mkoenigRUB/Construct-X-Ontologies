# -*- coding: utf-8 -*-
# Negativtests A-J. ALLE Eingabe-Bytes werden EINMAL zu Prozessstart gepinnt
# (open -> BytesIO), damit Datei-Drift (Sciebo) laeuftzeit irrelevant ist.
import os, io, datetime, hashlib
import rdflib
from pyshacl import validate

P  = rdflib.Namespace('https://www.construct-x.org/ontology/construction-project#')
C  = rdflib.Namespace('https://www.construct-x.org/ontology/construction-contract#')
NC = rdflib.Namespace('https://www.construct-x.org/ontology/notification-content#')
SH = rdflib.Namespace('http://www.w3.org/ns/shacl#')

ALL_INPUTS = [
 'construction-project/construction-project-example.ttl',
 'construction-project/construction-project-shapes-core.ttl',
 'construction-project/construction-project-shapes-vocabularies.ttl',
 'construction-project/construction-project-project-type.ttl',
 'construction-project/construction-project-project-phase-type.ttl',
 'construction-project/construction-project-project-phase-status.ttl',
 'construction-project/construction-project-project-status.ttl',
 'construction-project/construction-project-status-indicator.ttl',
 'construction-project/construction-project-participation-role.ttl',
 'construction-contract/construction-contract-example.ttl',
 'construction-contract/construction-contract-shapes-core.ttl',
 'construction-contract/construction-contract-shapes-vocabularies.ttl',
 'construction-contract/construction-contract-contract-type.ttl',
 'construction-contract/construction-contract-contractual-role.ttl',
 'construction-contract/construction-contract-subject-type.ttl',
 'construction-contract/construction-contract-pricing-model.ttl',
 'notification-content/notification-content-example.ttl',
 'notification-content/notification-content-shapes.ttl',
 'extensions/construct-x-construction-progress/examples/construction-progress-example.ttl',
 'extensions/construct-x-construction-progress/shapes/construct-x-construction-progress-shapes.ttl',
]

PIN = {}
def pin(path):
    if path not in PIN:
        with open(path,'rb') as f:
            PIN[path] = f.read()
        print(f'PIN {os.path.abspath(path)} bytes={len(PIN[path])} sha1={hashlib.sha1(PIN[path]).hexdigest()[:12]}')
    return PIN[path]

# --- vor jedem Test: ALLE Bytes fixieren ---
for p in ALL_INPUTS: pin(p)

def parse(*paths):
    g = rdflib.Graph()
    for p in paths:
        g.parse(io.BytesIO(pin(p)), format='turtle')
    return g

def check(label, data, shacl):
    conforms, resg, rest = validate(data_graph=data, shacl_graph=shacl, infer='none', advanced=True)
    nv = sum(1 for s,p,o in resg if p == SH.resultSeverity and str(o).endswith('#Violation'))
    ok = 'ok' if (not conforms) else 'FAIL(neg-test-did-not-fire)'
    print(f'[{ok}] {label}: conform={conforms} viol={nv}')
    return ok

def date_minus_1(lit):
    assert isinstance(lit, rdflib.Literal) and lit.datatype == rdflib.XSD.date, f'unerwarteter Literaltyp: {lit!r}'
    return rdflib.Literal(lit.value - datetime.timedelta(days=1), datatype=rdflib.XSD.date)

res=[]

# ================= PROJECT =================
PROJ_EX = 'construction-project/construction-project-example.ttl'
PROJ_SC = 'construction-project/construction-project-shapes-core.ttl'
PROJ_SV = 'construction-project/construction-project-shapes-vocabularies.ttl'
PROJ_VOCABS = [
 'construction-project/construction-project-project-type.ttl',
 'construction-project/construction-project-project-phase-type.ttl',
 'construction-project/construction-project-project-phase-status.ttl',
 'construction-project/construction-project-project-status.ttl',
 'construction-project/construction-project-status-indicator.ttl',
 'construction-project/construction-project-participation-role.ttl',
]

# (a) identifier fehlt bei Project
d = parse(PROJ_EX)
before = len(list(d.triples((None, P.identifier, None))))
for s in list(d.subjects(P.identifier, None)):
    d.remove((s, P.identifier, None))
print(f'[mut] proj A: identifier entfernt, vorher {before}')
res.append(check('proj A identifier-missing', d, parse(PROJ_SC)))

# (b) progress = 150
d = parse(PROJ_EX)
for s in list(d.subjects(P.progress, None)):
    d.remove((s, P.progress, None))
    d.add((s, P.progress, rdflib.Literal('150', datatype=rdflib.XSD.decimal)))
res.append(check('proj B progress=150', d, parse(PROJ_SC)))

# (c) plannedStart > plannedEnd (sh:sparql): plannedEnd := plannedStart - 1 Tag
d = parse(PROJ_EX)
cand = [s for s in d.subjects(P.plannedStart, None)]
if cand:
    s = cand[0]
    st = d.value(s, P.plannedStart, None)
    had_end = bool(list(d.triples((s, P.plannedEnd, None))))
    d.remove((s, P.plannedEnd, None))
    d.add((s, P.plannedEnd, date_minus_1(st)))
    print(f'[mut] proj C: {s} plannedEnd={d.value(s,P.plannedEnd,None)} (vorher {"vorhanden" if had_end else "abwesend"})')
    res.append(check('proj C start>end', d, parse(PROJ_SC)))
else:
    print('[FAIL] proj C: kein plannedStart-Subjekt im Beispiel')
    res.append('FAIL(no-mutation-target)')

# (d) phaseType aus fremdem Vokabular (sh:in)
s_ph = [s for s in parse(PROJ_EX).subjects(P.phaseType, None)]
if s_ph:
    dv = parse(*PROJ_VOCABS)
    dv2 = parse(PROJ_EX)
    s0 = s_ph[0]; old = dv2.value(s0, P.phaseType, None)
    dv2.remove((s0, P.phaseType, old))
    dv2.add((s0, P.phaseType, rdflib.URIRef('https://example.org/foreign/ZZZ')))
    merged = dv + dv2
    res.append(check('proj D foreign phaseType', merged, parse(PROJ_SV)))
else:
    print('[FAIL] proj D: kein phaseType im Beispiel'); res.append('FAIL(no-mutation-target)')

# ================= CONTRACT =================
CON_EX = 'construction-contract/construction-contract-example.ttl'
CON_SC = 'construction-contract/construction-contract-shapes-core.ttl'
CON_SV = 'construction-contract/construction-contract-shapes-vocabularies.ttl'
CON_VOCABS = [
 'construction-contract/construction-contract-contract-type.ttl',
 'construction-contract/construction-contract-contractual-role.ttl',
 'construction-contract/construction-contract-subject-type.ttl',
 'construction-contract/construction-contract-pricing-model.ttl',
]

# (e) identifier fehlt bei Contract
d = parse(CON_EX)
before = len(list(d.triples((None, C.identifier, None))))
for s in list(d.subjects(C.identifier, None)):
    d.remove((s, C.identifier, None))
print(f'[mut] con E: identifier entfernt, vorher {before}')
res.append(check('con E identifier-missing', d, parse(CON_SC)))

# (f) validFrom > validUntil (sh:sparql): validUntil := validFrom - 1 Tag
d = parse(CON_EX)
cand = [s for s in d.subjects(C.validFrom, None)]
if cand:
    s = cand[0]
    vf = d.value(s, C.validFrom, None)
    had_u = bool(list(d.triples((s, C.validUntil, None))))
    d.remove((s, C.validUntil, None))
    d.add((s, C.validUntil, date_minus_1(vf)))
    print(f'[mut] con F: {s} validUntil={d.value(s,C.validUntil,None)} (vorher {"vorhanden" if had_u else "abwesend"})')
    res.append(check('con F validFrom>validUntil', d, parse(CON_SC)))
else:
    print('[FAIL] con F: kein validFrom-Subjekt im Beispiel')
    res.append('FAIL(no-mutation-target)')

# (g) contractType fehlt (minCount)
d = parse(CON_EX)
for s in list(d.subjects(C.contractType, None)):
    d.remove((s, C.contractType, None))
res.append(check('con G contractType-missing', d, parse(CON_SC)))

# (h) subjectType aus fremdem Vokabular (sh:in)
s_sub = [s for s in parse(CON_EX).subjects(C.subjectType, None)]
if s_sub:
    dv = parse(*CON_VOCABS)
    dv2 = parse(CON_EX)
    s0 = s_sub[0]; old = dv2.value(s0, C.subjectType, None)
    dv2.remove((s0, C.subjectType, old))
    dv2.add((s0, C.subjectType, rdflib.URIRef('https://example.org/foreign/ZZZ')))
    res.append(check('con H foreign subjectType', dv + dv2, parse(CON_SV)))
else:
    print('[FAIL] con H: kein subjectType im Beispiel'); res.append('FAIL(no-mutation-target)')

# ================= NOTIFICATION-CONTENT =================
NC_EX = 'notification-content/notification-content-example.ttl'
NC_SH = 'notification-content/notification-content-shapes.ttl'

# (i) TaskRequested ohne taskType (sh:sparql: genau ein taskType)
d = parse(NC_EX)
nc_sub = rdflib.URIRef('https://data.example.com/project/alpha/nc/nc-detail-001')
removed = list(d.triples((nc_sub, NC.taskType, None)))
for t in removed: d.remove(t)
print(f'[mut] nc I: taskType von nc-detail-001 entfernt: {len(removed)} Triple(s)')
if removed:
    res.append(check('nc I taskType-missing', d, parse(NC_SH)))
else:
    print('[FAIL] nc I: kein taskType auf nc-detail-001')
    for s in d.subjects():
        for p in d.predicates(s, None):
            if 'taskType' in str(p): print('   taskType auf:', s, p)
    res.append('FAIL(no-mutation-target)')

# ================= CONSTRUCTION-PROGRESS (extension) =================
CXP_EX = 'extensions/construct-x-construction-progress/examples/construction-progress-example.ttl'
CXP_SH = 'extensions/construct-x-construction-progress/shapes/construct-x-construction-progress-shapes.ttl'

# (j) Transport-Output referenziert fremdes Paket (sh:sparql: kein Element in+out)
d = parse(CXP_EX)
out_state = rdflib.URIRef('https://example.construct-x.eu/progress/transport-output-state')
changed = False
for (s,p,o) in list(d.triples((out_state, None, None))):
    if str(p).endswith('hasOutputElementValue'):
        base = str(o)[:str(o).rfind('/')+1]
        d.remove((s,p,o)); d.add((s,p, rdflib.URIRef(base+'package-999'))); changed = True
if changed:
    res.append(check('cxcp J output foreign package', d, parse(CXP_SH)))
else:
    print('[FAIL] cxcp J: kein hasOutputElementValue auf transport-output-state')
    res.append('FAIL(no-mutation-target)')

print('=== NEG TESTS:', len(res), 'FAIL:', sum(1 for r in res if r != 'ok'))
