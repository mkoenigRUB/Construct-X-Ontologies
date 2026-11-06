# Handover — Construct-X Ontologien & Converter

**Stand:** 2026-11-06 (Construction Progress Extension `cxcp` + Baufortschritt-Beispiel + ICDD-Container, Ontologie-Repo) · **Status:** alle Verifikationen PASS

Dieses Dokument ist selbstständig: es beschreibt den Zustand beider Repos, wie man die
Entwicklungs-Umgebung auf einem **fremden Rechner** aufsetzt, und alle Wiederhol-Befehle.
Alles, was auf der Quellmaschine nur unter `C:\Users\Markus König\AppData\Local\Temp\opencode\`
lag, ist hier als "neu aufsetzbar" beschrieben — Sciebo synchronisiert ausschließlich
`D:\Sciebo\…`.

## 1. Zustand beider Repos (2026-11-04)

### Ontologie-Repo (`Construct-X-Ontologies`, dieses Repo)

- 8 Domänen-Module: Construction Schedule 0.5.0, Breakdown Structure 0.7.0, GAEB BoQ 0.5.0,
  Construction Progress Report 0.1.0, Construction Site 0.2.0, Construction Delivery 0.1.0,
  Built Asset 0.1.0, Notification Content 0.1.1.
- **1 Extension** (2026-11-06): `extensions/construct-x-construction-progress/` —
  **Construction Progress Extension `cxcp` 0.1.0** (extern, baut auf IoC Process Ontology
  `w3id.org/ioc` + BOT `w3id.org/bot` auf, eigenes IRI-Schema
  `w3id.org/construct-x/construction-progress#`; keine der 8 Domänen, Linking-Rule nicht anwendbar).
  Enthält `ontology/`, `shapes/`, `examples/`, `queries/` + README + documentation.html.
- 10 Link-Ontologien, 21 SKOS-Vokabulare, SHACL-Profile, Beispieldaten.
- **Beispiele (2026-11-06):** `examples/construct-x-baufortschritt-beispiel/` (End-to-End:
  Lieferung→Transport→Einbau, 3 Plain-JSON-Revisions + 3 Notifications + Result) und
  `examples/construct-x-icdd-beispiele/` (2 ICDD-Container, ISO 21597: Baufortschritt +
  Doppelboden; der Doppelboden-Container wurde auf die aktuelle notification-content 0.1.1
  synchronisiert).
- 86 TTL-Dateien + 39 RDF/XML-Mirrors parse-frei; **SHACL 11/11 Runs conform, 0 Violations**;
  MANIFEST ↔ `versionInfo` konsistent (41 Einträge); 41 Präfixe ohne Kollision.
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
| SHACL-Venv | `%TEMP%\opencode\shacl-venv` | s. u. — **Versionen exakt halten** |

SHACL-Venv anlegen (Versionen sind **kritisch**, s. Hinweis):

```powershell
python -m venv "$env:LOCALAPPDATA\Temp\opencode\shacl-venv"
& "$env:LOCALAPPDATA\Temp\opencode\shacl-venv\Scripts\pip.exe" install "rdflib==6.3.2" "pySHACL==0.28.1"
```

> **Warum diese Versionen:** Systemweit installiertes rdflib 7.6.0 mit pySHACL 0.40.1
> findet bei unseren SHACL-Profilen stillschweigend 0 Shapes (per Minimal-Counterexample
> bestätigt: der Counterexample wird nur im Venv korrekt abgelehnt).

Weitere Hinweise:

- **`JAVA_HOME` nicht global ändern.** Der Maschinen-Default (`C:\Program Files\openjdk`,
  JDK 17) ist zu alt. `JAVA_HOME` immer pro-Befehl setzen (s. §3).
- **Maven-Local-Repo (~/.m2):** Auf der Quellmaschine sind die Jena-Dependencies
  vorab geladen. Auf einem fremden Rechner lädt Maven sie bei Erstlauf aus dem Internet
  (ca. wenige Minuten, Internetverbindung nötig).
- Vor jedem Maven-Lauf prüfen, dass der Maven-Pfad existiert (`Test-Path`) — Temp-Ordner
  werden beim Neustart teilweise geleert; dann neu entpacken (Befehl obige Tabelle).

## 3. Wiederhol-Befehle (exakte Kommandos)

Pfade in `$env:TEMP\opencode\…`; bei abweichendem Benutzerkonto entsprechend ersetzen.

### 3.1 RDF-Parse (Ontologie-Repo, 86 TTL + 39 RDF/XML)

```powershell
$py = "$env:LOCALAPPDATA\Temp\opencode\shacl-venv\Scripts\python.exe"
& $py -c "import glob, rdflib; [rdflib.Graph().parse(f, format='turtle') for f in glob.glob(r'D:\Sciebo\Construction-X\200_Arbeitspakete\AP3\AP 3.4\Construct-X-Ontologies\**\*.ttl', recursive=True)]"
```

Auch ohne Fehler = PASS. (Bei Inline-Befehls-Problemen: .ps1 auf Platte, s. §4.)

### 3.2 SHACL — 11 Runs (erwartet: alle conform, 0 Violations)

