# Handover — Construct-X Ontologien & Converter

**Stand:** 2026-11-14 (Ontologie-Repo: Construction-Project + Construction-Contract 0.1.0
Draft-Module, notification-content SHACL-SPARQL-Fix, HTML-Doku auf 20 Sektionen,
Verifikationsskripte in `scripts/`) / 2026-11-08 (Converter-Repo: Bauposten-Auswahl +
Strikt-Modus-Toggle) / 2026-11-06 (Construction Progress Extension `cxcp` + Baufortschritt-
Beispiel + ICDD-Container) · **Status:** alle Verifikationen PASS

Dieses Dokument ist selbstständig: es beschreibt den Zustand beider Repos, wie man die
Entwicklungs-Umgebung auf einem **fremden Rechner** aufsetzt, und alle Wiederhol-Befehle.
Die Verifikationsskripte liegen jetzt **im Repo unter `scripts/`** (früher nur in `%TEMP%\opencode\`
— das war nicht sync-fähig); nur noch die Toolchains (Python-Venv, JDK, Maven) müssen je Rechner
neu angelegt werden. Sciebo synchronisiert `D:\Sciebo\…` (bzw. den jeweiligen Sciebo-Root).

## 1. Zustand beider Repos (2026-11-14)

### Ontologie-Repo (`Construct-X-Ontologies`, dieses Repo)

- **10 Domänen-Module:** Construction Schedule 0.5.0, Breakdown Structure 0.7.0, GAEB BoQ 0.5.0,
  Construction Progress Report 0.1.0, Construction Site 0.2.0, Construction Delivery 0.1.0,
  Built Asset 0.1.0, Notification Content 0.1.1, **Construction Project 0.1.0 (Draft, 2026-11-11)**,
  **Construction Contract 0.1.0 (Draft, 2026-11-11)**. Die beiden Drafts sind noch **nicht** Teil
  des JSON-LD-Kontexts (kommen mit dem nächsten Context-Bump).
- **1 Extension** (2026-11-06): `extensions/construct-x-construction-progress/` —
  **Construction Progress Extension `cxcp` 0.1.0** (extern, baut auf IoC Process Ontology
  `w3id.org/ioc` + BOT `w3id.org/bot` auf, eigenes IRI-Schema
  `w3id.org/construct-x/construction-progress#`; keine der Domänen, Linking-Rule nicht anwendbar).
  Enthält `ontology/`, `shapes/`, `examples/`, `queries/` + README + documentation.html.
- 10 Link-Ontologien, **31 SKOS-Vokabulare**, SHACL-Profile, Beispieldaten.
- **Beispiele (2026-11-06):** `examples/construct-x-baufortschritt-beispiel/` (End-to-End:
  Lieferung→Transport→Einbau, 3 Plain-JSON-Revisions + 3 Notifications + Result) und
  `examples/construct-x-icdd-beispiele/` (2 ICDD-Container, ISO 21597: Baufortschritt +
  Doppelboden; der Doppelboden-Container wurde auf die aktuelle notification-content 0.1.1
  synchronisiert).
- **104 TTL-Dateien + 51 RDF/XML-Mirrors parse-frei; SHACL 15/15 Runs conform, 0 Violations;
  10 Negativtests verstoßen korrekt; MANIFEST ↔ `versionInfo` konsistent (54 Einträge);
  keine neuen Präfix-Kollisionen** (bekannt: `dct`/`dcterms`-Kollision auf `http://purl.org/dc/terms/`,
  vorbestehend, außerhalb des Construct-X-Namenraums).
- **JSON-LD-Kontext** `contexts/construct-x-context.jsonld` (0.1.0, `@version: 1.1`,
  Kontext-IRI `https://www.construct-x.org/context/construct-x/0.1.0`): 380 `@context`-Einträge
  (1 `@version` + 55 Präfixe + 208 Bare-Term-String-Mappings + 116 Objekt-Definitionen),
  seit 2026-11-06 inkl. `cxcp`-Präfix + 8 cxcp-Terme.
  Kollidierende Bare-Terme sind nur per Präfix nutzbar — Designentscheidung.
  Verifiziert per Jena 4.10.0 (Projekt `contexts/validation/`): 48 Triples / 77 IRIs,
  Roundtrip 48 → 48, Exit 0.

### Converter-Repo (`construct-x-converters`)

- Reverse-Konverter fertig (GAEB/MS → RDF, inkl. 3 Pom-Fixes + 2 Test-Pfad-Fixes).
- **Construct-X SDK** (2026-11-05): neues Maven-Modul `construct-x-sdk/`
  (`org.construct-x:construct-x-sdk:0.1.0-SNAPSHOT`, Java 25, Jena 4.10.0, Jackson 2.17.2, kein Spring) —
  Ebene 1 der Use-Case-Architektur. De-duplizierte die identischen Kopien
  `ConxCurieRegister` (×3), `RdfInput` (×2), `PlainJsonModelWriter` (×3) und Basis-`ConxNamespaces`;
  neu: `IriFactory`, `OntologyRegistry`, `ShaclValidatorHelper`, `ProvenanceHelper`.
  Die GAEB-spezifischen `ConxNamespaces`-Konstanten (`P_IDENTIFIER`, `BILL_OF_QUANTITIES`, …)
  bleiben im GAEB-`core`-Modul. 12 duplizierte Quelldateien (inkl. Test-Klassen) aus den Builds gelöscht.
- **Vollverifikation 2026-11-05, 161/161 Tests grün:** SDK 81/81, GAEB 32/32 (core 17 + web 15),
  MS 33/33, RDF 15/15 (JDK 25.0.5 + Maven 3.9.9). Die duplizierten Unit-Tests laufen jetzt
  einmal im SDK → Converter-Gesamt von 104 auf 80 gesunken (keine Abdeckung verloren).

## 2. Rechner-Setup (Windows, PowerShell)

Voraussetzung: Sciebo-Ordner `D:\Sciebo\Construction-X\200_Arbeitspakete\AP3\AP 3.4\`
mit beiden Repos (Sync). Falls der Sciebo-Root anders liegt, absolute Pfade in allen
Befehlen entsprechend anpassen (v. a. `CONX_ONTOLOGY_ROOT`).

| Komponente | Zielort (maschinenspezifisch!) | Herkunft |
|---|---|---|
| Temurin JDK 25 | `%TEMP%\opencode\jdk25\jdk-25.0.5+8` | https://adoptium.net/ (Temurin 25, Windows x64), ZIP entpacken, ggf. Ordner auf `jdk-25.0.5+8` umbenennen |
| Maven 3.9.9 | `%TEMP%\opencode\maven\apache-maven-3.9.9` | `Invoke-WebRequest https://archive.apache.org/dist/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.zip -OutFile maven.zip` → `Expand-Archive maven.zip -DestinationPath "%TEMP%\opencode\maven"` |
| Python 3.12 | Systeminstallation | https://python.org |
| SHACL-Venv | **`.venv/` im Repo-Root** (in `.gitignore`, je Rechner neu) | s. u. — **Versionen exakt halten** |

SHACL-Venv anlegen (aus dem **Repo-Root**; Versionen exakt):

```powershell
python -m venv .venv
& .\.venv\Scripts\pip.exe install "rdflib==7.6.0" "pySHACL==0.40.1"
```

> **Wichtig:** Der korrekte pySHACL-Aufruf ist `validate(data_graph=…, shacl_graph=…,
> infer='none', advanced=True)`. Ein Aufruf mit dem falschen Keyword `shapes_graph=`
> verwerft die Shapes stillschweigend und meldet "0 Shapes" → vorgebliches CONFORM.
> Die Skripte in `scripts/` verwenden das korrekte Keyword (VALIDATION.md Note 18,
> korrigiert 2026-11-11 — es gibt **keinen** pySHACL/rdflib-versions-Bug; der repo-interne
> `.venv` mit rdflib 7.6.0 + pySHACL 0.40.1 funktioniert korrekt).

Weitere Hinweise:

- **`JAVA_HOME` nicht global ändern.** Der Maschinen-Default (`C:\Program Files\openjdk`,
  JDK 17) ist zu alt. `JAVA_HOME` immer pro-Befehl setzen (s. §3).
- **Maven-Local-Repo (~/.m2):** Auf der Quellmaschine sind die Jena-Dependencies
  vorab geladen. Auf einem fremden Rechner lädt Maven sie bei Erstlauf aus dem Internet
  (ca. wenige Minuten, Internetverbindung nötig).
- Vor jedem Maven-Lauf prüfen, dass der Maven-Pfad existiert (`Test-Path`) — Temp-Ordner
  werden beim Neustart teilweise geleert; dann neu entpacken (Befehl obige Tabelle).

## 3. Wiederhol-Befehle (exakte Kommandos)

Pfade in `$env:TEMP\opencode\…` für die Toolchains; die **Verifikationsskripte liegen im
Repo unter `scripts/`** und laufen **aus dem Repo-Root** mit dem `.venv`-Python.

### 3.1 RDF-Parse + SHACL + Negativtests + MANIFEST (Ontologie-Repo, via `scripts/`)

```powershell
# aus dem Repo-Root; .venv muss existieren (s. §2)
$py = ".venv\Scripts\python.exe"
& $py scripts\verify_parse.py      # -> TTL 104 / OWL 51, keine Errors, 51 isomorphe Paare
& $py scripts\verify_neg.py        # -> NEG TESTS: 10, FAIL: 0
& $py scripts\verify_shacl.py      # -> RUNS: 15, FAIL: 0 (alle CONFORM, 0 viol)
& $py scripts\verify_manifest.py   # -> TOTAL 54, MISSING 0, version mismatches 0
```

Details, Negativtest-Referenz A–J und erwarteter Output: `scripts/README.md`.

**SHACL — 15 Runs** (Ablauf pro Run: Profile + SKOS-Vokabulare des Moduls in den
**Data-Graph** laden — nötig für `sh:class skos:Concept` / `sh:in` — Beispiel parsen,
`validate(data_graph=…, shacl_graph=…, infer='none', advanced=True)`):

| # | Data | Profile |
|---|---|---|
| 1 | `construction-schedule` Beispiel | Core, Schedule-Type, Activity-Status, Precedence-Relationship-Type (alle 4) |
| 2 | `breakdown-structure` Beispiel | Core + Node-Types |
| 3 | `gaeb-boq` Beispiel | Core + Price-Component-Type |
| 4 | `construction-progress-report` Beispiel | Core + Activity-Status |
| 5 | `construction-site` Beispiel | Core + Vocabulary + Site-Logistics + Area-Allocation |
| 6 | `construction-delivery` Beispiel | Core + Vocabulary |
| 7 | `built-asset` Beispiel | Core + Vocabulary |
| 8 | integriertes Link-Beispiel | alle 10 Link-Profile |
| 9 | `built-asset-links-example.ttl` | Site–Built Asset + Built Asset–Breakdown |
| 10 | `notification-content` Beispiel | Core (Negativtest I: `TaskRequested` ohne `taskType` muss verstoßen) |
| 11 | `extensions/…construction-progress` Beispiel | cxcp-Profile, **`advanced=True`** (Negativtest J) |
| 12 | `construction-project` Beispiel | Core (`advanced=True`, 3 `sh:sparql`-Constraints; Negativtests A/B/C) |
| 13 | `construction-project` Beispiel | Vocabularies (6 `sh:in`; Negativtest D) |
| 14 | `construction-contract` Beispiel | Core (`advanced=True`, 2 `sh:sparql`-Constraints; Negativtests E/F/G) |
| 15 | `construction-contract` Beispiel | Vocabularies (4 `sh:in`; Negativtest H) |

Die exakte Laufkonfiguration steht in `VALIDATION.md` (Abschnitt "Package validation").

### 3.3 JSON-LD-Kontext-Check (Jena 4.10.0, erwartet: `ERGEBNIS: PASS`, Exit 0)

```powershell
Set-Location "D:\Sciebo\Construction-X\200_Arbeitspakete\AP3\AP 3.4\Construct-X-Ontologies\contexts\validation"
$env:JAVA_HOME = "$env:LOCALAPPDATA\Temp\opencode\jdk25\jdk-25.0.5+8"
& "$env:LOCALAPPDATA\Temp\opencode\maven\apache-maven-3.9.9\bin\mvn.cmd" -q compile exec:java "-Dexec.args=test\test-doc.jsonld"
```

Erwartet: 48 Triples, 77 IRIs (One-Way-Check auf 75 erwartete IRIs; zusätzliche IRIs erlaubt),
Roundtrip 48 → 48.
Das erzeugt `contexts\validation\target\` → **danach löschen** (gehört nicht ins Repo).
Achtung: Die Repo-Kopie `test/test-doc.jsonld` referenziert den Kontext per
`"../../construct-x-context.jsonld"` — **nie** die Temp-Version über die Repo-Kopie
kopieren.
Achtung: Jena 4.10.0 akzeptiert das Kontext-Feld `@version` **nur** mit dem Wert `1.1`
(jeder andere Wert → `LOADING_REMOTE_CONTEXT_FAILED`); daher bleibt `@version: 1.1`
(versionierte Kontext-IRI `@id` bleibt der Versionsmarker).

### 3.4 ICDD-Container-Integrität (neu, 2026-11-06) + MANIFEST-Check

**MANIFEST-Check:** jetzt Teil von §3.1 (`scripts\verify_manifest.py` — erwartet
`TOTAL 54 … MISSING: 0 … version mismatches: 0`).

**ICDD:** Pro `.icdd`-Container (ZIP): `Index.rdf` als RDF/XML parsen, für jede
`ct:InternalDocument` mit `ct:checksum` den SHA-256 der `Payload documents/…`-Datei neu
berechnen und vergleichen, `Payload triples/links.rdf` als RDF/XML parsen, eingebettete
Ontologie als TTL parsen. Erwartet: alle Checksummen OK (Baufortschritt 8/8, Doppelboden 3/3),
`ICDD-CHECK: PASS`. Ad-hoc-Check, kein dauerhaftes Skript; Details + Stand:
`documentation/ICDD-EXAMPLES.md` und `VALIDATION.md`.

### 3.5 Converter-Tests (183/183 erwartet: SDK 85 + GAEB 48 + MS 35 + RDF 15)

Zuerst das SDK-Modul (bei SDK-Änderungen; ansonsten einmalig, bis es im lokalen m2 liegt):

```powershell
$env:JAVA_HOME = "$env:LOCALAPPDATA\Temp\opencode\jdk25\jdk-25.0.5+8"
Set-Location "D:\Sciebo\Construction-X\200_Arbeitspakete\AP3\AP 3.4\construct-x-converters\construct-x-sdk"
& "$env:LOCALAPPDATA\Temp\opencode\maven\apache-maven-3.9.9\bin\mvn.cmd" clean test
# danach (einmalig):  mvn -q install -DskipTests
```

Danach pro Converter-Modul, mit JDK 25 + Ontologie-Root:

```powershell
$env:JAVA_HOME = "$env:LOCALAPPDATA\Temp\opencode\jdk25\jdk-25.0.5+8"
$env:CONX_ONTOLOGY_ROOT = "D:\Sciebo\Construction-X\200_Arbeitspakete\AP3\AP 3.4\Construct-X-Ontologies"
Set-Location "D:\Sciebo\Construction-X\200_Arbeitspakete\AP3\AP 3.4\construct-x-converters\Converter"
& "$env:LOCALAPPDATA\Temp\opencode\maven\apache-maven-3.9.9\bin\mvn.cmd" clean test
# analog: …\msproject-converter-service  und  …\rdf-converter-service
```

Erwartet: GAEB core 26/26 + web 22/22, MS 35/35, RDF 15/15, SDK 85/85 = **183/183** (2026-11-08: SDK/GAEB/MS neu verifiziert; RDF-Modul unverändert, 15/15 vom 2026-11-05).
`clean` ist **erforderlich** (ECJ-Stale-Class-Falle: ohne `clean` werden evtl. alte
Class-Dateien aus `target/` mitbenutzt).

## 4. Bekannte Fallen

1. **PowerShell-Scanner:** Schleifen/Arrays in Inline-Befehlen werden teils mit
   `Portable shell scanner cannot analyze command: invalid-structure` abgelehnt.
   Workaround: einfache `Select-String`/`Measure-Object`-One-Liner oder .ps1 auf Platte.
2. **`python -c` mit Backslash-Pfaden** bricht → Rohzeichenketten (`r'…'`) oder Forward
   Slashes.
3. **PS 5.1 liest .ps1 ohne BOM als ANSI** → Umlaute in Paden in .ps1-Dateien vermeiden
   (oder UTF-8-BOM).
4. **TTL-Multi-Type-Deklarationen** (z. B. `a owl:DatatypeProperty, owl:…`) matchen nicht
   auf die Regex `owl:DatatypeProperty$` — bei automatischen Audits beachten.
5. **File-Writes immer per Re-Read verifizieren** — einmal nicht persistiert.
6. **Maven/Lokal-Repo:** `~/.m2` ist maschinenspezifisch; bei Cache-Problemen
   `mvn -U` (forced Update).
7. **byte-buddy-agent-Pfad (MS/RDF-Poms):** Die Poms von `msproject-converter-service`
   und `rdf-converter-service` referenzieren `byte-buddy-agent.jar` über einen
   hartkodierten, maschinenspezifischen Pfad. Wenn er nicht auflösbar ist, dem Maven-Call
   `-Dbyte-buddy-agent.jar=<lokaler Pfad zu byte-buddy-agent-1.14.13.jar>` anhängen
   (Pom nicht ändern). Die GAEB-Builds und das SDK sind davon nicht betroffen.

## 5. Offene Punkte & Risiken

| Punkt | Status |
|---|---|
| **Git** | Ontologie-Repo auf GitHub (`mkoenigRUB/Construct-X-Ontologies`, `main`); Stand: Commit `1ff099f` (2026-11-13) **lokal committet, noch nicht gepusht** (1 Ahead von `origin/main`) — Push ist der nächste offene Schritt. Converter-Repo weiterhin **ohne** Git (bewusst) — dort nur Sciebo-Sync |
| **Toolchains maschinenspezifisch** | Python-Venv (`.venv/` im Repo-Root), JDK, Maven müssen auf jedem Rechner neu aufgesetzt werden (§2). Die Verifikationsskripte liegen dagegen **im Repo** unter `scripts/` (2026-11-14) und sind damit sync-fähig |
| **Kein zentrales Test-Skript** im Converter-Repo | `Converter\build.ps1` ist **kein** Ersatz (GAEB-Sandbox-Fallback, hardcodet `C:\Program Files\Java\jdk-20`, benötigt vorbefülltes `web/lib`); `test-all.ps1` existiert nicht |
| **Parker B: selektive LV-Positions-Auswahl** | **erledigt (08.11.)**: Baum mit Checkboxen (GAEB-Tab 8084) + `POST /api/v1/positions/gaeb-boq` + `selection`-Parameter am Convert-Endpoint; Strikt-Modus-Toggle `strict=true` an beiden Reverse-Endpoints (Datenverlust → 400, Approximationen getolert, Klassifikation `ConxStrict` im SDK). Details: `Construct-X-Converters/HANDOFF.md` (2026-11-08) + `README.md` |
| **Semantic-Kennzeichen im JSON-LD-Test-Doc** | bewusst akzeptiert (z. B. `conx-cs:hasStatus`-Domain = Activity, aber N2 ist kein Activity; `conx-del:quantity`-Domain = LogisticsLoadItem vs. N3 LogisticsLoad; N10-Link mit `sbdl`/`babl`-Properties). Der Jena-Test prüft nur IRI-Expansion, **kein SHACL** |
| **Altlasten im Ontologie-Root** | `Construct-X-Ontologies.zip`, `gaeb-boq.zip`, `notification-content_0.1.1.zip`, `VSCode_…Starter (1).zip`, `AGENTS.md.bak` — bewusst unangetastet; `maven.zip` in Temp ist löschbar |
| **Sciebo-Datei-Drift** | Sciebo tauscht gelegentlich Datei-Versionen auf Disk (beobachtet bei den Modul-Beispiel-TTLs und der HTML-Doku). Vor jedem Commit die kritischen Dateien per `Get-FileHash` gegen die bekannten Werte prüfen (Referenzwerte: `scripts/README.md` + die jeweiligen VALIDATION.md-Items) |
| ~~**AUDIT-Item 44**~~ | erledigt (04.11.): formaler Konsistenz-Check in `AUDIT.md` Item 45 dokumentiert — alle Sub-Behauptungen bestätigt |

## 6. Dokumentations-Index

| Datei | Inhalt |
|---|---|
| `README.md` | Repo-Überblick, Modulstand (inkl. Extension + 2 Draft-Module), JSON-LD- + SDK-Passus, 2026-11-11/12-Integration |
| `VALIDATION.md` | vollständiger Validierungsbericht; SHACL-15-Runs, ICDD- + Jena-Abschnitt, Notes 19–37 (36 = nc-SPARQL-Fix, 37 = HTML-Sync) |
| `AUDIT.md` | Audit-Items; 41–45 = JSON-LD-Kontext, 46–48 = SDK, 49–56 (2026-11-06) = cxcp + ICDD, 57 = Converter, 58–61 (2026-11-11) = Project/Contract-Drafts, **62–63 (2026-11-12) = nc-SPARQL-Fix + HTML-Sync** |
| `MANIFEST.json` | zentrales Register (**54 Einträge**: 10 Domänen + 10 Link + 31 Vokabulare + `json_ld_context` + `sdk` + `extensions`) |
| `scripts/` | **Verifikationsskripte (rechnerunabhängig, 2026-11-14):** `verify_parse.py`, `verify_neg.py`, `verify_shacl.py`, `verify_manifest.py` + `README.md` mit Setup, Befehlen, erwartetem Output, Negativtest-Referenz A–J |
| `construction-project/` | **Draft 0.1.0 (2026-11-11):** Ontologie (4 Klassen, 15 OP + 16 DP), 6 SKOS-Vokabulare, Core + Vocabularies SHACL, Beispiel, 7 OWL-Mirrors |
| `construction-contract/` | **Draft 0.1.0 (2026-11-11):** Ontologie (4 Klassen), 4 SKOS-Vokabulare, Core + Vocabularies SHACL, Beispiel (3 Einzelverträge der Brücke-XY-Kette), 5 OWL-Mirrors — **2026-11-14: Einzelvertragssicht** (Ketten-Properties `subcontractOf`/`hasUpstreamContract` entfernt, Kette kommt im Projekt zusammen; ARGE = 1 untypisierte IRI pro Partei) |
| `documentation/CONSTRUCT-X-ONTOLOGIES.html` | HTML-Doku (nur Ontologien, **20 Sektionen**, Stand 2026-11-12); **Sektion 7 = Construction Progress (CPR + cxcp)**, **Sektionen 12/13 = Construction Project / Contract (neu)**, Sektion 15 = Vokabulare (inkl. neuer Projekt-/Vertrags-Blöcke), Sektion 20 = JSON-LD |
| `documentation/ICDD-EXAMPLES.md` | eigenständige ICDD-Dokumentation (2026-11-06): Container-Aufbau (ISO 21597), beide Beispiele, Integritätsstatus + Doppelboden-Sync-Notiz, Referenzen |
| `extensions/construct-x-construction-progress/` | cxcp 0.1.0: `ontology/` (58 Tripel), `shapes/` (69 Tripel, 1× `sh:sparql`), `examples/` (TTL + JSON-LD + Runtime-JSON), `queries/`, README, documentation.html |
| `examples/construct-x-baufortschritt-beispiel/` | End-to-End-Beispiel (3 Daten-Revisions, 3 Notifications, Result) |
| `examples/construct-x-icdd-beispiele/` | 2 ICDD-Container (ISO 21597) + README + documentation.html |
| `contexts/construct-x-context.jsonld` | JSON-LD-Kontext (0.1.0, `@version: 1.1`, 380 `@context`-Einträge, inkl. `cxcp`-Präfix + 8 Terme; **ohne** die 2 Draft-Module — kommen mit dem nächsten Context-Bump) |
| `contexts/validation/test/test-doc-reference.md` | Referenz-Explanation der Test-Doku (inkl. Node N11 = cxcp) |
| `construct-x-converters/HANDOFF.md` | Handover-Dokument des Converter-Repos |

## 7. Nächste Schritte / Wie man auf einem anderen Rechner weiterarbeitet

### Erst einmal ankommen (Checkliste)
1. Repo per `git clone` bzw. Sciebo-Sync holen (Stand: Commit `1ff099f`, `main`).
2. Python-Venv anlegen: `python -m venv .venv` + `pip install "rdflib==7.6.0" "pySHACL==0.40.1"` (§2).
3. **Smoke-Test:** die vier Skripte aus §3.1 ausführen — erwartet `TTL 104/OWL 51`, `NEG 10/FAIL 0`, `RUNS 15/FAIL 0`, `TOTAL 54/MISSING 0`. Damit ist die Umgebung reproduziert.
4. Optional (nur für Jena/Converter): JDK 25 + Maven 3.9.9 in `%TEMP%\opencode\` entpacken (§2).

### Offene Fachaufgaben (nach Priorität)
1. **Push** `main` — Commit `1ff099f` liegt nur lokal (1 Ahead von `origin/main`). `git push` ist der erste offene Schritt.
2. **Draft-Module weiter ausbauen (0.2.0-Vorbereitung, nicht jetzt):**
   - Contract: Klauselhierarchie, Compensation, ContractDocument/Change, typisierte Subject→Deliverable-Referenz.
   - Project: geplante `project-*-link`-Link-Ontologien (z. B. Project↔Contract, Project↔Schedule).
   - JSON-LD-Kontext um die 2 Drafts erweitern (**mit Context-Bump**; `@version` bleibt 1.1 — Jena-Quirk).
3. **Optional:** vorbestehende Doku-Kleinheiten aufräumen (`dct`/`dcterms`-Kollision, 8 Manifest-naming-mismatches, VALIDATION-Zahlen 34/36 + 27/31) — bisher bewusst nicht angefasst.

### Konventionen, die bei jeder Modul-Änderung gelten
- IRIs über **versionierte** Ontologie-IRIs (`…/0.x.0`); Link-Ontologien nur gemäß `documentation/ONTOLOGY-LINKING-RULE.md`; **keine** Cross-Domain-ObjectProperties in Domänen-Ontologien.
- **Kein Version-Bump ohne Absprache.** Shapes in `<ont>-shapes-core.ttl`.
- Modul-Änderung ⇒ `MANIFEST.json` + `VALIDATION.md` + `AUDIT.md` (nächstes Item) + HTML-Doku synchron halten.
- Vor Abschluss: alle vier Verifikationsskripte aus `scripts/` laufen lassen und den echten Output zeigen.
- **Datei-Drift (Sciebo):** vor jedem Commit die kritischen Dateien (Modul-Beispiel-TTLs, HTML-Doku) per `Get-FileHash` gegen die bekannten Werte prüfen (§5).

### Was **nicht** in dieses Repo gehört
- Konverter-Dienste (GAEB/MS/RDF), Frontends, Docker-Betrieb ⇒ separates Repo `construct-x-converters`.
- `contexts/construct-x-context.jsonld` **nicht** ohne Absprache/Context-Bump erweitern.
