# Construct-X — ICDD-Beispiele (Dokumentencontainer, ISO 21597)

**Stand:** 2026-11-06 · **Status:** Integritätscheck PASS

Dieses Dokument beschreibt die **ICDD-Beispiele** des Pakets getrennt von der
Ontologie-Übersicht ([`CONSTRUCT-X-ONTOLOGIES.html`](./CONSTRUCT-X-ONTOLOGIES.html)).
ICDD ist eine **Liefer- und Verknüpfungsschicht** — keine Fachontologie. Die Fachsemantik
bleibt in den Ontologien (IoC, BOT, Construct-X, u. a. der Construction Progress Extension
`cxcp`, s. Sektion 7 der Ontologie-Doku); ICDD bündelt die dazu gehörigen Dokumente und
beschreibt, welche Elemente in verschiedenen Dateien zueinander gehören.

Die Beispiel-Container liegen unter `examples/construct-x-icdd-beispiele/`; die
example-lokale Detail-Dokumentation der Linksets liegt in
`examples/construct-x-icdd-beispiele/documentation.html`.

## 1. Rolle

ICDD (ISO 21597, *Information Container for Linked Document Delivery*) wird genutzt, um ein
Austauschpaket als selbstständigen, prüfbaren Container zu verschiffen:

- **Notification** meldet das Ereignis bzw. die Anforderung und verweist auf den Container.
- **Data Content** enthält die fachlichen Objekte und Beziehungen (Plain JSON).
- **ICDD** bündelt die Dateien (Dokumente, Ontologien, Linksets) und beschreibt die
  dokumentübergreifenden Verknüpfungen.

> ICDD ersetzt nicht die Fachontologien. Eine Aussage wie „GK-001 ist Input von
> installation-001" bleibt Teil des Fachmodells. ICDD verbindet z. B. die Repräsentation von
> `WALL-4711` im JSON mit der IFC-Repräsentation desselben Bauteils.

## 2. Standardstruktur

Ein `.icdd`-Container ist eine ZIP-Datei mit fester Grundstruktur:

```text
example.icdd
├── Index.rdf                 Container-Beschreibung + (checksummierte) interne Dokumente + Linkset
├── Ontology resources/       mitgelieferte Ontologie-Kopien (bewusst KEINE checksummierten Dokumente)
├── Payload documents/        die fachlichen Dateien (JSON, IFC, HTML, …)
└── Payload triples/
    └── links.rdf             Linkset (Identifier + DirectedBinaryLinks)
```

- `Index.rdf` (RDF/XML) registriert den Container (`ct:ContainerDescription`), die
  Dokumente (`ct:InternalDocument`) und das Linkset. Jedes Payload-Dokument trägt eine
  `ct:checksum` (SHA-256) + `ct:checksumAlgorithm`.
- `links.rdf` (RDF/XML) beschreibt Identifier (für JSON-Pfade hier in JSONPath-ähnlicher
  Schreibweise) und `ls:DirectedBinaryLink`s zwischen Dokumenten bzw. Elementen.
- Die ICDD-Container-/Linkset-Ontologien werden über die ISO-IRIs referenziert;
  Construct-X-Ontologien können unter `Ontology resources/` mitgeliefert werden.

## 3. Beispiel A — Baufortschritt

`construct-x-baufortschritt-beispiel.icdd`

Durchgängige Kette: `PACK-001` → Transport ins 4. OG → Produkte `GK-001`/`GK-002`/`MP-001`
→ `installation-001` → `WALL-4711` (IFC-Element).

| Bestandteil | Inhalt |
|---|---|
| `Index.rdf` | 111 Tripel; 8 checksummierte Payload-Dokumente |
| `Ontology resources/construct-x-construction-progress.ttl` | eingebettete `cxcp`-Ontologie 0.1.0 (58 Tripel); importiert IoC |
| `Payload documents/` | 3 Daten-Revisions (delivery/transport/installation), 3 Notifications, 1 IFC-Referenz (`bim/building-reference.ifc`), 1 Result |
| `Payload triples/links.rdf` | 78 Tripel, 10 LinkElement, 5 DirectedBinaryLink |