Ablauf pro Run: SHACL-Profil(e) + SKOS-Vokabular(en) des Moduls in den **Data-Graph**
laden (nötig für `sh:class skos:Concept` / `sh:in`), Beispiel-Datei parsen,
`pyshacl.validate(data_graph=..., shacl_graph=..., infer='none')`.

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
| 10 | `notification-content` Beispiel | Core (inkl. Negativtest: `TaskRequested` ohne `taskType`/Target muss verstoßen) |
| 11 | `extensions/construct-x-construction-progress` Beispiel | cxcp-Profile, **mit `advanced=True`** (enthält einen `sh:sparql`-Constraint: Transport muss ein Element als Input UND Output behalten; inkl. Negativtest: Transport mit unterschiedlichem Input/Output-Element muss verstoßen) |

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

### 3.4 ICDD-Container-Integrität + MANIFEST-Check (neu, 2026-11-06)

Pro `.icdd`-Container (ZIP): `Index.rdf` als RDF/XML parsen, für jede `ct:InternalDocument`
mit `ct:checksum` den SHA-256 der `Payload documents/…`-Datei neu berechnen und vergleichen,
`Payload triples/links.rdf` als RDF/XML parsen, eingebettete Ontologie als TTL parsen.
Außerdem: MANIFEST ↔ in-file `versionInfo`-Konsistenz (41 Einträge, inkl. `extensions`).

Erwartet: alle Checksummen OK (Baufortschritt 8/8, Doppelboden 3/3), `ICDD-CHECK: PASS`,
`MANIFEST-CHECK: PASS`. (Laufskripte liegen in der Arbeitssitzung 2026-11-06, s. `VALIDATION.md`.)

### 3.5 Converter-Tests (161/161 erwartet: SDK 81 + GAEB 32 + MS 33 + RDF 15)

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

Erwartet: GAEB core 17/17 + web 15/15, MS 33/33, RDF 15/15, SDK 81/81 = **161/161**.
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
| **Git** | Ontologie-Repo seit 2026-11-05 auf GitHub (`mkoenigRUB/Construct-X-Ontologies`, `main`); Converter-Repo weiterhin **ohne** Git (bewusst) — dort nur Sciebo-Sync |
| **Toolchains maschinenspezifisch im Temp** | JDK/Maven/Venv müssen auf jedem Rechner neu aufgesetzt werden (§2) |
| **Kein zentrales Test-Skript** im Converter-Repo | `Converter\build.ps1` ist **kein** Ersatz (GAEB-Sandbox-Fallback, hardcodet `C:\Program Files\Java\jdk-20`, benötigt vorbefülltes `web/lib`); `test-all.ps1` existiert nicht |
| **Parker B: selektive LV-Positions-Auswahl** | Nutzerfrage offen: "Bauposten nur (flache Liste) oder alle Ebenen (Baum mit Checkboxen)?" + Strikt-Modus-Toggle |
| **Semantic-Kennzeichen im JSON-LD-Test-Doc** | bewusst akzeptiert (z. B. `conx-cs:hasStatus`-Domain = Activity, aber N2 ist kein Activity; `conx-del:quantity`-Domain = LogisticsLoadItem vs. N3 LogisticsLoad; N10-Link mit `sbdl`/`babl`-Properties). Der Jena-Test prüft nur IRI-Expansion, **kein SHACL** |
| **Altlasten im Ontologie-Root** | `Construct-X-Ontologies.zip`, `gaeb-boq.zip`, `notification-content_0.1.1.zip`, `VSCode_…Starter (1).zip`, `AGENTS.md.bak` — bewusst unangetastet; `maven.zip` in Temp ist löschbar |
| ~~**AUDIT-Item 44**~~ | erledigt (04.11.): formaler Konsistenz-Check in `AUDIT.md` Item 45 dokumentiert — alle Sub-Behauptungen bestätigt |

## 6. Dokumentations-Index

| Datei | Inhalt |
|---|---|
| `README.md` | Repo-Überblick, Modulstand (inkl. Extension), JSON-LD- + SDK-Passus, 2026-11-06-Integration |
| `VALIDATION.md` | vollständiger Validierungsbericht; SHACL-11-Runs, ICDD-Validierungsabschnitt, Jena-Abschnitt, Notes 19–29 |
| `AUDIT.md` | Audit-Items; Items 41–45 = JSON-LD-Kontext, 46–48 = SDK, **49–55 (2026-11-06) = cxcp-Extension + Beispiele + ICDD** |
| `MANIFEST.json` | zentrales Register (41 Ontologie-Einträge + `json_ld_context` + `sdk` + **`extensions`**-Sektion) |
| `documentation/CONSTRUCT-X-ONTOLOGIES.html` | HTML-Doku; Sektion 18 (JSON-LD) und **Sektion 19 (cxcp-Extension + ICDD, id `cxcp-icdd`)** |
| `extensions/construct-x-construction-progress/` | cxcp 0.1.0: `ontology/` (58 Tripel), `shapes/` (69 Tripel, 1× `sh:sparql`), `examples/` (TTL + JSON-LD + Runtime-JSON), `queries/`, README, documentation.html |
| `examples/construct-x-baufortschritt-beispiel/` | End-to-End-Beispiel (3 Daten-Revisions, 3 Notifications, Result) |
| `examples/construct-x-icdd-beispiele/` | 2 ICDD-Container (ISO 21597) + README + documentation.html |
| `contexts/construct-x-context.jsonld` | JSON-LD-Kontext (0.1.0, `@version: 1.1`, 380 `@context`-Einträge, inkl. `cxcp`-Präfix + 8 Terme) |
| `contexts/validation/test/test-doc-reference.md` | Referenz-Explanation der Test-Doku (inkl. Node N11 = cxcp) |
| `construct-x-converters/HANDOFF.md` | Handover-Dokument des Converter-Repos |
