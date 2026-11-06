# JSON-LD-Kontext-Testdokument — Referenz

**Zugehöriges Testdokument:** `test-doc.jsonld` (dieser Ordner)
**Kontext:** `construct-x-context.jsonld` (Repo `contexts/`, lokal kopiert ins Projekt-Root)
**Zweck:** Nachweisen, dass die 8 Construct-X-Domänen-Ontologien (inkl. Link-Modules) korrekt per JSON-LD-Kontext expandierbar sind, dass ein JSON-LD→RDF→JSON-LD-Roundtrip verlustfrei läuft und dass nur IRIs entstehen, die in den Ontologien deklariert sind.

## 1. Node-Übersicht

| # | @id | @type (IRI) | Eigenschaften (IRIs) | Werte |
|---|---|---|---|---|
| N1 | `…/schedule/SCH-01` | `conx-cs:ConstructionSchedule` | `conx-cs:scheduleType`, `conx-cs:hasActivity` | `conx-st:RoughNetwork`; `…/activity/ACT-01` |
| N2 | `…/activity/ACT-01` | `conx-cs:Activity` | `conx-cs:plannedStart`, `conx-cs:plannedFinish`, `conx-cs:earliestStart`, `conx-cs:hasStatus`, `conx-cs:hasPredecessor`, `conx-cs:description`, `conx-cs:hierarchyCode` | Datums-Literals; `conx-status:InProgress`; `…/activity/ACT-01` (selbst, Feiertags-Beispiel); String; `W-100` |
| N3 | `…/load/LOAD-001` | `conx-del:LogisticsLoad` | `conx-del:hasStatus`, `conx-del:plannedStart`, `conx-del:quantity`, `conx-del:unitCode` | `conx-drs:InProgress`; Datum; 125 (decimal); `unit:m3` |
| N4 | `…/boq/POS-001` | `conx-gaeb:BoQItem` | `conx-gaeb:quantity`, `conx-gaeb:unitCode`, `conx-gaeb:identifier` | 42 (decimal); `unit:m3`; `POS-001` |
| N5 | `…/report/CPR-001` | `conx-cpr:ConstructionProgressReport` | `conx-cpr:activityStatus`, `conx-cpr:actualStart`, `conx-cpr:actualFinish` | `conx-status:Completed`; Datums-Literals |
| N6 | `…/asset/BA-001` | `conx-ba:BuiltAsset` | `conx-ba:hierarchyCode`, `conx-ba:hasSpatialStructureType` | `B-200`; `conx-bst:Storey` |
| N7 | `…/site/SITE-001` | `conx-site:ConstructionSite` | `conx-site:name`, `conx-site:description`, `geo:hasGeometry` | Strings; `…/geom/GEOM-001` |
| N8 | `…/geom/GEOM-001` | (ohne @type) | — | Geometrie-Referenzziel |
| N9 | `…/notification/NC-001` | `conx-nc:NotificationContent` | `conx-nc:taskStatus`, `conx-nc:taskType`, `conx-nc:notificationType`, `rdfs:seeAlso` | `conx-ts:Cancelled`; `conx-tt:DetailedScheduling`; `conx-nt:TaskRequested`; `…/schedule/SCH-01` |
| N10 | `…/wbs/WBS-001` | (ohne @type, WBS-Knoten als Link-Ziel) | `conx-sbl:isClassifiedByWBSNode` (Rolle: N2 referenziert ihn), `conx-sbl:isClassifiedByCBSNode`, `conx-sbdl:isRepresentedByLBSNode`, `conx-babl:isRepresentedByLBSNode`, `conx-babl:isClassifiedByCBSNode` | `conx-bs:WBSNode`-Referenz, `conx-cs:Activity`, `conx-de-lbs:Storey` (×2), `conx-cs:Activity` |
| N11 | `…/progress/INST-001` | `cxcp:InstallationProcess` | `hasExecutionSpace`, `hasExecutionSpaceValue`, `hasProgressEvidence`, `hasProgressEvidenceValue`, `ifcGlobalId` | `…/progress/PDS-EXEC-001`; `…/site/ROOM-412`; `…/progress/PDS-EV-001`; `…/progress/EVID-001`; String `2oX9fQ3nH6u8K1pLm4R7sT` (IFC GlobalId) |

Abkürzung: `…` = `https://data.construct-x.org/project/X`

## 2. Testziel pro Node

