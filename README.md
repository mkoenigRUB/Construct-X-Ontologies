# Construct-X Ontologies

Das Construct-X Ontologie-Paket: 8 Domänen-Ontologien, 10 Link-Ontologien, 21 SKOS-Vokabulare und 1 externe Extension (Stand `MANIFEST.json`), jeweils mit SHACL-Profilen und Beispieldaten.

Starten mit:

- `MANIFEST.json` — Modul-Register mit Versionen
- `VALIDATION.md` / `AUDIT.md` — Validierungsstatus
- `documentation/ONTOLOGY-LINKING-RULE.md` — Architekturregeln für Link-Ontologien
- `documentation/CONSTRUCT-X-ONTOLOGIES.html` — interaktive Übersicht
- `usecase/` — Anwendungszenario und Komponentenüberblick
- `examples/construct-x-doppelboden-beispieldaten/` — durchgängiges Beispiel inkl. Exchange-Package-Dokumentation (u. a. §6.1 „Plain JSON v2 / Envelope")
- `extensions/construct-x-construction-progress/` — Baufortschritt-Extension auf Basis der IoC Process Ontology (externes IRI-Schema `w3id.org/construct-x/construction-progress#`)
- `examples/construct-x-baufortschritt-beispiel/` — End-to-End-Beispiel: Lieferung → Transport → Einbau bis zum BIM-Konstruktionselement
- `examples/construct-x-icdd-beispiele/` — zwei ICDD-Container (ISO 21597) als Beispiel für die Liefer-/Verknüpfungsschicht

## Modules (as of 2026-10-30)

| Module                          | Type            | Version |
|---------------------------------|-----------------|---------|
| `construction-schedule`         | Domain ontology | 0.5.0   |
| `breakdown-structure`           | Domain ontology | 0.7.0   |
| `gaeb-boq`                      | Domain ontology | 0.5.0   |
| `construction-progress-report`  | Domain ontology | 0.1.0   |
| `construction-site`             | Domain ontology | 0.2.0   |
| `construction-delivery`         | Domain ontology | 0.1.0   |
| `built-asset`                   | Domain ontology | 0.1.0   |
| `notification-content`          | Domain ontology | 0.1.1   |
| `schedule-breakdown-link`       | Link ontology   | 0.6.0   |
| `schedule-boq-link`             | Link ontology   | 0.2.1   |
| `schedule-progress-report-link` | Link ontology   | 0.1.0   |
| `site-breakdown-link`           | Link ontology   | 0.1.0   |
| `delivery-site-link`            | Link ontology   | 0.1.0   |
| `delivery-boq-link`             | Link ontology   | 0.1.0   |
| `schedule-delivery-link`        | Link ontology   | 0.1.0   |
| `schedule-site-link`            | Link ontology   | 0.1.0   |
| `built-asset-breakdown-link`    | Link ontology   | 0.1.0   |
| `site-built-asset-link`         | Link ontology   | 0.1.0   |
| `construct-x-construction-progress` | Extension     | 0.1.0   |

> `construct-x-construction-progress` ist eine **Extension** (keine der 8 Domänen): eine schlanke Erweiterung der externen IoC Process Ontology (`w3id.org/ioc`) und von BOT (`w3id.org/bot`) mit eigenem IRI-Schema (`w3id.org/construct-x/construction-progress#`). Deshalb eigener `extensions/`-Ordner und eigene `MANIFEST.json`-Sektion — die Linking Rule (Querrelationen nur in Link-Ontologien zwischen Construct-X-Domänen) greift nicht.

The Construction Site and Construction Delivery modules (plus their four link ontologies and six SKOS vocabularies) were added on 22 Oct 2026 from the working document "Ontologien & Standards für Baustellen".

On 22 Oct 2026 the Construction Site module was advanced to 0.2.0 to support **time-varying area allocation (Flächenbelegung)**: a new `AreaAllocation` class, the `area-allocation-status` SKOS vocabulary, a dedicated SHACL profile (with an overlap-conflict rule) and the `schedule-site-link` link ontology. The Built Asset domain (0.1.0) and the `site-built-asset-link` link ontology were added in the same revision.

On 30 Oct 2026 the `built-asset-breakdown-link` ontology (0.1.0, added to the package together with the Built Asset domain) was registered in `MANIFEST.json` and re-verified end-to-end (RDF parse, isomorphic RDF/XML mirror, SHACL against `built-asset-links-example.ttl` and the integrated link example, linking-rule architecture checks).

On 4 Nov 2026 the `notification-content` module (0.1.1, on disk since the exchange-package work and already referenced by the Converters' CURIE register and the doppelboden example notification) was registered in `MANIFEST.json`, gained RDF/XML mirrors for all five TTL files and the example data file `notification-content-example.ttl`; the full package was re-verified (SHACL 10/10 runs conform, 0 violations).

On 4 Nov 2026 the combined JSON-LD context `contexts/construct-x-context.jsonld` (0.1.0, `@version: 1.1`, context IRI `https://www.construct-x.org/context/construct-x/0.1.0`) was added. It covers all 8 domain ontologies, all 10 link ontologies and all 21 SKOS vocabularies in a single file (371 `@context` entries). Bare term names that collide across modules are mapped to exactly one bare term entry and remain usable via their module prefix. The context is registered in `MANIFEST.json` under `json_ld_context` and verified end-to-end by the self-contained Jena 4.10.0 project `contexts/validation/` (PASS on 2026-11-04: test document expands to 42 triples / 64 IRIs, roundtrip 42 → 42).

On 5 Nov 2026 the shared **Construct-X SDK** was extracted from the converter builds into the new `construct-x-sdk/` module of the `construct-x-converters` repository (`org.construct-x:construct-x-sdk:0.1.0-SNAPSHOT`, Java 25 / Jena 4.10.0, no Spring) as "Ebene 1" of the use-case architecture. It de-duplicates `ConxCurieRegister`, `RdfInput`, `PlainJsonModelWriter` and the base `ConxNamespaces`, and adds the shared helpers `IriFactory`, `OntologyRegistry`, `ShaclValidatorHelper` and `ProvenanceHelper` (PROV-O annotations). The SDK is registered in `MANIFEST.json` under `sdk`; all four builds re-verified on 2026-11-05 (SDK 81/81, GAEB 32/32, MS-Project 33/33, RDF 15/15 — 161/161 tests, BUILD SUCCESS).

On 6 Nov 2026 the **Construction Progress Extension** `cxcp` (0.1.0) was integrated under `extensions/construct-x-construction-progress/` and registered in `MANIFEST.json` (new `extensions` section, 41 entries). The combined JSON-LD context was extended with the `cxcp` prefix + 8 terms (380 `@context` entries; `@version` stays 1.1 due to a Jena 4.10.0 loader quirk) and re-verified (PASS: 48 triples / 77 IRIs, roundtrip 48 → 48). The end-to-end Baufortschritt example (`examples/construct-x-baufortschritt-beispiel/`) and two ICDD container examples (`examples/construct-x-icdd-beispiele/`, ISO 21597) were added; the Doppelboden container's embedded notification-content ontology was synced to 0.1.1. Full package re-verified: 86 TTL + 39 RDF/XML parsed, SHACL 11/11 conform (incl. a new cxcp run with `sh:sparql` constraint + negative test), all ICDD payload checksums OK.

## Related repository: Construct-X Converters

Die Konverter-Dienste (GAEB BoQ, MS Project, RDF) mit ihren Web-Frontends und Docker-Compose-Setups sind im separaten Repository **`construct-x-converters`** (Java 25 / Spring Boot 3.5 / Apache Jena 4.10). Dort auch die vollständige Spezifikation des Plain-JSON-Formats v2 und der Exchange-Package-Envelope; die Beispiel-Daten in `examples/` folgen derselben Konvention.

## Use Case (as of 2026-10-27)

`usecase/` documents an end-to-end scenario (general contractor → subcontractor → logistics provider) showing how the ontologies enable cross-organisation data exchange, plus a component overview in three layers (shared Construct-X components incl. an SDK, reusable converter services, company-specific integration services). See `usecase/index.html` for the interactive version.
