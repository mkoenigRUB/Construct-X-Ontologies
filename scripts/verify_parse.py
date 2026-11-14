import glob, os
import rdflib

def collect(ext):
    out = []
    for p in glob.glob('**/*' + ext, recursive=True):
        if '.venv' in p:
            continue
        out.append(p)
    return out

ttl = collect('.ttl')
owl = collect('.owl')

def parse(paths, fmt):
    errs = []
    for p in paths:
        try:
            rdflib.Graph().parse(p, format=fmt)
        except Exception as e:
            errs.append((p, str(e)))
    return errs

e1 = parse(ttl, 'turtle')
e2 = parse(owl, 'xml')
print('TTL count', len(ttl))
print('OWL count', len(owl))
print('TTL ERRORS', e1 if e1 else 'none')
print('OWL ERRORS', e2 if e2 else 'none')

pairs = 0
bad = []
for t in ttl:
    o = t[:-4] + '.owl'
    if os.path.exists(o):
        pairs += 1
        gt = rdflib.Graph(); gt.parse(t, format='turtle')
        go = rdflib.Graph(); go.parse(o, format='xml')
        if not gt.isomorphic(go):
            bad.append(t)
print('ISO PAIRS', pairs, 'MISMATCH', bad if bad else 'none')