| Node | Nachgewiesene Ontologie / Vocabular |
|---|---|
| N1 | construction-schedule (Klasse, Property, Vocabulary schedule-type) |
| N2 | construction-schedule (Klasse Activity, 7 Properties), activity-status-vocab |
| N3 | construction-delivery (Klasse, 4 Properties), requirement-status-vocab, QUDT-Unit |
| N4 | gaeb-boq (Klasse, 3 Properties) |
| N5 | construction-progress-report (Klasse, 3 Properties), activity-status-vocab |
| N6 | built-asset (Klasse, 2 Properties), spatial-structure-type-vocab |
| N7/N8 | construction-site (Klasse, 2 Properties), GeoSPARQL-Geometrie |
| N9 | notification-content (Klasse, 3 Properties, 3 Vocabs), RDFS-seeAlso |
| N10 | schedule-breakdown-link, site-breakdown-link, built-asset-breakdown-link, de-lbs-node-type-vocab |
| N11 | construction-progress-Extension `cxcp` (Klasse InstallationProcess, 4 Objekt-Properties, Datatype-Property ifcGlobalId) |

## 3. Ontologie-Belege (alle Namen mit Grep in den echten Modul-TTLs verifiziert, Pfade relativ zum Repo-Root)

### 3.1 Ontologie-Klassen und -Properties

| # | IRI | deklariert in | Zeile |
|---|---|---|---|
| 1 | `conx-cs:ConstructionSchedule` | `construction-schedule\construction-schedule.ttl` | 30 |
| 2 | `conx-cs:Activity` | `construction-schedule\construction-schedule.ttl` | 41 |
| 3 | `conx-cs:scheduleType` | `construction-schedule\construction-schedule.ttl` | 72 |
| 4 | `conx-cs:hasActivity` | `construction-schedule\construction-schedule.ttl` | 82 |
| 5 | `conx-cs:hasStatus` | `construction-schedule\construction-schedule.ttl` | 101 |
| 6 | `conx-cs:hasPredecessor` | `construction-schedule\construction-schedule.ttl` | 92 |
| 7 | `conx-cs:description` | `construction-schedule\construction-schedule.ttl` | 192 |
| 8 | `conx-cs:hierarchyCode` | `construction-schedule\construction-schedule.ttl` | 182 |
| 9 | `conx-cs:plannedStart` | `construction-schedule\construction-schedule.ttl` | 202 |
| 10 | `conx-cs:plannedFinish` | `construction-schedule\construction-schedule.ttl` | 211 |
| 11 | `conx-cs:earliestStart` | `construction-schedule\construction-schedule.ttl` | 220 |
| 12 | `conx-del:LogisticsLoad` | `construction-delivery\construction-delivery.ttl` | 45 |
| 13 | `conx-del:hasStatus` | `construction-delivery\construction-delivery.ttl` | 73 |
| 14 | `conx-del:plannedStart` | `construction-delivery\construction-delivery.ttl` | 188 |
| 15 | `conx-del:quantity` | `construction-delivery\construction-delivery.ttl` | 220 |
| 16 | `conx-del:unitCode` | `construction-delivery\construction-delivery.ttl` | 228 |
| 17 | `conx-gaeb:BoQItem` | `gaeb-boq\gaeb-boq.ttl` | 85 |
| 18 | `conx-gaeb:identifier` | `gaeb-boq\gaeb-boq.ttl` | 149 |
| 19 | `conx-gaeb:quantity` | `gaeb-boq\gaeb-boq.ttl` | 237 |
| 20 | `conx-gaeb:unitCode` | `gaeb-boq\gaeb-boq.ttl` | 246 |
| 21 | `conx-cpr:ConstructionProgressReport` | `construction-progress-report\construction-progress-report.ttl` | 28 |
| 22 | `conx-cpr:activityStatus` | `construction-progress-report\construction-progress-report.ttl` | 42 |
| 23 | `conx-cpr:actualStart` | `construction-progress-report\construction-progress-report.ttl` | 91 |
| 24 | `conx-cpr:actualFinish` | `construction-progress-report\construction-progress-report.ttl` | 103 |
| 25 | `conx-ba:BuiltAsset` | `built-asset\built-asset.ttl` | 31 |
| 26 | `conx-ba:hasSpatialStructureType` | `built-asset\built-asset.ttl` | 110 |
| 27 | `conx-ba:hierarchyCode` | `built-asset\built-asset.ttl` | 236 |
| 28 | `conx-site:ConstructionSite` | `construction-site\construction-site.ttl` | 39 |
| 29 | `conx-site:name` | `construction-site\construction-site.ttl` | 314 |
| 30 | `conx-site:description` | `construction-site\construction-site.ttl` | 321 |
| 31 | `conx-nc:NotificationContent` | `notification-content\notification-content-ontology.ttl` | 92 |
| 32 | `conx-nc:taskStatus` | `notification-content\notification-content-ontology.ttl` | 65 |
| 33 | `conx-nc:taskType` | `notification-content\notification-content-ontology.ttl` | 75 |
| 34 | `conx-nc:notificationType` | `notification-content\notification-content-ontology.ttl` | 45 |