Beispiel-Links: Notification `processId` → Prozess im Data Content; `WALL-4711` (JSON) →
IFC GlobalId `2oX9fQ3nH6u8K1pLm4R7sT`; `photo-001` → externes Fortschrittsfoto.

## 4. Beispiel B — Doppelboden / Feinterminplanung

`construct-x-doppelboden-feinterminplanung.icdd`

`Task Request` → `contextResource` → Planning Context `PCS-001` → Zielaktivität `A100`.

| Bestandteil | Inhalt |
|---|---|
| `Index.rdf` | 49 Tripel; 3 checksummierte Payload-Dokumente |
| `Ontology resources/notification-content-ontology.ttl` | eingebettete notification-content-Ontologie **0.1.1** (90 Tripel) |
| `Payload documents/` | Task-Request, Planning-Context, Ausgangs-Dokumentation |
| `Payload triples/links.rdf` | 34 Tripel, 4 LinkElement, 2 DirectedBinaryLink |

Beispiel-Links: Notification `$.content.contextResource` → Data-Content `$.id`;
Notification `assignedResource` → `entities[*].id` im Planning Context.

## 5. Zusammenspiel mit Notifications

Die Container-Notifications enthalten zusätzlich das Feld

```json
"informationContainer": "urn:uuid:…"
```

Dies ist **keine** Tractus-X-Industry-Core-Vorgabe, sondern eine Construct-X-spezifische
Ergänzung — ein Rückverweis auf den eigenen Container (eigene Container-UUID). Im
produktiven Connector-Austausch kann die Notification klein bleiben und separat auf den
ICDD-Container verweisen; im Beispiel sind die Notifications zusätzlich im Container
enthalten, damit alles nachvollziehbar bleibt.

## 6. Integrität & Validierung (2026-11-06)

Prüfung pro Container (RDF-Parse von `Index.rdf`/`links.rdf`, Neu-Berechnung aller
SHA-256-Prüfsummen der `Payload documents/…`, TTL-Parse der eingebetteten Ontologie):

- Baufortschritt: `Index.rdf` OK, 8/8 Checksummen OK, `links.rdf` OK, Ontologie OK.
- Doppelboden: `Index.rdf` OK, 3/3 Checksummen OK, `links.rdf` OK, Ontologie OK.

**Ergebnis: PASS.** Hinweis: Die lokale Struktur-/RDF-Prüfung ist keine formale
Zertifizierung durch einen externen ISO-21597-Validator.

### Synchronisation des Doppelboden-Containers (2026-11-06)

Da noch nichts veröffentlicht bzw. produktiv genutzt ist, wurde der Doppelboden-Container an
die aktuelle Ontologie angepasst: die eingebettete
`Ontology resources/notification-content-ontology.ttl` wurde von **0.1.0 auf 0.1.1** ersetzt
(ergibt u. a. `contextResource`). Die Ontologie-Kopie im Ordner `Ontology resources/` ist
bewusst **kein** checksummiertes `ct:InternalDocument` — es musste daher keine Prüfsumme im
`Index.rdf` geändert werden; alle 3 Payload-Prüfsummen blieben gültig. Der Baufortschritt-
Container war bereits konsistent (eingebettete `cxcp`-Ontologie bit-identisch zum Modul
`extensions/construct-x-construction-progress/`) und blieb unverändert.

## 7. Referenzen

- ISO 21597-1:2020 — Information container for linked document delivery — Part 1: Container.
- ISO 21597-2:2020 — Link types / dynamic semantics.
- IoC Process Ontology (`w3id.org/ioc`) — Prozess-, Input-/Output- und Zustandsmodellierung.
- [`CONSTRUCT-X-ONTOLOGIES.html`](./CONSTRUCT-X-ONTOLOGIES.html) Sektion 7 — Construction Progress (CPR + `cxcp`).
