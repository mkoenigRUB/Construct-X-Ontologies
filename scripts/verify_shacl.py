import glob, os
import rdflib
from pyshacl import validate

def G():
    return rdflib.Graph()

def load(g, path, fmt='turtle'):
    g.parse(path, format=fmt)

def run(label, example, profiles, data_loads, advanced=True, expect='conform'):
    data = G()
    for d in data_loads:
        load(data, d)
    load(data, example)
    shacl = G()
    for p in profiles:
        load(shacl, p)
    conforms, res_graph, res_text = validate(data_graph=data, shacl_graph=shacl,
                                             infer='none', advanced=advanced)
    nviol = 0
    for s, p, o in res_graph:
        if 'violation' in str(p):
            nviol += 1
    status = 'CONFORM' if conforms else 'VIOLATED'
    if expect == 'conform' and not conforms:
        ok = 'FAIL'
    elif expect == 'violate' and conforms:
        ok = 'FAIL'
    else:
        ok = 'ok'
    print(f'[{ok}] {status} ({nviol} viol) {label}')
    return ok

results = []

# 1 schedule
results.append(run('1 schedule',
  'construction-schedule/construction-schedule-example.ttl',
  ['construction-schedule/construction-schedule-shapes-core.ttl',
   'construction-schedule/construction-schedule-shapes-schedule-type.ttl',
   'construction-schedule/construction-schedule-shapes-activity-status.ttl',
   'construction-schedule/construction-schedule-shapes-precedence-relationship-type.ttl'],
  ['construction-schedule/vocab/activity-status.ttl',
   'construction-schedule/vocab/schedule-type.ttl',
   'construction-schedule/vocab/precedence-relationship-type.ttl']))

# 2 breakdown
results.append(run('2 breakdown',
  'breakdown-structure/breakdown-structure-example.ttl',
  ['breakdown-structure/breakdown-structure-shapes-core.ttl',
   'breakdown-structure/breakdown-structure-shapes-node-types.ttl'],
  ['breakdown-structure/de-wbs-node-type.ttl',
   'breakdown-structure/de-sbs-node-type.ttl',
   'breakdown-structure/de-lbs-node-type.ttl',
   'breakdown-structure/de-cbs-node-type.ttl']))

# 3 gaeb
results.append(run('3 gaeb',
  'gaeb-boq/gaeb-boq-example.ttl',
  ['gaeb-boq/gaeb-boq-shapes-core.ttl',
   'gaeb-boq/gaeb-boq-shapes-price-component-type.ttl'],
  ['gaeb-boq/boq-price-component-type-vocab.ttl']))

# 4 progress report
results.append(run('4 progress-report',
  'construction-progress-report/construction-progress-report-example.ttl',
  ['construction-progress-report/construction-progress-report-shapes-core.ttl',
   'construction-progress-report/construction-progress-report-shapes-activity-status.ttl'],
  ['construction-schedule/vocab/activity-status.ttl']))

# 5 site
results.append(run('5 site',
  'construction-site/construction-site-example.ttl',
  ['construction-site/construction-site-shapes-core.ttl',
   'construction-site/construction-site-shapes-vocabularies.ttl',
   'construction-site/construction-site-shapes-site-logistics.ttl',
   'construction-site/construction-site-shapes-area-allocation.ttl'],
  ['construction-site/construction-site-area-type.ttl',
   'construction-site/construction-site-area-allocation-status.ttl',
   'construction-site/construction-site-equipment-type.ttl',
   'construction-site/construction-site-facility-type.ttl',
   'construction-site/construction-site-utility-type.ttl']))

# 6 delivery
results.append(run('6 delivery',
  'construction-delivery/construction-delivery-example.ttl',
  ['construction-delivery/construction-delivery-shapes-core.ttl',
   'construction-delivery/construction-delivery-shapes-vocabularies.ttl'],
  ['construction-delivery/construction-delivery-operation-type.ttl',
   'construction-delivery/construction-delivery-requirement-status.ttl']))

# 7 built asset
results.append(run('7 built-asset',
  'built-asset/built-asset-example.ttl',
  ['built-asset/built-asset-shapes-core.ttl',
   'built-asset/built-asset-shapes-vocabularies.ttl'],
  ['built-asset/built-asset-type.ttl',
   'built-asset/built-asset-spatial-structure-type.ttl']))

