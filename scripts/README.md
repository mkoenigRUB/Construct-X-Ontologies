# scripts/ — Verifikationsskripte (rechnerunabhängig)

Diese vier Skripte sind der **kanonische Validierungslauf** des Ontologie-Pakets.
Sie liegen im Repo, damit der Lauf auf **jedem Rechner** identisch reproduzierbar ist
(früher lagen sie nur in `%TEMP%\opencode\` — das ist nicht sync-fähig).

Ausführung: **immer aus dem Repo-Root** (die Skripte nutzen relative Pfade).

## Voraussetzungen: Python-Venv

```powershell
# aus dem Repo-Root; Versionen exakt (rdflib 7.6.0 + pySHACL 0.40.1)
python -m venv .venv
& .\.venv\Scripts\pip.exe install "rdflib==7.6.0" "pySHACL==0.40.1"
```

`.venv/` ist in `.gitignore` — das Venv wird je Rechner neu angelegt.
(Wichtig: pySHACL wird über `validate(data_graph=…, shacl_graph=…, infer='none', advanced=True)`
gerufen. Das Keyword `shacl_graph=` ist korrekt — ein Aufruf mit `shapes_graph=`
würde die Shapes stillschweigend verwerfen und 0 Shapes melden, s. VALIDATION.md Note 18.)

## Die vier Läufe

| Skript | Zweck | Erwartetes Ergebnis |
|---|---|---|
| `verify_parse.py` | TTL- + RDF/XML-Parsen aller Dateien (exkl. `.venv`), Isomorphie-Check der TTL/RDF/XML-Paare | `TTL count 104`, `OWL count 51`, `TTL ERRORS none`, `OWL ERRORS none`, `ISO PAIRS 51 MISMATCH none` |
| `verify_neg.py` | 10 Negativtests A–J (jeder **muss** eine Verletzung auslösen); gepinnte Eingabe-Bytes gegen Datei-Drift | `=== NEG TESTS: 10 FAIL: 0` |
| `verify_shacl.py` | 15 SHACL-Runs (Beispiel vs. Core- + Vokabular-Profile, SKOS-Vokabulare in den Data-Graph) | `=== RUNS: 15 FAIL: 0`, alle `[ok] CONFORM (0 viol)` |
| `verify_manifest.py` | MANIFEST.json ↔ in-file `owl:versionInfo` + Präfix-Kollisionscheck | `TOTAL entries: 54 … MISSING: 0 … version mismatches: 0` (bekannt: `COLLISION IRI http://purl.org/dc/terms/ dct dcterms` — vorbestehend, nicht Teil des Construct-X-Namenraums) |

Ablauf:

```powershell
$py = ".venv\Scripts\python.exe"
& $py scripts\verify_parse.py
& $py scripts\verify_neg.py
& $py scripts\verify_shacl.py
& $py scripts\verify_manifest.py
```

## Negativtest-Referenz (verify_neg.py)

| # | Mutierung | Profil |
|---|---|---|
| A | `identifier` fehlt bei `Project` | project core |
| B | `progress` = 150 | project core |
| C | `plannedEnd` := `plannedStart` − 1 Tag (`sh:sparql`) | project core |
| D | `phaseType` aus fremdem Vokabular (`sh:in`) | project vocab |
| E | `identifier` fehlt bei `Contract` | contract core |
| F | `validUntil` := `validFrom` − 1 Tag (`sh:sparql`) | contract core |
| G | `contractType` fehlt (minCount) | contract core |
| H | `subjectType` aus fremdem Vokabular (`sh:in`) | contract vocab |
| I | `taskType` fehlt bei `TaskRequested` (`sh:sparql`) | notification-content |
| J | cxcp Transport-Output auf fremdes Paket (`sh:sparql`) | cxcp-Extension |

Stand: 2026-11-14 (nach Commit `1ff099f`); letzter grüner Lauf 2026-11-13 auf Windows/PowerShell
(rdflib 7.6.0 / pySHACL 0.40.1).