### 3.2 SKOS-Vocabulary-Concepts

| # | IRI | deklariert in |
|---|---|---|
| 35 | `conx-st:RoughNetwork` | `construction-schedule\vocab\schedule-type.ttl` |
| 36 | `conx-status:InProgress` | `construction-schedule\vocab\activity-status.ttl` |
| 37 | `conx-status:Completed` | `construction-schedule\vocab\activity-status.ttl` |
| 38 | `conx-drs:InProgress` | `construction-delivery\construction-delivery-requirement-status.ttl` |
| 39 | `conx-bst:Storey` | `built-asset\built-asset-spatial-structure-type.ttl` |
| 40 | `conx-de-lbs:Storey` | `breakdown-structure\de-lbs-node-type.ttl` |
| 41 | `conx-ts:Cancelled` | `notification-content\task-status-vocabulary.ttl` |
| 42 | `conx-tt:DetailedScheduling` | `notification-content\task-type-vocabulary.ttl` |
| 43 | `conx-nt:TaskRequested` | `notification-content\notification-type-vocabulary.ttl` |

### 3.3 Link-Ontologie-Properties

| # | IRI | deklariert in |
|---|---|---|
| 44 | `conx-sbl:isClassifiedByWBSNode` | `link-ontologies\schedule-breakdown-link.ttl` |
| 45 | `conx-sbl:isClassifiedByCBSNode` | `link-ontologies\schedule-breakdown-link.ttl` |
| 46 | `conx-sbdl:isRepresentedByLBSNode` | `link-ontologies\site-breakdown-link.ttl` |
| 47 | `conx-babl:isRepresentedByLBSNode` | `link-ontologies\built-asset-breakdown-link.ttl` |
| 48 | `conx-babl:isClassifiedByCBSNode` | `link-ontologies\built-asset-breakdown-link.ttl` |

### 3.4 Externe Standards (nicht aus Ontologien, via Kontext-Präfixe expandiert)

| IRI | Herkunft |
|---|---|
| `xsd:dateTime`, `xsd:decimal` | W3C XML Schema |
| `unit:m3` → `https://qudt.org/vocab/unit/m3` | QUDT |
| `geo:hasGeometry` → `http://www.opengis.net/ont/geosparql#hasGeometry` | GeoSPARQL |
| `rdfs:seeAlso` → `http://www.w3.org/2000/01/rdf-schema#seeAlso` | RDFS |

### 3.5 Construction-Progress-Extension `cxcp` (Node N11)

| # | IRI | deklariert in |
|---|---|---|
| 49 | `cxcp:InstallationProcess` | `extensions\construct-x-construction-progress\ontology\construct-x-construction-progress.ttl` |
| 50 | `cxcp:hasExecutionSpace` | dito |
| 51 | `cxcp:hasExecutionSpaceValue` | dito |
| 52 | `cxcp:hasProgressEvidence` | dito |
| 53 | `cxcp:hasProgressEvidenceValue` | dito |
| 54 | `cxcp:ifcGlobalId` | dito |

IRI-Basis: `https://w3id.org/construct-x/construction-progress#` (anderes Namensraum-Schema als die Domänen-Ontologien; die Extension ist eine externe IoC-/BOT-Erweiterung, keine der 8 Domänen).

## 4. Jena-Verifikation (`Main.java`)

- **Prüfung 1 (One-Way):** Alle im geparsten Modell vorkommenden IRIs (Subjekte, Prädikate, Resource-Objekte, Literal-Datatypes) müssen in der erwarteten IRI-Menge (75 IRIs: 64 Domänen/Link/Vocabular + 11 `cxcp` (Node N11) + Standards) enthalten sein. Output: `OK <iri>` / `FEHLT <iri>`.
- **Prüfung 2 (Roundtrip):** Modell → JSON-LD → erneut parsen → Tripelanzahl muss identisch sein.
- **Ergebnis:** `ERGEBNIS: PASS` (Exit 0) bzw. `FAIL(n)` (Exit 1).