# 8 link ontologies example vs all 10 link profiles
link_profiles = [
  'link-ontologies/schedule-breakdown-link-shapes-core.ttl',
  'link-ontologies/schedule-boq-link-shapes-core.ttl',
  'link-ontologies/schedule-progress-report-link-shapes-core.ttl',
  'link-ontologies/site-breakdown-link-shapes-core.ttl',
  'link-ontologies/delivery-site-link-shapes-core.ttl',
  'link-ontologies/delivery-boq-link-shapes-core.ttl',
  'link-ontologies/schedule-delivery-link-shapes-core.ttl',
  'link-ontologies/schedule-site-link-shapes-core.ttl',
  'link-ontologies/site-built-asset-link-shapes-core.ttl',
  'link-ontologies/built-asset-breakdown-link-shapes-core.ttl',
]
results.append(run('8 link-example (10 profiles)',
  'link-ontologies/link-ontologies-example.ttl', link_profiles, []))

# 9 built-asset-links example
results.append(run('9 built-asset-links',
  'link-ontologies/built-asset-links-example.ttl',
  ['link-ontologies/site-built-asset-link-shapes-core.ttl',
   'link-ontologies/built-asset-breakdown-link-shapes-core.ttl'], []))

# 10 notification content (neg test handled separately)
results.append(run('10 notification-content',
  'notification-content/notification-content-example.ttl',
  ['notification-content/notification-content-shapes.ttl'],
  ['notification-content/task-type-vocabulary.ttl',
   'notification-content/subject-role-vocabulary.ttl',
   'notification-content/task-status-vocabulary.ttl',
   'notification-content/notification-type-vocabulary.ttl']))

# 11 cxcp
results.append(run('11 cxcp',
  'extensions/construct-x-construction-progress/examples/construction-progress-example.ttl',
  ['extensions/construct-x-construction-progress/shapes/construct-x-construction-progress-shapes.ttl'],
  [], advanced=True))

# 12 project core
results.append(run('12 project core',
  'construction-project/construction-project-example.ttl',
  ['construction-project/construction-project-shapes-core.ttl'],
  ['construction-project/construction-project-project-type.ttl',
   'construction-project/construction-project-project-phase-type.ttl',
   'construction-project/construction-project-project-phase-status.ttl',
   'construction-project/construction-project-project-status.ttl',
   'construction-project/construction-project-status-indicator.ttl',
   'construction-project/construction-project-participation-role.ttl'], advanced=True))

# 13 project vocab
results.append(run('13 project vocab',
  'construction-project/construction-project-example.ttl',
  ['construction-project/construction-project-shapes-vocabularies.ttl'],
  ['construction-project/construction-project-project-type.ttl',
   'construction-project/construction-project-project-phase-type.ttl',
   'construction-project/construction-project-project-phase-status.ttl',
   'construction-project/construction-project-project-status.ttl',
   'construction-project/construction-project-status-indicator.ttl',
   'construction-project/construction-project-participation-role.ttl'], advanced=True))

# 14 contract core
results.append(run('14 contract core',
  'construction-contract/construction-contract-example.ttl',
  ['construction-contract/construction-contract-shapes-core.ttl'],
  ['construction-contract/construction-contract-contract-type.ttl',
   'construction-contract/construction-contract-contractual-role.ttl',
   'construction-contract/construction-contract-subject-type.ttl',
   'construction-contract/construction-contract-pricing-model.ttl'], advanced=True))

# 15 contract vocab
results.append(run('15 contract vocab',
  'construction-contract/construction-contract-example.ttl',
  ['construction-contract/construction-contract-shapes-vocabularies.ttl'],
  ['construction-contract/construction-contract-contract-type.ttl',
   'construction-contract/construction-contract-contractual-role.ttl',
   'construction-contract/construction-contract-subject-type.ttl',
   'construction-contract/construction-contract-pricing-model.ttl'], advanced=True))

print('=== RUNS:', len(results), 'FAIL:', sum(1 for r in results if r == 'FAIL'))
